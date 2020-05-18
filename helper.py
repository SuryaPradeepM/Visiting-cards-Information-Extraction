# EMAIL_REGEX = r'(([^<>()\[\]\\.,;:\s@\"]+(\.[^<>()\[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))'
EMAIL_REGEX = r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'
PROPER_WEBSITE_REGEX = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})'
PARTIAL_WEBSITE_REGEX = r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'

ADDRESS_REGEX = r'\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?'

TEL_REGEX = [
    {
        # 'regex': r'([+][0 - 9]{1, 4}\s * )?(\([0-9]{1, 2}\)\s*)?([0-9]+[\s |\\\/.-]?){3, }',
        'regex': r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
        'confidence': 0.3
    }
    # {
    #     # 'regex': r"((tel | phon | dir)\w * ([. |:]) *\s*)([+][0-9]{1, 4}\s*)?(\([0-9]{1, 2}\)\s*)?([0-9]+[\s |\\\/.-]?){3, }",)
    #     'regex': r"(?<Telephone>([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)([ ]|[:]|\t|[-])*(?<Where>Home|Office|Work|Away|t|T|tel|Tel|Call|call|Phone|phone|p)|(?<Where>Home|Office|Work|Away|Fax|FAX|Phone|Daytime|Evening)([ ]|[:]|\t|[-])*(?<Telephone>([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)|(?<Telephone>([(]([0-9]){3}[)]([ ])?([0-9]){3}([ ]|-)([0-9]){4}))",
    #     'confidence': 0.5
    # }
]


MOB_REGEX = [
    {
        # 'regex': r'([+][0 - 9]{1, 4}\s * )?(\([0-9]{1, 2}\)\s*)?([0-9]+[\s |\\\/.-]?){3, }',
        'regex': r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
        'confidence': 0.3
    }
    # {
    #     'regex': r'((mobi | cell | hand)\w * ([. |:]) *\s*)([+][0-9]{1, 4}\s*)?(\([0-9]{1, 2}\)\s*)?([0-9]+[\s |\\\/.-]?){3, }',
    #     'confidence': 0.5
    # }
]

FAX_REGEX = [
    {
        # 'regex': r'([+][0 - 9]{1, 4}\s * )?(\([0-9]{1, 2}\)\s*)?([0-9]+[\s |\\\/.-]?){3, }',
        'regex': r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
        'confidence': 0.3
    }
    # {
    #     # 'regex': r'((fax)\w * ([. |:]) *\s*)([+][0-9]{1, 4}\s*)?(\([0-9]{1, 2}\)\s*)?([0-9]+[\s |\\\/.-]?){3, }',
    #     'regex': r'(?<Fax>([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)([ ]|[:]|\t|[-])*(?<Where>Fax|FAX|f|F)|(?<Where>Fax|FAX|f|F)([ ]|[:]|\t|[-])*(?<Fax>([0-9]|[ ]|[-]|[\(]|[\)]|ext.|[,])+)|(?<Fax>([(]([0-9]){3}[)]([ ])?([0-9]){3}([ ]|-)([0-9]){4}))',
    #     'confidence': 0.5
    # }
]


helper = {}


helper['designation'] = [
    r'\bapprentice\b',
    r'\bexecutive\b',
    r'\banalyst\b',
    r'\bcustomer\b',
    r'\bcoach\b',
    r'\badministrative\b',
    r'\badministrator\b',
    r'\bagent\b',
    r'\bhead\b',
    r'\bchief\b',
    r'\bdirector\b',
    r'\bvice\b',
    r'\bpresident\b',
    r'\bmanager\b',
    r'\bcoordinator\b',
    r'\bcounselor\b',
    r'\bsupervisor\b',
    r'\bassistant\b',
    r'\bspecialist\b',
    r'\bartist\b',
    r'\bworker\b',
    r'\bconsultant\b',
    r'\brepresentative\b',
    r'\barchitect\b',
    r'\bstaff\b',
    r'\bmember\b',
    r'\bdeveloper\b',
    r'\bengineer\b',
    r'\bexaminor\b',
    r'\bdoctor\b',
    r'\bprofessor\b',
    r'\bteacher\b',
    r'\blead\b',
    r'\bofficer\b',
    # levels
    r'\bintern\b',
    r'\bcandidate\b',
    r'\blead\b'
]

helper['corporate levels'] = [
    r'\bcae\b',
    r'\bcaio\b',
    r'\bcao\b',
    r'\bcbdo\b',
    r'\bcbo\b',
    r'\bcco\b',
    r'\bcdo\b',
    r'\bceo\b',
    r'\bcfo\b',
    r'\bcgo\b',
    r'\bchro\b',
    r'\bcino\b',
    r'\bcio\b',
    r'\bciso\b',
    r'\bcito\b',
    r'\bcko\b',
    r'\bclo\b',
    r'\bcmo\b',
    r'\bcno\b',
    r'\bcoo\b',
    r'\bcpo\b',
    r'\bcqo\b',
    r'\bcrdo\b',
    r'\bcro\b',
    r'\bcse\b',
    r'\bcso\b',
    r'\bcto\b',
    r'\bcvo\b',
    r'\bcwo\b',
    r'\bcxo\b',
    r'\bjunior\b',
    r'\bsenior\b']

helper['title'] = [
    r'\bprofessor\b',
    r'\bdr\b',
    r'\bdr.\b',
    r'\bdoc\b',
    r'\bdoc.\b',
    r'\bdoctor\b',
    r'\bmr\b',
    r'\bmr.\b',
    r'\bmrs.\b',
    r'\bmrs\b',
    r'\bms.\b',
    r'\bms\b',
    r'\bmiss\b',
    r'\brev\b',
    r'\brev.'
]

helper['titleTrash'] = [
    r'\bing\b',
    r'\bing.\b',
    r'\bing.-\b',
    r'\bphd\b',
    r'\bphd.-\b'
]

