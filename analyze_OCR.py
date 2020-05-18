"""Script to analyze and score entities in the OCRed Text

Attributes:
    NAME_COMPANY_THRESHOLD (float): Min confidence required to classiify as
                                    name/company
    TEL_MIN_LENGTH (int): min length to be a tel number
    THRESHOLD_HIGH (float): Max threshold for checking string similarity
    THRESHOLD_LOW (float): Min threshold for checking string similarity
"""
import re
from helper import helper, EMAIL_REGEX, PROPER_WEBSITE_REGEX, \
    PARTIAL_WEBSITE_REGEX, ADDRESS_REGEX, TEL_REGEX, FAX_REGEX
import utils
# from tqdm import tqdm
import usaddress
from pprint import pprint
import math
import copy
# import time

NAME_COMPANY_THRESHOLD = 0.05
TEL_MIN_LENGTH = 4
THRESHOLD_HIGH = 0.5
THRESHOLD_LOW = 0.2


def match_regex(pattern, string):
    """find all substrings which match the pattern

    Args:
        pattern (str): REGEX pattern
        string (str): string to extract substrings

    Returns:
        list: list of substrings which match the pattern
    """
    # print(pattern, string.lower())
    return re.findall(pattern, string.lower(), re.IGNORECASE)


def get_font_ratio(avg_font_size, ele_font_size):
    """Returns the font ratio

    Args:
        avg_font_size (int): self explanatory
        ele_font_size (int): the element whose font we are comparing

    Returns:
        float: the ratio between the avg font size and the element's font size
    """
    # 0 if font size is lesser than avg font size
    # if font size is greater than 2 * avg, then 1
    ele_font_size = avg_font_size \
        if avg_font_size > ele_font_size else ele_font_size
    ele_font_size = (avg_font_size * 2) \
        if (avg_font_size * 2) < ele_font_size else ele_font_size

    return (ele_font_size / avg_font_size) - 1


def extract_number(text):
    """Get numbers from the text

    Args:
        text (str): string

    Returns:
        str: numbers in the string
    """
    nums = re.findall(r'\b\d+\b', text)
    return ''.join(nums)


def extract_designation(text):
    """Get designation from text

    Args:
        text (str): string

    Returns:
        str: Designation in the string
    """

    words = text.split(' ')
    designation = ''
    for i, word in enumerate(words):
        for _designation in list(helper['designation']):
            if len(match_regex(_designation, word)) > 0:
                if i > 0:
                    designation += words[i - 1] + ' '
                designation += word
                if i == 0 and (i + 1) < len(words):

                    designation += ' ' + words[i + 1]
                    if words[i + 1].lower() in ['in', 'of', 'at']:
                        if (i + 2) < len(words):
                            designation += ' ' + words[i + 2]

                return designation

    for i, word in enumerate(words):
        for _designation in list(helper['corporate levels']):
            if len(match_regex(_designation, word)) > 0:

                designation += word
                return designation
    return designation.strip()


def extract_name(text):
    """Get name from text

    Args:
        text (str): string

    Returns:
        str: name in the string
    """
    return utils.strip_punctuations(text).strip()


def extract_company(text):
    """Get Company from text

    Args:
        text (str): string

    Returns:
        str: Company in the string
    """
    return utils.strip_punctuations(text).strip()


def extract_website(text):
    """Get websites from text

    Args:
        text (str): string

    Returns:
        str: websites in the string
    """
    matches = match_regex(pattern=PROPER_WEBSITE_REGEX, string=text)

    if len(matches) > 0:
        return matches[0]

    matches = match_regex(pattern=PARTIAL_WEBSITE_REGEX, string=text)

    if len(matches) > 0:
        return matches[0]

    return text