helper['street'] = [
    r'\bacres\b',
    r'\ballee\b',
    r'\balley\b',
    r'\bally\b',
    r'\baly\b',
    r'\banex\b',
    r'\bannex\b',
    r'\bannx\b',
    r'\banx\b',
    r'\bapproach\b',
    r'\barc\b',
    r'\barcade\b',
    r'\bav\b',
    r'\bave\b',
    r'\baven\b',
    r'\bavenu\b',
    r'\bavenue\b',
    r'\bavn\b',
    r'\bavnue\b',
    r'\bbay\b',
    r'\bbayoo\b',
    r'\bbayou\b',
    r'\bbch\b',
    r'\bbeach\b',
    r'\bbend\b',
    r'\bbg\b',
    r'\bbgs\b',
    r'\bbl\b',
    r'\bblf\b',
    r'\bblfs\b',
    r'\bbluf\b',
    r'\bbluff\b',
    r'\bbluffs\b',
    r'\bblvd\b',
    r'\bbnd\b',
    r'\bboardwalk\b',
    r'\bbot\b',
    r'\bbottm\b',
    r'\bbottom\b',
    r'\bboul\b',
    r'\bboulevard\b',
    r'\bboulv\b',
    r'\bbow\b',
    r'\bbr\b',
    r'\bbrae\b',
    r'\bbranch\b',
    r'\bbrdge\b',
    r'\bbrg\b',
    r'\bbridge\b',
    r'\bbrk\b',
    r'\bbrks\b',
    r'\bbrnch\b',
    r'\bbroadway\b',
    r'\bbrook\b',
    r'\bbrooks\b',
    r'\bbtm\b',
    r'\bburg\b',
    r'\bburgs\b',
    r'\bbyp\b',
    r'\bbypa\b',
    r'\bbypas\b',
    r'\bbypass\b',
    r'\bbyps\b',
    r'\bbyu\b',
    r'\bcamp\b',
    r'\bcanyn\b',
    r'\bcanyon\b',
    r'\bcape\b',
    r'\bcauseway\b',
    r'\bcauswa\b',
    r'\bcausway\b',
    r'\bcen\b',
    r'\bcent\b',
    r'\bcenter\b',
    r'\bcenters\b',
    r'\bcentr\b',
    r'\bcentre\b',
    r'\bci\b',
    r'\bcir\b',
    r'\bcirc\b',
    r'\bcircl\b',
    r'\bcircle\b',
    r'\bcircles\b',
    r'\bcircus\b',
    r'\bcirs\b',
    r'\bck\b',
    r'\bclb\b',
    r'\bclf\b',
    r'\bclfs\b',
    r'\bcliff\b',
    r'\bcliffs\b',
    r'\bclose\b',
    r'\bclub\b',
    r'\bcmn\b',
    r'\bcmns\b',
    r'\bcmp\b',
    r'\bcnter\b',
    r'\bcntr\b',
    r'\bcnyn\b',
    r'\bcommon\b',
    r'\bcommons\b',
    r'\bcor\b',
    r'\bcorner\b',
    r'\bcorners\b',
    r'\bcors\b',
    r'\bcottage\b',
    r'\bcourse\b',
    r'\bcourt\b',
    r'\bcourts\b',
    r'\bcove\b',
    r'\bcoves\b',
    r'\bcp\b',
    r'\bcpe\b',
    r'\bcr\b',
    r'\bcrcl\b',
    r'\bcrcle\b',
    r'\bcrecent\b',
    r'\bcreek\b',
    r'\bcres\b',
    r'\bcrescent\b',
    r'\bcresent\b',
    r'\bcrest\b',
    r'\bcrk\b',
    r'\bcrossing\b',
    r'\bcrossroad\b',
    r'\bcrossroads\b',
    r'\bcrscnt\b',
    r'\bcrse\b',
    r'\bcrsent\b',
    r'\bcrsnt\b',
    r'\bcrssing\b',
    r'\bcrssng\b',
    r'\bcrst\b',
    r'\bcrt\b',
    r'\bcswy\b',
    r'\bct\b',
    r'\bctr\b',
    r'\bctrs\b',
    r'\bcts\b',
    r'\bcurv\b',
    r'\bcurve\b',
    r'\bcv\b',
    r'\bcvs\b',
    r'\bcyn\b',
    r'\bdale\b',
    r'\bdam\b',
    r'\bdiv\b',
    r'\bdivide\b',
    r'\bdl\b',
    r'\bdm\b',
    r'\bdr\b',
    r'\bdriv\b',
    r'\bdrive\b',
    r'\bdrives\b',
    r'\bdrs\b',
    r'\bdrv\b',
    r'\bdv\b',
    r'\bdvd\b',
    r'\besplanade\b',
    r'\best\b',
    r'\bestate\b',
    r'\bestates\b',
    r'\bests\b',
    r'\bex\b',
    r'\bexp\b',
    r'\bexpr\b',
    r'\bexpress\b',
    r'\bexpressway\b',
    r'\bexpw\b',
    r'\bexpy\b',
    r'\bext\b',
    r'\bextension\b',
    r'\bextensions\b',
    r'\bextn\b',
    r'\bextnsn\b',
    r'\bexts\b',
    r'\bfall\b',
    r'\bfalls\b',
    r'\bferry\b',
    r'\bfield\b',
    r'\bfields\b',
    r'\bflat\b',
    r'\bflats\b',
    r'\bfld\b',
    r'\bflds\b',
    r'\bfls\b',
    r'\bflt\b',
    r'\bflts\b',
    r'\bford\b',
    r'\bfords\b',
    r'\bforest\b',
    r'\bforests\b',
    r'\bforg\b',
    r'\bforge\b',
    r'\bforges\b',
    r'\bfork\b',
    r'\bforks\b',
    r'\bfort\b',
    r'\bfrd\b',
    r'\bfrds\b',
    r'\bfreeway\b',
    r'\bfreewy\b',
    r'\bfrg\b',
    r'\bfrgs\b',
    r'\bfrk\b',
    r'\bfrks\b',
    r'\bfrry\b',
    r'\bfrst\b',
    r'\bfrt\b',
    r'\bfrway\b',
    r'\bfrwy\b',
    r'\bfry\b',
    r'\bft\b',
    r'\bfwy\b',
    r'\bgarden\b',
    r'\bgardens\b',
    r'\bgardn\b',
    r'\bgate\b',
    r'\bgateway\b',
    r'\bgatewy\b',
    r'\bgatway\b',
    r'\bgdn\b',
    r'\bgdns\b',
    r'\bglen\b',
    r'\bglens\b',
    r'\bgln\b',
    r'\bglns\b',
    r'\bgrden\b',
    r'\bgrdn\b',
    r'\bgrdns\b',
    r'\bgreen\b',
    r'\bgreens\b',
    r'\bgrn\b',
    r'\bgrns\b',
    r'\bgrov\b',
    r'\bgrove\b',
    r'\bgroves\b',
    r'\bgrv\b',
    r'\bgrvs\b',
    r'\bgtway\b',
    r'\bgtwy\b',
    r'\bharb\b',
    r'\bharbor\b',
    r'\bharbors\b',
    r'\bharbr\b',
    r'\bhaven\b',
    r'\bhavn\b',
    r'\bhbr\b',
    r'\bhbrs\b',
    r'\bheight\b',
    r'\bheights\b',
    r'\bhgts\b',
    r'\bhighway\b',
    r'\bhighwy\b',
    r'\bhill\b',
    r'\bhills\b',
    r'\bhiway\b',
    r'\bhiwy\b',
    r'\bhl\b',
    r'\bhllw\b',
    r'\bhls\b',
    r'\bhollow\b',
    r'\bhollows\b',
    r'\bholw\b',
    r'\bholws\b',
    r'\bhrbor\b',
    r'\bht\b',
    r'\bhts\b',
    r'\bhvn\b',
    r'\bhway\b',
    r'\bhwy\b',
    r'\binlet\b',
    r'\binlt\b',
    r'\bis\b',
    r'\bisland\b',
    r'\bislands\b',
    r'\bisle\b',
    r'\bisles\b',
    r'\bislnd\b',
    r'\bislnds\b',
    r'\biss\b',
    r'\bjct\b',
    r'\bjction\b',
    r'\bjctn\b',
    r'\bjctns\b',
    r'\bjcts\b',
    r'\bjunction\b',
    r'\bjunctions\b',
    r'\bjunctn\b',
    r'\bjuncton\b',
    r'\bkey\b',
    r'\bkeys\b',
    r'\bknl\b',
    r'\bknls\b',
    r'\bknol\b',
    r'\bknoll\b',
    r'\bknolls\b',
    r'\bky\b',
    r'\bkys\b',
    r'\bla\b',
    r'\blake\b',
    r'\blakes\b',
    r'\bland\b',
    r'\blanding\b',
    r'\blane\b',
    r'\blanes\b',
    r'\blck\b',
    r'\blcks\b',
    r'\bldg\b',
    r'\bldge\b',
    r'\blf\b',
    r'\blgt\b',
    r'\blgts\b',
    r'\blight\b',
    r'\blights\b',
    r'\blk\b',
    r'\blks\b',
    r'\bln\b',
    r'\blndg\b',
    r'\blndng\b',
    r'\bloaf\b',
    r'\block\b',
    r'\blocks\b',
    r'\blodg\b',
    r'\blodge\b',
    r'\bloop\b',
    r'\bloops\b',
    r'\blp\b',
    r'\bmall\b',
    r'\bmanor\b',
    r'\bmanors\b',
    r'\bmdw\b',
    r'\bmdws\b',
    r'\bmeadow\b',
    r'\bmeadows\b',
    r'\bmedows\b',
    r'\bmews\b',
    r'\bmi\b',
    r'\bmile\b',
    r'\bmill\b',
    r'\bmills\b',
    r'\bmission\b',
    r'\bmissn\b',
    r'\bml\b',
    r'\bmls\b',
    r'\bmn\b',
    r'\bmnr\b',
    r'\bmnrs\b',
    r'\bmnt\b',
    r'\bmntain\b',
    r'\bmntn\b',
    r'\bmntns\b',
    r'\bmotorway\b',
    r'\bmount\b',
    r'\bmountain\b',
    r'\bmountains\b',
    r'\bmountin\b',
    r'\bmsn\b',
    r'\bmssn\b',
    r'\bmt\b',
    r'\bmtin\b',
    r'\bmtn\b',
    r'\bmtns\b',
    r'\bmtwy\b',
    r'\bnck\b',
    r'\bneck\b',
    r'\bopas\b',
    r'\borch\b',
    r'\borchard\b',
    r'\borchrd\b',
    r'\boval\b',
    r'\boverlook\b',
    r'\boverpass\b',
    r'\bovl\b',
    r'\bovlk\b',
    r'\bparade\b',
    r'\bpark\b',
    r'\bparks\b',
    r'\bparkway\b',
    r'\bparkways\b',
    r'\bparkwy\b',
    r'\bpass\b',
    r'\bpassage\b',
    r'\bpath\b',
    r'\bpaths\b',
    r'\bpike\b',
    r'\bpikes\b',
    r'\bpine\b',
    r'\bpines\b',
    r'\bpk\b',
    r'\bpkway\b',
    r'\bpkwy\b',
    r'\bpkwys\b',
    r'\bpky\b',
    r'\bpl\b',
    r'\bplace\b',
    r'\bplain\b',
    r'\bplaines\b',
    r'\bplains\b',
    r'\bplaza\b',
    r'\bpln\b',
    r'\bplns\b',
    r'\bplz\b',
    r'\bplza\b',
    r'\bpne\b',
    r'\bpnes\b',
    r'\bpoint\b',
    r'\bpoints\b',
    r'\bport\b',
    r'\bports\b',
    r'\bpr\b',
    r'\bprairie\b',
    r'\bprarie\b',
    r'\bprk\b',
    r'\bprr\b',
    r'\bprt\b',
    r'\bprts\b',
    r'\bpsge\b',
    r'\bpt\b',
    r'\bpts\b',
    r'\bpw\b',
    r'\bpwy\b',
    r'\bquay\b',
    r'\brad\b',
    r'\bradial\b',
    r'\bradiel\b',
    r'\bradl\b',
    r'\bramp\b',
    r'\branch\b',
    r'\branches\b',
    r'\brapid\b',
    r'\brapids\b',
    r'\brd\b',
    r'\brdg\b',
    r'\brdge\b',
    r'\brdgs\b',
    r'\brds\b',
    r'\brest\b',
    r'\bri\b',
    r'\bridge\b',
    r'\bridges\b',
    r'\brise\b',
    r'\briv\b',
    r'\briver\b',
    r'\brivr\b',
    r'\brn\b',
    r'\brnch\b',
    r'\brnchs\b',
    r'\broad\b',
    r'\broads\b',
    r'\broute\b',
    r'\brow\b',
    r'\brpd\b',
    r'\brpds\b',
    r'\brst\b',
    r'\brte\b',
    r'\brue\b',
    r'\brun\b',
    r'\brvr\b',
    r'\bshl\b',
    r'\bshls\b',
    r'\bshoal\b',
    r'\bshoals\b',
    r'\bshoar\b',
    r'\bshoars\b',
    r'\bshore\b',
    r'\bshores\b',
    r'\bshr\b',
    r'\bshrs\b',
    r'\bskwy\b',
    r'\bskyway\b',
    r'\bsmt\b',
    r'\bspg\b',
    r'\bspgs\b',
    r'\bspng\b',
    r'\bspngs\b',
    r'\bspring\b',
    r'\bsprings\b',
    r'\bsprng\b',
    r'\bsprngs\b',
    r'\bspur\b',
    r'\bspurs\b',
    r'\bsq\b',
    r'\bsqr\b',
    r'\bsqre\b',
    r'\bsqrs\b',
    r'\bsqs\b',
    r'\bsqu\b',
    r'\bsquare\b',
    r'\bsquares\b',
    r'\bst\b',
    r'\bsta\b',
    r'\bstation\b',
    r'\bstatn\b',
    r'\bstn\b',
    r'\bstr\b',
    r'\bstra\b',
    r'\bstrav\b',
    r'\bstrave\b',
    r'\bstraven\b',
    r'\bstravenue\b',
    r'\bstravn\b',
    r'\bstream\b',
    r'\bstreet\b',
    r'\bstreets\b',
    r'\bstreme\b',
    r'\bstrm\b',
    r'\bstrt\b',
    r'\bstrvn\b',
    r'\bstrvnue\b',
    r'\bsts\b',
    r'\bsumit\b',
    r'\bsumitt\b',
    r'\bsummit\b',
    r'\bte\b',
    r'\bter\b',
    r'\bterr\b',
    r'\bterrace\b',
    r'\bthroughway\b',
    r'\btl\b',
    r'\btpk\b',
    r'\btpke\b',
    r'\btr\b',
    r'\btrace\b',
    r'\btraces\b',
    r'\btrack\b',
    r'\btracks\b',
    r'\btrafficway\b',
    r'\btrail\b',
    r'\btrailer\b',
    r'\btrails\b',
    r'\btrak\b',
    r'\btrce\b',
    r'\btrfy\b',
    r'\btrk\b',
    r'\btrks\b',
    r'\btrl\b',
    r'\btrlr\b',
    r'\btrlrs\b',
    r'\btrls\b',
    r'\btrnpk\b',
    r'\btrpk\b',
    r'\btrwy\b',
    r'\btunel\b',
    r'\btunl\b',
    r'\btunls\b',
    r'\btunnel\b',
    r'\btunnels\b',
    r'\btunnl\b',
    r'\bturn\b',
    r'\bturnpike\b',
    r'\bturnpk\b',
    r'\bun\b',
    r'\bunderpass\b',
    r'\bunion\b',
    r'\bunions\b',
    r'\buns\b',
    r'\bupas\b',
    r'\bvale\b',
    r'\bvalley\b',
    r'\bvalleys\b',
    r'\bvally\b',
    r'\bvdct\b',
    r'\bvia\b',
    r'\bviadct\b',
    r'\bviaduct\b',
    r'\bview\b',
    r'\bviews\b',
    r'\bvill\b',
    r'\bvillag\b',
    r'\bvillage\b',
    r'\bvillages\b',
    r'\bville\b',
    r'\bvillg\b',
    r'\bvilliage\b',
    r'\bvis\b',
    r'\bvist\b',
    r'\bvista\b',
    r'\bvl\b',
    r'\bvlg\b',
    r'\bvlgs\b',
    r'\bvlly\b',
    r'\bvly\b',
    r'\bvlys\b',
    r'\bvst\b',
    r'\bvsta\b',
    r'\bvw\b',
    r'\bvws\b',
    r'\bwalk\b',
    r'\bwalks\b',
    r'\bwall\b',
    r'\bway\b',
    r'\bways\b',
    r'\bwell\b',
    r'\bwells\b',
    r'\bwl\b',
    r'\bwls\b',
    r'\bwood\b',
    r'\bwoods\b',
    r'\bwy\b',
    r'\bxc\b',
    r'\bxg\b',
    r'\bxing\b',
    r'\bxrd\b',
    r'\bxrds\b'
]

helper['directions'] = [
    r'\bn\b',
    r'\bs\b',
    r'\be\b',
    r'\bw\b',
    r'\bne\b',
    r'\bnw\b',
    r'\bse\b',
    r'\bsw\b',
    r'\bnorth\b',
    r'\bsouth\b',
    r'\beast\b',
    r'\bwest\b',
    r'\bnortheast\b',
    r'\bnorthwest\b',
    r'\bsoutheast\b',
    r'\bsouthwest\b'
]
helper['phone'] = ['telephone',
                   'office',
                   'mobile',
                   'direct',
                   'phone',
                   'home',
                   'cell',
                   'call',
                   'work',
                   'away',
                   'tel',
                   'mob',
                   'ph',
                   't',
                   'p',
                   't',
                   'h']
helper['fax'] = ['fax', 'f']

helper['company'] = [r'\blp\b',
                     r'\bllp\b',
                     r'\bllc\b',
                     r'\blc\b',
                     r'\bco\b',
                     r'\binc\b',
                     r'\bcorp\b',
                     r'\bltd\b',
                     # r'\boffice\b',
                     r'\bservices\b',
                     r'\bschool\b',
                     r'\buniversity\b',
                     r'\bcollege\b',
                     r'\bfund\b',
                     r'\bfoundation\b',
                     r'\binstitute\b',
                     r'\bsociety\b',
                     r'\bunion\b',
                     r'\blimited\b',
                     r'\bclub\b']