def get_template(_for='result'):
    """Get templates for results/blocks/ent_line_probabilities

    Args:
        _for (str, optional): (result or block or ent_line_probs)

    Returns:
        dict: with the entities prefilled with default values/scores
    """
    if _for == 'result':
        template = {
            "name": "",
            "company": "",
            "designation": "",
            "email": [],
            "address": "",
            "website": [],
            "phone": [],
            "fax": [],
        }
    elif _for == 'block':
        template = {
            'text': "",
            'font_size': 0,
            'confidence': {'name': 0,
                           'company': 0,
                           'designation': 0,
                           'email': 0,
                           'address': 0,
                           'website': 0,
                           'phone': 0,
                           'fax': 0
                           },
            'used': False
        }
    elif _for == 'entity_line_probabilities' or _for == 'entity_line_spans':
        return {'name': [],
                'company': [],
                'designation': [],
                'email': [],
                'address': [],
                'website': [],
                'phone': [],
                'fax': []
                }
    return template


def preprocess_ocr_line(line):
    """Preprocess OCR line

    Args:
        line (str): OCR line output

    Returns:
        str: processed OCR line
    """
    # sometimes email have extra space around @, . character
    if '@' in line:
        cleaned_words = []
        line_split = line.split('@')
        for word in line_split:
            cleaned_words.append(word.strip())
        line = '@'.join(cleaned_words)

    return line


def make_blocks_for_lines(ocr_lines, ocr_bboxes):
    """Creates BCR(buisness card reader) dict which stores all line
    probabilites, avg font size of the card, etc

    Args:
        ocr_lines (list): OCR lines
        ocr_bboxes (list): list containing bbox coordinates for each OCR line

    Returns:
        dict: BCR dict
    """
    BCR = {'blocks': [], 'avg_font_size': 0}
    font_sizes = []
    for ocr_line, ocr_bbox in zip(ocr_lines, ocr_bboxes):
        (x1, y1, x2, y2) = ocr_bbox

        block = get_template(_for='block')
        clean_line = preprocess_ocr_line(ocr_line)
        block['text'] = clean_line
        block['font_size'] = int(y2 - y1)
        font_sizes.append(block['font_size'])

        BCR['blocks'].append(block)

    avg_font_size = sum(font_sizes) / len(font_sizes)
    BCR['avg_font_size'] = avg_font_size
    return BCR


def score_name(ocr_lines, BCR):
    # steps:
    #   1. get all keywords(potential emails from which we can get a name)
    #   2. compare all other lines and compare similarity scores with extracted
    #      keywords.
    #   3. Check if the similarity is higher than threshold, if so assign
    #      weightage of similarity * 0.5
    #   4. Assign 0.2 weightage by font size
    #   5. If line contains any of the common names, add weightage of 0.3
    #   6. If line contains any of the titles, then add weightage of 0.1

    keywords = []

    for i, block in enumerate(BCR['blocks']):

        if BCR['blocks'][i]['confidence']['email'] > 0:
            email_line = block['text'].lower()

            if len(email_line) > 0:
                email_line = email_line.strip()
                email_line = email_line.split('@')[0]

                email_line = email_line.replace('.', ' ')

                email_line = email_line.replace('e-mail:', '')
                email_line = email_line.replace('e-mail.', '')
                email_line = email_line.replace('e-mail', '')
                email_line = email_line.replace('email:', '')
                email_line = email_line.replace('email.', '')
                email_line = email_line.replace('email', '')
                email_line = email_line.replace('mail', '')
                email_line = email_line.replace('mail:', '')
                email_line = email_line.replace('mail.', '')
                # email_line = email_line.strip()

                if len(email_line) > 0:
                    keywords.append(email_line.strip())
    keywords = list(set(keywords))
    # print('name keywords:', keywords)
    for i, block in enumerate(BCR['blocks']):

        if BCR['blocks'][i]['confidence']['email'] > 0 or \
                BCR['blocks'][i]['confidence']['website'] > 0:
            continue

        line = block['text'].lower()
        clean_line = utils.strip_punctuations(line, True)
        words = line.split(' ')

        for keyword in keywords:
            if keyword == '' or len(keyword) == 0:
                continue
            sim = utils.ssimilarity(line, keyword.lower())

            if sim >= THRESHOLD_HIGH:
                BCR['blocks'][i]['confidence']['name'] += sim * 0.5

            clean_keyword = utils.strip_punctuations(keyword.lower(), True)
            # print(clean_keyword, clean_line, sim)
            # print(keyword, line, sim)
            if clean_keyword in clean_line or clean_line in clean_keyword:
                BCR['blocks'][i]['confidence']['name'] += 0.5
            elif len(clean_keyword) > 1:
                # sometimes first letter is short form of first name so remove
                # that eg: for John Lamos, keyword could be jlamos
                clean_keyword = clean_keyword[1:]
                if clean_keyword in clean_line or clean_line in clean_keyword:
                    BCR['blocks'][i]['confidence']['name'] += 0.5

        BCR['blocks'][i]['confidence']['name'] += get_font_ratio(
            BCR['avg_font_size'], BCR['blocks'][i]['font_size']) * 0.2

        for word in words:
            if word in list(helper['name']):
                BCR['blocks'][i]['confidence']['name'] += 0.43
                break

        for title_pattern in list(helper['title']):
            if match_regex(title_pattern, line):
                BCR['blocks'][i]['confidence']['name'] += 0.1

    return BCR