helper['name'] = ["aaron", "adam", "adrian", "agnes", "alan", "albert",
                  "alberto", "alex", "alexander", "alfred", "alfredo", "alice",
                  "alicia", "allan", "allen", "allison", "alma", "alvin",
                  "amanda", "amber", "amy", "ana", "andre", "andrea", "andrew",
                  "andy", "angel", "angela", "anita", "ann", "anna", "anne",
                  "annette", "annie", "anthony", "antonio", "april", "arlene",
                  "armando", "arnold", "arthur", "ashley", "audrey", "barbara",
                  "barry", "beatrice", "becky", "ben", "benjamin", "bernard",
                  "bernice", "bertha", "bessie", "beth", "betty", "beverly",
                  "bill", "billie", "billy", "bob", "bobbie", "bobby", "bonnie",
                  "brad", "bradley", "brandon", "brandy", "brenda", "brent",
                  "brett", "brian", "brittany", "bruce", "bryan", "byron",
                  "calvin", "carl", "carla", "carlos", "carmen", "carol",
                  "carole", "caroline", "carolyn", "carrie", "casey",
                  "cassandra", "catherine", "cathy", "cecil", "chad",
                  "charlene", "charles", "charlie", "charlotte", "cheryl",
                  "chester", "chris", "christian", "christina", "christine",
                  "christopher", "christy", "cindy", "claire", "clara",
                  "clarence", "claude", "claudia", "clayton", "clifford",
                  "clifton", "clinton", "clyde", "cody", "colleen", "connie",
                  "constance", "corey", "cory", "courtney", "craig", "crystal",
                  "curtis", "cynthia", "daisy", "dale", "dan", "dana", "daniel",
                  "danielle", "danny", "darlene", "darrell", "darren", "darryl",
                  "daryl", "dave", "david", "dawn", "dean", "deanna", "debbie",
                  "deborah", "debra", "delores", "denise", "dennis", "derek",
                  "derrick", "diana", "diane", "dianne", "dolores", "don",
                  "donald", "donna", "dora", "doris", "dorothy", "douglas",
                  "duane", "dustin", "dwayne", "dwight", "earl", "eddie",
                  "edgar", "edith", "edna", "eduardo", "edward", "edwin",
                  "eileen", "elaine", "eleanor", "elizabeth", "ella", "ellen",
                  "elmer", "elsie", "emily", "emma", "enrique", "eric", "erica",
                  "erik", "erika", "erin", "ernest", "esther", "ethel"
                  "eugene",
                  "eva", "evelyn", "everett", "felicia", "felix", "fernando",
                  "florence", "floyd", "frances", "francis", "francisco",
                  "frank", "franklin", "fred", "freddie", "frederick",
                  "gabriel", "gail", "gary", "gene", "george", "georgia",
                  "gerald", "geraldine", "gertrude", "gilbert", "gina",
                  "gladys", "glen", "glenda", "glenn", "gloria", "gordon",
                  "grace", "greg", "gregory", "guy", "gwendolyn", "harold",
                  "harry", "harvey", "hazel", "heather", "hector", "heidi",
                  "helen", "henry", "herbert", "herman", "hilda", "holly",
                  "howard", "hugh", "ian", "ida", "irene", "irma", "isaac",
                  "ivan", "jack", "jackie", "jacob", "jacqueline", "jaime",
                  "james", "jamie", "jane", "janet", "janice", "jared", "jason",
                  "javier", "jay", "jean", "jeanette", "jeanne", "jeff",
                  "jeffery", "jeffrey", "jennie", "jennifer", "jenny",
                  "jeremy", "jerome", "jerry", "jesse", "jessica", "jessie",
                  "jesus", "jill", "jim", "jimmie", "jimmy", "jo", "joan",
                  "joann", "joanne", "joe", "joel", "joey", "john", "johnathan",
                  "johnnie",
                  "johnny", "jon", "jonathan", "jordan", "jorge", "jose",
                  "joseph", "josephine", "joshua", "joy", "joyce", "juan",
                  "juanita", "judith", "judy", "julia", "julian", "julie",
                  "julio", "june", "justin", "karen", "karl", "katherine",
                  "kathleen", "kathryn", "kathy", "katie", "katrina", "kay",
                  "keith", "kelly", "ken", "kenneth", "kent", "kevin", "kim",
                  "kimberly", "kirk", "kristen", "kristin", "kristina", "kurt",
                  "kyle", "lance", "larry", "laura", "lauren", "laurie",
                  "lawrence", "leah", "lee", "lena", "leo", "leon", "leona",
                  "leonard", "leroy", "leslie", "lester", "lewis", "lillian",
                  "lillie", "linda", "lisa", "lloyd", "lois", "lonnie",
                  "loretta", "lori", "lorraine", "louis", "louise", "lucille",
                  "lucy", "luis", "lydia", "lynn", "mabel", "mae", "manuel",
                  "marc", "marcia", "marcus", "margaret", "margie", "maria",
                  "marian", "marie", "marilyn", "mario", "marion", "marjorie",
                  "mark", "marlene", "marsha", "marshall", "martha", "martin",
                  "marvin", "mary", "mathew", "matthew", "mattie", "maureen",
                  "maurice", "max", "maxine", "megan", "melanie", "melinda",
                  "melissa", "melvin", "michael", "micheal", "michele",
                  "michelle", "miguel", "mike", "mildred", "milton",
                  "minnie", "miriam", "misty", "mitchell", "monica",
                  "morris", "myrtle", "nancy", "naomi", "natalie", "nathan",
                  "nathaniel", "neil", "nellie", "nelson", "nicholas",
                  "nicole", "nina", "nora", "norma", "norman", "olga",
                  "oscar", "pamela", "patricia", "patrick", "patsy",
                  "paul", "paula", "pauline", "pearl", "pedro", "peggy",
                  "penny", "perry", "peter", "philip", "phillip",
                  "phyllis", "priscilla", "rachel", "rafael", "ralph",
                  "ramon", "ramona", "randall", "randy", "raul", "ray",
                  "raymond", "rebecca", "regina", "reginald", "rene",
                  "renee", "rhonda", "ricardo", "richard", "rick",
                  "ricky", "rita", "robert", "roberta", "roberto",
                  "robin", "rodney", "roger", "roland", "ron", "ronald",
                  "ronnie", "rosa", "rose", "rosemary", "ross", "roy",
                  "ruben", "ruby", "russell", "ruth", "ryan", "sally",
                  "salvador", "sam", "samantha", "samuel", "sandra",
                  "sara", "sarah", "scott", "sean", "sergio", "seth",
                  "shane", "shannon", "sharon", "shawn", "sheila",
                  "shelly", "sherri", "sherry", "shirley", "sidney",
                  "sonia", "stacey", "stacy", "stanley", "stella",
                  "stephanie", "stephen", "steve", "steven", "sue",
                  "susan", "suzanne", "sylvia", "tamara", "tammy",
                  "tanya", "tara", "ted", "teresa", "terrance",
                  "terrence", "terri", "terry", "thelma", "theodore",
                  "theresa", "thomas", "tiffany", "tim", "timothy",
                  "tina", "todd", "tom", "tommy", "toni", "tony",
                  "tonya", "tracey", "tracy", "travis", "troy",
                  "tyler", "tyrone", "valerie", "vanessa", "velma",
                  "vera", "vernon", "veronica", "vicki", "vickie",
                  "victor", "victoria", "vincent", "viola", "violet",
                  "virgil", "virginia", "vivian", "wade", "wallace",
                  "walter", "wanda", "warren", "wayne", "wendy", "wesley",
                  "willard", "william", "willie", "wilma", "yolanda",
                  "yvonne", "zachary"]


# helper['city'] = [
#     ["Warrington", "United Kingdom", "Warrington"],
#     ["Newbury", "United Kingdom", "West Berkshire"],
#     ["Swindon", "United Kingdom", "Swindon"],
#     ["Wick", "United Kingdom", "Highland"],
#     ["Dudley", "United Kingdom", "Dudley"],
#     ["Oxford", "United Kingdom", "Oxfordshire"],
#     ["Hackney", "United Kingdom", "Hackney"],
#     ["Matlock", "United Kingdom", "Derbyshire"],
#     ["Lochgilphead", "United Kingdom", "Argyll and Bute"],
#     ["Northallerton", "United Kingdom", "North Yorkshire"],
#     ["Edinburgh", "United Kingdom", "Edinburgh, City of"],
#     ["Sunderland", "United Kingdom", "Sunderland"],
#     ["Swansea", "United Kingdom", "Swansea"],
#     ["Wokingham", "United Kingdom", "Wokingham"],
#     ["City of Westminster", "United Kingdom", "Westminster"],
#     ["Solihull", "United Kingdom", "Solihull"],
#     ["Rochdale", "United Kingdom", "Rochdale"],
#     ["Nottingham", "United Kingdom", "Nottingham"],
#     ["Winchester", "United Kingdom", "Hampshire"],
#     ["Wembley", "United Kingdom", "Brent"],
#     ["Motherwell", "United Kingdom", "North Lanarkshire"],
#     ["Reading", "United Kingdom", "Reading"],
#     ["Torquay", "United Kingdom", "Torbay"],
#     ["Thornbury", "United Kingdom", "South Gloucestershire"],
#     ["Oldham", "United Kingdom", "Oldham"],
#     ["Elgin", "United Kingdom", "Moray"],
#     ["Wallsend", "United Kingdom", "North Tyneside"],
#     ["Weston-super-Mare", "United Kingdom", "North Somerset"],
#     ["Hounslow", "United Kingdom", "Hounslow"],
#     ["Irvine", "United Kingdom", "North Ayrshire"],
#     ["Barnsley", "United Kingdom", "Barnsley"],
#     ["Falkirk", "United Kingdom", "Falkirk"],
#     ["Slough", "United Kingdom", "Slough"],
#     ["Huddersfield", "United Kingdom", "Kirklees"],
#     ["Kingston upon Hull", "United Kingdom", "Kingston upon Hull, City of"],
#     ["Romford", "United Kingdom", "Havering"],
#     ["Stafford", "United Kingdom", "St. Helens"],
#     ["Grays", "United Kingdom", "Thurrock"],
#     ["Hertford", "United Kingdom", "Hertfordshire"],
#     ["Coventry", "United Kingdom", "Coventry"],
#     ["Leicester", "United Kingdom", "Leicester"],
#     ["Beverley", "United Kingdom", "East Riding of Yorkshire"],
#     ["Stirling", "United Kingdom", "Stirling"],
#     ["Norwich", "United Kingdom", "Norfolk"],
#     ["Darlington", "United Kingdom", "Darlington"],
#     ["Hereford", "United Kingdom", "Herefordshire"],
#     ["Grimsby", "United Kingdom", "North East Lincolnshire"],
#     ["Bradford", "United Kingdom", "Bradford"],
#     ["Bracknell", "United Kingdom", "Bracknell Forest"],
#     ["Morpeth", "United Kingdom", "Northumberland"],
#     ["Gateshead", "United Kingdom", "Gateshead"],
#     ["Wandsworth", "United Kingdom", "Wandsworth"],
#     ["South Shields", "United Kingdom", "South Tyneside"],
#     ["Sheffield", "United Kingdom", "Sheffield"],
#     ["Ystrad Mynach", "United Kingdom", "Caerphilly"],
#     ["South Bank", "United Kingdom", "Redcar and Cleveland"],
#     ["Haddington", "United Kingdom", "East Lothian"],
#     ["Aberaeron", "United Kingdom", "Ceredigion"],
#     ["Lerwick", "United Kingdom", "Shetland Islands"],
#     ["Cambridge", "United Kingdom", "Cambridgeshire"],
#     ["Glenrothes", "United Kingdom", "Fife"],
#     ["Pen-y-Bont ar Ogwr", "United Kingdom", "Bridgend"],
#     ["Barri", "United Kingdom", "Vale of Glamorgan, The"],
#     ["Carlisle", "United Kingdom", "Cumbria"],
#     ["Aylesbury", "United Kingdom", "Buckinghamshire"],
#     ["Lincoln", "United Kingdom", "Lincolnshire"],
#     ["Bromley", "United Kingdom", "Bromley"],
#     ["Kirkwall", "United Kingdom", "Orkney Islands"],
#     ["Blackpool", "United Kingdom", "Blackpool"],
#     ["Croydon", "United Kingdom", "Croydon"],
#     ["Dorchester", "United Kingdom", "Dorset"],
#     ["Hendon", "United Kingdom", "Barnet"],
#     ["Hammersmith", "United Kingdom", "Hammersmith and Fulham"],
#     ["Bournemouth", "United Kingdom", "Bournemouth"],
#     ["Fort William", "United Kingdom", "Highland"],
#     ["Dumfries", "United Kingdom", "Dumfries and Galloway"],
#     ["Dumbarton", "United Kingdom", "West Dunbartonshire"],
#     ["Luton", "United Kingdom", "Luton"],
#     ["Bristol", "United Kingdom", "Bristol, City of"],
#     ["Enfield", "United Kingdom", "Enfield"],
#     ["Camberwell", "United Kingdom", "Southwark"],
#     ["Truro", "United Kingdom", "Cornwall"],
#     ["Penzance", "United Kingdom", "Cornwall"],
#     ["Clydach Vale", "United Kingdom", "Rhondda Cynon Taff"],
#     ["Telford", "United Kingdom", "Telford and Wrekin"],
#     ["Stockton-on-Tees", "United Kingdom", "Stockton-on-Tees"],
#     ["Maidenhead", "United Kingdom", "Windsor and Maidenhead"],
#     ["Dalkeith", "United Kingdom", "Midlothian"],
#     ["Wood Green", "United Kingdom", "Haringey"],
#     ["Pont-y-pŵl", "United Kingdom", "Torfaen"],
#     ["Perth", "United Kingdom", "Perth and Kinross"],
#     ["Milton Keynes", "United Kingdom", "Milton Keynes"],
#     ["Hartlepool", "United Kingdom", "Hartlepool"],
#     ["Harrow", "United Kingdom", "Harrow"],
#     ["Oldbury", "United Kingdom", "Sandwell"],
#     ["Ashton-under-Lyne", "United Kingdom", "Tameside"],
#     ["Wakefield", "United Kingdom", "Wakefield"],
#     ["Trowbridge", "United Kingdom", "Wiltshire"],
#     ["Maidstone", "United Kingdom", "Kent"],
#     ["Poole", "United Kingdom", "Poole"],
#     ["Newport", "United Kingdom", "Isle of Wight"],
#     ["Walsall", "United Kingdom", "Walsall"],
#     ["Woolwich", "United Kingdom", "Greenwich"],
#     ["Southend-on-Sea", "United Kingdom", "Southend-on-Sea"],
#     ["Scunthorpe", "United Kingdom", "North Lincolnshire"],
#     ["Caernarfon", "United Kingdom", "Gwynedd"],
#     ["Hamilton", "United Kingdom", "South Lanarkshire"],
#     ["Durham", "United Kingdom", "Durham"],
#     ["Warwick", "United Kingdom", "Warwickshire"],
#     ["Aberdeen", "United Kingdom", "Aberdeen City"],
#     ["Newtown Saint Boswells", "United Kingdom", "Scottish Borders, The"],
#     ["Sutton", "United Kingdom", "Sutton"],
#     ["Catford", "United Kingdom", "Lewisham"],
#     ["Lambeth", "United Kingdom", "Lambeth"],
#     ["Lewes", "United Kingdom", "East Sussex"],
#     ["Dundee", "United Kingdom", "Dundee City"],
#     ["Ipswich", "United Kingdom", "Suffolk"],
#     ["Birmingham", "United Kingdom", "Birmingham"],
#     ["Stoke", "United Kingdom", "Stoke-on-Trent"],
#     ["Stockport", "United Kingdom", "Stockport"],
#     ["Chelmsford", "United Kingdom", "Essex"],
#     ["Leeds", "United Kingdom", "Leeds"],
#     ["Bath", "United Kingdom", "Bath and North East Somerset"],
#     ["Ayr", "United Kingdom", "South Ayrshire"],
#     ["Kirkintilloch", "United Kingdom", "East Dunbartonshire"],
#     ["Wallasey", "United Kingdom", "Wirral"],
#     ["Conwy", "United Kingdom", "Conwy"],
#     ["Rhuthun", "United Kingdom", "Denbighshire"],
#     ["Walthamstow", "United Kingdom", "Waltham Forest"],
#     ["Halifax", "United Kingdom", "Calderdale"],
#     ["Peterborough", "United Kingdom", "Peterborough"],
#     ["Rotherham", "United Kingdom", "Rotherham"],
#     ["Alloa", "United Kingdom", "Clackmannanshire"],
#     ["Southampton", "United Kingdom", "Southampton"],
#     ["Ebbw Vale", "United Kingdom", "Blaenau Gwent"],
#     ["Forfar", "United Kingdom", "Angus"],
#     ["Islington", "United Kingdom", "Islington"],
#     ["Caerfyrddin", "United Kingdom", "Carmarthenshire"],
#     ["Ealing", "United Kingdom", "Ealing"],
#     ["Kilmarnock", "United Kingdom", "East Ayrshire"],
#     ["Newport", "United Kingdom", "Newport"],
#     ["Kensington", "United Kingdom", "Kensington and Chelsea"],
#     ["Hwlffordd", "United Kingdom", "Pembrokeshire"],
#     ["Uxbridge", "United Kingdom", "Hillingdon"],
#     ["Twickenham", "United Kingdom", "Richmond upon Thames"],
#     ["Plymouth", "United Kingdom", "Plymouth"],
#     ["Livingston", "United Kingdom", "West Lothian"],
#     ["Portsmouth", "United Kingdom", "Portsmouth"],
#     ["Paisley", "United Kingdom", "Renfrewshire"],
#     ["Exeter", "United Kingdom", "Devon"],
#     ["Widnes", "United Kingdom", "Halton"],
#     ["Stretford", "United Kingdom", "Trafford"],
#     ["Stornoway", "United Kingdom", "Eilean Siar"],
#     ["Manchester", "United Kingdom", "Manchester"],
#     ["Inverness", "United Kingdom", "Highland"],
#     ["Morden", "United Kingdom", "Merton"],
#     ["London", "United Kingdom"],
#     ["Ilford", "United Kingdom", "Redbridge"],
#     ["Poplar", "United Kingdom", "Tower Hamlets"],
#     ["Salford", "United Kingdom", "Salford"],
#     ["Derby", "United Kingdom", "Derby"],
#     ["Mold", "United Kingdom", "Flintshire"],
#     ["Worcester", "United Kingdom", "Worcestershire"],
#     ["Rochester", "United Kingdom", "Medway"],
#     ["Chichester", "United Kingdom", "West Sussex"],
#     ["East Ham", "United Kingdom", "Newham"],
#     ["Oakham", "United Kingdom", "Rutland"],
#     ["Gloucester", "United Kingdom", "Gloucestershire"],
#     ["Wrecsam", "United Kingdom", "Wrexham"],
#     ["Wolverhampton", "United Kingdom", "Wolverhampton"],
#     ["Llangefni", "United Kingdom", "Isle of Anglesey"],
#     ["Hove", "United Kingdom", "Brighton and Hove"],
#     ["Brighton", "United Kingdom", "Brighton and Hove"],
#     ["Doncaster", "United Kingdom", "Doncaster"],
#     ["Shrewsbury", "United Kingdom", "Shropshire"],
#     ["Glasgow", "United Kingdom", "Glasgow City"],
#     ["Camden Town", "United Kingdom", "Camden"],
#     ["Cardiff", "United Kingdom", "Cardiff"],
#     ["Bexleyheath", "United Kingdom", "Bexley"],
#     ["Dover", "United Kingdom", "Kent"],
#     ["Bury", "United Kingdom", "Bury"],
#     ["Greenock", "United Kingdom", "Inverclyde"],
#     ["Middlesbrough", "United Kingdom", "Redcar and Cleveland"],
#     ["Scarborough", "United Kingdom", "North Yorkshire"],
#     ["Merthyr Tudful", "United Kingdom", "Merthyr Tydfil"],
#     ["Taunton", "United Kingdom", "Somerset"],
#     ["York", "United Kingdom", "York"],
#     ["Port Talbot", "United Kingdom", "Neath Port Talbot"],
#     ["Dagenham", "United Kingdom", "Barking and Dagenham"],
#     ["Liverpool", "United Kingdom", "Liverpool"],
#     ["Saint Helens", "United Kingdom", "St. Helens"],
#     ["Knowsley", "United Kingdom", "Knowsley"],
#     ["Kingston upon Thames", "United Kingdom", "Kingston upon Thames"],
#     ["Wigan", "United Kingdom", "Wigan"],
#     ["Southport", "United Kingdom", "Sefton"],
#     ["Preston", "United Kingdom", "Lancashire"],
#     ["Blackburn", "United Kingdom", "Blackburn with Darwen"],
#     ["Bolton", "United Kingdom", "Bolton"],
#     ["Hugh Town", "United Kingdom", "Isles of Scilly"],
#     ["Bedford", "United Kingdom", "Bedford"],
#     ["Chicksands", "United Kingdom", "Central Bedfordshire"],
#     ["Sandbach", "United Kingdom", "Cheshire East"],
#     ["Chester", "United Kingdom", "Cheshire West and Chester"],
#     ["Llandrindod Wells", "United Kingdom", "Powys"],
#     ["Northampton", "United Kingdom", "Northamptonshire"],
#     ["Giffnock", "United Kingdom", "East Renfrewshire"],
#     ["Newcastle", "United Kingdom", "Newcastle upon Tyne"],
#     ["Downpatrick", "United Kingdom", "Newry, Mourne and Down"],
#     ["Coleraine", "United Kingdom", "Causeway Coast and Glens"],
#     ["Magherafelt", "United Kingdom", "Mid Ulster"],
#     ["Dungannon", "United Kingdom", "Mid Ulster"],
#     ["Cookstown", "United Kingdom", "Mid Ulster"],
#     ["Bangor", "United Kingdom", "Ards and North Down"],
#     ["Strabane", "United Kingdom", "Derry and Strabane"],
#     ["Londonderry", "United Kingdom", "Derry and Strabane"],
#     ["Omagh", "United Kingdom", "Fermanagh and Omagh"],
#     ["Enniskillen", "United Kingdom", "Fermanagh and Omagh"],
#     ["Ballymena", "United Kingdom", "Mid and East Antrim"],
#     ["Banbridge", "United Kingdom", "Armagh, Banbridge and Craigavon"],
#     ["Armagh", "United Kingdom", "Armagh, Banbridge and Craigavon"],
#     ["Newtownabbey", "United Kingdom", "Antrim and Newtownabbey"],
#     ["Craigavon", "United Kingdom", "Armagh, Banbridge and Craigavon"],
#     ["Antrim", "United Kingdom", "Antrim and Newtownabbey"],
#     ["Newry", "United Kingdom", "Newry, Mourne and Down"],
#     ["Lisburn", "United Kingdom", "Lisburn and Castlereagh"],
#     ["Belfast", "United Kingdom", "Belfast"],
#     ["Belfast", "United Kingdom", "Belfast"],
#     ["Usk", "United Kingdom", "Monmouthshire"]]