def score_company(ocr_lines, BCR):
    # steps:
    #   1. get all keywords(potential emails, websites
    #                       from which we can get company name)
    #   2. compare all other lines and compare similarity scores with extracted
    #      keywords.
    #   3. Check if the similarity is higher than threshold, if so assign
    #      weightage of similarity * 0.8
    #   4. Assign 0.2 weightage by font size
    keywords = []
    for i, block in enumerate(BCR['blocks']):

        if BCR['blocks'][i]['confidence']['website'] > 0:
            website_line = extract_website(block['text'])

            website = website_line.split('.')

            if len(website) > 0:
                # exclude .com, .org etc and get domain name
                website = website[-2]
                website_line = website

            website_line = website_line.lower()
            if len(website_line) > 0:

                website_line.replace('website:', '')
                website_line.replace('website.', '')
                website_line.replace('website', '')
                website_line.replace('webpage:', '')
                website_line.replace('webpage.', '')
                website_line.replace('webpage', '')
                website_line.replace('visit:', '')
                website_line.replace('visit.', '')
                website_line.replace('visit', '')

                keywords.append(website_line.strip())

        if BCR['blocks'][i]['confidence']['email'] > 0:
            email_line = block['text'].lower()

            if len(email_line) > 0:
                if '@' in email_line:
                    email_line = email_line.split('@')[1]
                if '.' in email_line:
                    email_line = email_line.split('.')[0]
            if len(email_line) > 0:
                email_line = email_line.replace('e-mail:', '')
                email_line = email_line.replace('e-mail.', '')
                email_line = email_line.replace('e-mail', '')
                email_line = email_line.replace('email:', '')
                email_line = email_line.replace('email.', '')
                email_line = email_line.replace('email', '')
                email_line = email_line.replace('mail', '')
                email_line = email_line.replace('mail:', '')
                email_line = email_line.replace('mail.', '')
                # email_line = email_line.strip()
                keywords.append(email_line.strip())
    keywords = list(set(keywords))
    # print('company keywords:', keywords)
    for i, block in enumerate(BCR['blocks']):

        line = block['text'].lower()
        clean_line = utils.strip_punctuations(line)

        for company_term in list(helper['company']):
            if len(match_regex(company_term, clean_line)) > 0:
                BCR['blocks'][i]['confidence']['company'] += 0.4

        if (BCR['blocks'][i]['confidence']['email'] > 0) or \
                (BCR['blocks'][i]['confidence']['website'] > 0):
            continue

        for keyword in keywords:
            if keyword == '' or len(keyword) == 0:
                continue
            sim = utils.ssimilarity(line, keyword.lower())

            if sim > THRESHOLD_LOW:
                BCR['blocks'][i]['confidence']['company'] += sim * 0.8

        BCR['blocks'][i]['confidence']['company'] += get_font_ratio(
            BCR['avg_font_size'], BCR['blocks'][i]['font_size']) * 0.2
    return BCR


def score_designation(ocr_lines, BCR):
    # steps:
    #   1. Check if a line exists after the name and if so assign score of 0.2
    #      (This assumes that the lines are ordered)
    #   2. compare all other lines and compare similarity scores with common
    #      designations defined in helper
    #   3. Check if the similarity is higher than threshold, if so assign
    #      weightage of similarity * 0.55
    #   4. Assign 0.2 weightage by font size
    for i, block in enumerate(BCR['blocks']):

        # if BCR['blocks'][i]['confidence']['name'] > 0:
        #     if (i + 1) < len(BCR['blocks']):
        #         BCR['blocks'][i]['confidence']['designation'] += 0.2

        line = block['text'].lower()

        for designation in list(helper['designation']):
            if len(match_regex(designation, line)) > 0:
                BCR['blocks'][i]['confidence']['designation'] += 0.55
                break
        for designation in list(helper['corporate levels']):
            if len(match_regex(designation, line)) > 0:
                BCR['blocks'][i]['confidence']['designation'] += 0.6
                break

        # BCR['blocks'][i]['confidence']['name'] += get_font_ratio(
        #     BCR['avg_font_size'], BCR['blocks'][i]['font_size']) * 0.2
    return BCR


def score_email(ocr_lines, BCR):
    """Score whether there are emails in the card

    Args:
        ocr_lines (list): list of OCR lines
        BCR (dict): BCR dict

    Returns:
        dict: BCR dict updated with email confidence for each line
    """
    confidence = 1.0
    for i, block in enumerate(BCR['blocks']):
        matches = match_regex(EMAIL_REGEX, block['text'])

        if len(matches) > 0:
            BCR['blocks'][i]['confidence']['email'] += confidence
        elif '@' in block['text'] or 'email' in block['text'] or \
                'mail' in block['text']:
            BCR['blocks'][i]['confidence']['email'] += 0.7
    return BCR


def score_address(ocr_lines, BCR):
    """Score whether there's an address in the card

    Args:
        ocr_lines (list): list of OCR lines
        BCR (dict): BCR dict

    Returns:
        dict: BCR dict updated with address confidence for each line
    """
    street_tags = ["AddressNumber",
                   "StreetNamePreDirectional",
                   "StreetNamePreType",
                   "StreetName",
                   "StreetNamePostType",
                   "StreetNamePostDirectional",
                   "OccupancyType",
                   "OccupancyIdentifier"
                   ]
    place_country_zip_tags = ["PlaceName",
                              "StateName", "ZipCode", "CountryName"]
    num_common_tags = 0
    for i, block in enumerate(BCR['blocks']):

        try:
            tags_dict, classification = usaddress.tag(block['text'])

        except usaddress.RepeatedLabelError:
            # print('Probabably Phone number or Fax')
            continue

        # ordereddict to list
        tags = list(tags_dict)

        num_common_tags = len(utils.common_pairs(
            place_country_zip_tags, tags))

        if classification == 'Street Address' and \
                BCR['blocks'][i]['confidence']['phone'] < 0.5:
            BCR['blocks'][i]['confidence']['address'] += 0.8
            continue
        for tag in tags:

            if tag in street_tags:
                street_tags.remove(tag)
                BCR['blocks'][i]['confidence']['address'] += 0.2

            if tag in place_country_zip_tags:
                place_country_zip_tags.remove(tag)

                if tag == 'ZipCode' and len(tags_dict[tag]) > 5 and \
                        len(tags_dict[tag]) < 4:
                    BCR['blocks'][i]['confidence']['address'] -= 0.25
                    # zip code cant have len more than 5 and less than 4
                    continue

                if tag == 'StateName' or tag == 'PlaceName':
                    _name = utils.strip_punctuations(
                        tags_dict[tag].lower()).strip()

                    if _name in helper['phone'] or \
                            _name in helper['fax']:
                        BCR['blocks'][i]['confidence']['address'] -= 0.25
                        continue

                if (tag == 'ZipCode' or tag == 'CountryName') and \
                        num_common_tags >= 2:
                    BCR['blocks'][i]['confidence']['address'] += 0.8
                    continue

                BCR['blocks'][i]['confidence']['address'] += 0.55

    return BCR


def score_website(ocr_lines, BCR):
    """Score whether there are websites in the card

    Args:
        ocr_lines (list): list of OCR lines
        BCR (dict): BCR dict

    Returns:
        dict: BCR dict updated with website confidence for each line
    """
    confidence = 1.0
    for i, block in enumerate(BCR['blocks']):

        line = block['text'].lower()
        # print(block)
        proper_matches = match_regex(pattern=PROPER_WEBSITE_REGEX,
                                     string=line)
        partial_matches = match_regex(pattern=PARTIAL_WEBSITE_REGEX,
                                      string=line)
        clean_partial_matches = []

        if len(proper_matches) > 0:
            BCR['blocks'][i]['confidence']['website'] += confidence
            return BCR

        for match in partial_matches:
            extension = match.split('.')[-1]
            if len(extension) < 2:
                continue
            # check if the match contains any alphabets and extension also
            # contains alphabets
            if not re.search('[a-zA-Z]+', match) or \
                    not re.search('[a-zA-Z]+', extension):
                continue
            match_split = line.split(match)

            if len(match_split[0]) > 0:
                # if the substring is part of email
                if match_split[0][-1] == '@':
                    continue
            clean_partial_matches.append(match)
        if len(clean_partial_matches) > 0:
            BCR['blocks'][i]['confidence']['website'] += 0.77

    return BCR


def score_number(ocr_lines, BCR):
    """Score whether there are numbers(phone/fax) in the card

    Args:
        ocr_lines (list): list of OCR lines
        BCR (dict): BCR dict

    Returns:
        dict: BCR dict updated with phone/fax confidence for each line
    """
    for i, block in enumerate(BCR['blocks']):
        numbers = extract_number(block['text'])
        clean_text_list = utils.strip_punctuations(
            block['text'].lower()).split(' ')
        if len(numbers) > TEL_MIN_LENGTH:

            for tel_dict in TEL_REGEX:
                pattern, confidence = tel_dict['regex'], \
                    tel_dict['confidence']

                matches = match_regex(pattern, numbers)

                if len(matches) > 0:
                    BCR['blocks'][i]['confidence']['phone'] += confidence
                    if len(utils.common_pairs(
                            helper['phone'], clean_text_list)) > 0:
                        BCR['blocks'][i]['confidence']['phone'] += 0.5
            for fax_dict in FAX_REGEX:
                pattern, confidence = fax_dict['regex'], \
                    fax_dict['confidence']

                matches = match_regex(pattern, numbers)

                if len(matches) > 0:

                    if len(utils.common_pairs(
                            helper['fax'], clean_text_list)) > 0:
                        BCR['blocks'][i]['confidence']['fax'] += 0.8
        else:
            continue

    return BCR


def analyze_OCR(ocr_results, silent=True):
    """This is main function to score all the requried entities amd gathering
    results.

    Args:
        ocr_results (list): list of detected OCR lines
        silent (bool, optional): whether to print the final results

    Returns:
        dict: results which contains the extracted entities as values and
              entities like name, phone number as keys.
    """
    bboxes = []
    lines = []
    for (bbox, line) in ocr_results:
        bboxes.append(bbox)
        lines.append(line)

    BCR = make_blocks_for_lines(lines, bboxes)
    # print('scoring ...')
    BCR = score_email(lines, BCR)
    # print('scoring emails done')
    BCR = score_number(lines, BCR)
    # print('scoring numbers done')
    BCR = score_website(lines, BCR)
    # print('scoring website done')
    BCR = score_company(lines, BCR)
    # print('scoring company done')
    BCR = score_name(lines, BCR)
    # print('scoring name done')
    BCR = score_designation(lines, BCR)
    # print('scoring designation done')
    BCR = score_address(lines, BCR)
    # print('scoring address done')

    results = gather_results(copy.deepcopy(BCR))
    if not silent:
        pprint(results)
    return results


def gather_results(BCR):
    """Gathers results for each line given the entities confidences.

    Args:
        BCR (dict): The dict which contains probabilites for each ent for every
                    line

    Returns:
        dict: results which contains the extracted entities as values and
              entities like name, phone number as keys.
    """
    results = get_template(_for='result')

    # dict where entities are keys and corresponding values are list containing
    # tuples in form of (line_number, probability).
    # {
    #   'name' : [(0, 0.403), (5, 0.3)]
    #   'company': [(1, 0.8), (5, 0.6)]
    #    ...
    # }
    # ^ in example dict above name ent is predicted on lines 0 and 1 with scores
    #  0.403 and 0.3 respectively.
    #
    entity_line_probabilities = get_template(_for='entity_line_probabilities')

    for i, block in enumerate(BCR['blocks']):

        confidence = block['confidence']

        for ent, score in confidence.items():

            if math.ceil(score) == 0:
                continue

            entity_line_probabilities[ent].append((i, score))

    for ent, _list in entity_line_probabilities.items():

        entity_line_probabilities[ent] = sorted(
            _list, key=lambda x: x[1], reverse=True)
    # pprint(entity_line_probabilities)

    number_pattern = TEL_REGEX[0]['regex']
    extracted_results = []

    for i, block in enumerate(BCR['blocks']):

        line = block['text'].lower()
        clean_line = utils.strip_punctuations(line)
        confidence = block['confidence']

        if confidence['fax'] > 0:

            splits = clean_line.split('fax')

            if len(splits) > 1:

                splits = splits[1:]

            else:

                splits = clean_line.split('f')

                if len(splits) > 1:
                    splits = splits[1:]

            for phone_term in helper['phone']:
                _line = ''.join(splits)
                if len(_line) == 0:
                    break
                if phone_term not in _line:
                    continue

                _splits = _line.split(phone_term)
                # if the phone term is not present continue
                if len(_splits) == 1:
                    continue
                # if the phone term is present, then use the first half of the
                # split with the phone term
                splits = _splits[:1]

            for split in splits:

                fax_numbers = match_regex(number_pattern, extract_number(split))

                for fax_number in fax_numbers:
                    if fax_number not in extracted_results:
                        results['fax'].append(fax_number)
                        extracted_results.append(fax_number)

        if confidence['phone'] > 0:
            numbers = extract_number(line)
            _numbers = extract_number(clean_line)

            # print('extracted number:', numbers)
            # print('extracted _number:', _numbers)

            # if we get more results in the clean line then use that instead
            if len(_numbers) > len(numbers):
                numbers = _numbers
            phone_numbers = match_regex(number_pattern, numbers)
            # print(phone_numbers)
            for phone_number in phone_numbers:
                _line = utils.strip_punctuations(line, strip_space=True)
                # make sure that there are no characters in between the
                # extracted numbers
                if phone_number not in _line:
                    continue
                if phone_number not in extracted_results:
                    results['phone'].append(phone_number)
                    extracted_results.append(phone_number)

        if confidence['email'] > 0:
            emails = match_regex(EMAIL_REGEX, line)
            for email in emails:
                if email not in extracted_results:
                    results['email'].append(email)
                    extracted_results.append(email)
                    # to prevent website regex from matching parts of email
                    extracted_results.append(email.split('@')[0])

        if confidence['website'] > 0:
            if '.' in line:
                # sometimes we have extra space around .
                words = []
                line_split = line.split('.')
                for word in line_split:
                    if 'www' in word.lower():
                        w_start_index = word.find('w')
                        # some urls contain more wwws
                        words.append(word[:w_start_index] + 'www')
                        continue
                    words.append(word)

                line = '.'.join(words)
            websites = match_regex(PROPER_WEBSITE_REGEX, line)
            for website in websites:
                if website not in extracted_results:
                    results['website'].append(website)
                    extracted_results.append(website)

            if len(websites) == 0:
                partial_matches = match_regex(pattern=PARTIAL_WEBSITE_REGEX,
                                              string=line)
                for website in partial_matches:
                    extension = website.split('.')[-1]
                    # check if the match contains any alphabets and extension
                    # also contains alphabets
                    if not re.search('[a-zA-Z]+', website) or \
                            not re.search('[a-zA-Z]+', extension):
                        continue
                    website_split = line.split(website)

                    if len(website_split[0]) > 0:
                        # if the substring is part of email
                        if website_split[0][-1] == '@':
                            continue
                    if website not in extracted_results:
                        results['website'].append(website)
                        extracted_results.append(website)

    for i, block in enumerate(BCR['blocks']):

        line = block['text']
        clean_line = utils.strip_punctuations(line.lower()).strip()
        confidence = block['confidence']

        if confidence['address'] > 0.5:

            state_name_false_pos = False
            place_name_false_pos = False
            zip_false_pos = False
            tags, _ = usaddress.tag(line)
            # print(tags)

            if 'StateName' in list(tags):

                state_name = utils.strip_punctuations(
                    tags['StateName'].lower()).strip()
                state_name_false_pos = state_name in helper['phone'] or \
                    state_name in helper['fax']
            if 'PlaceName' in list(tags):

                place_name = utils.strip_punctuations(
                    tags['PlaceName'].lower()).strip()
                place_name_false_pos = place_name in helper['phone'] or \
                    place_name in helper['fax']

            if 'ZipCode' in list(tags):

                if extract_number(tags['ZipCode']) in extracted_results and \
                        state_name_false_pos:
                    zip_false_pos = True

            if len(tags) - (place_name_false_pos +
                            zip_false_pos + state_name_false_pos) > 1:
                results['address'] += line + '\n'

    designation_line_number = None
    name_line_number = None
    company_line_number = None

    if entity_line_probabilities['designation']:
        designation_line_number, _ = entity_line_probabilities['designation'][0]

        results['designation'] = extract_designation(
            BCR['blocks'][designation_line_number]['text'])
    if entity_line_probabilities['name']:
        name_line_number, name_score = entity_line_probabilities['name'][0]
        if name_score > NAME_COMPANY_THRESHOLD:
            results['name'] = extract_name(
                BCR['blocks'][name_line_number]['text'])

    if entity_line_probabilities['company']:

        company_line_number, company_score = \
            entity_line_probabilities['company'][0]

        if name_line_number is not None and \
                name_line_number == company_line_number:

            if name_score > company_score:

                if len(entity_line_probabilities['company']) > 1:
                    company_line_number, company_score = \
                        entity_line_probabilities['company'][1]

            else:

                if len(entity_line_probabilities['name']) > 1:

                    name_line_number, name_score = \
                        entity_line_probabilities['name'][1]

                    if name_score > NAME_COMPANY_THRESHOLD:

                        results['name'] = extract_name(
                            BCR['blocks'][name_line_number]['text'])

        if company_score > NAME_COMPANY_THRESHOLD:

            results['company'] = extract_company(
                BCR['blocks'][company_line_number]['text'])

    results['address'] = results['address'].strip('\n')

    # pprint(results)

    return results


if __name__ == "__main__":
    lines = []
    bboxes = []

    # analyze_OCR(ocr_results, silent=False)
