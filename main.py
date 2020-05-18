"""Runs the Entity extaction modules. It first runs the text extraction model
and uses the results(line by line) to do OCR and then using the OCR it runs the
entity extraction model. It also runs the logo detection model.

Attributes:
    args : contains command line arguments
    BBOX_RESULT_PREFIX (str): string prefix for identifying BBOX text files
    bboxes_filenames (list): list containing BBOX filenames
    THRESHOLD (bool): Whether to apply thresholding to the input image
    BINARY_THREHOLD (int): value used for thresholding grayscale image
    files (list): list containing image filepaths
    GRAYSCALE (bool): Whether to grayscale the image before doing OCR
    input_images_path (str): dir storing the input images. NOTE: the image files
                             given by the user are moved to this folder before
                             running the text extraction model. The folder is
                             also emptied(all contents are deleted) before each
                             run
    padding (float): a small amount of space added to the bbox to aid OCR model
    parser (argparse.ArgumentParser): ArgumentParser object
    results_path (str): Dir to store results. Here the results of text detection
                        model, the final result(json) are stored. NOTE:  The
                        folder is also emptied(all contents are deleted) before
                        each run

"""
import cv2
import os
import pytesseract
import argparse

import json
import shutil

from analyze_OCR import analyze_OCR
from contour_detection import extract_biggest_contour


parser = argparse.ArgumentParser()

parser.add_argument('--imgs', required=True,
                    help='a high quality imag of the visiting card or \
                        a directory containing images of high quality images of\
                        visiting cards in jpg or png format')
args = parser.parse_args()


input_images_path = 'input_images/'
results_path = 'results/'


padding = 0.01
BINARY_THREHOLD = 180
GRAYSCALE = True
THRESHOLD = True

BBOX_RESULT_PREFIX = 'res_'


SHOW_PARSE = True


def save_json(data, path):
    """Save the dict as a json file

    Args:
        data (dict): dictionary containing the data
        path (str): full path where the data will be saved
    """
    with open(path, 'w') as fp:
        json.dump(data, fp)


def read_text_file(filename):
    """Reads the text file containing bbox coordinates

    Args:
        filename (str): path of the text file to read

    Returns:
        list: list contaning bbox coordinates
    """
    with open(filename) as f:
        bboxes = [tuple(map(int, l.strip('\n').split(',')))
                  for l in f.readlines()]
    return bboxes


def run_text_extraction(img_files):
    """Runs the text extraction model given the image file paths

    Args:
        img_files (list): list containing the img paths
    """
    # clear contents of input_images_path if it exists and delete the folder
    if os.path.exists(input_images_path):
        shutil.rmtree(input_images_path)
    # create the folder to store input_images
    os.makedirs(input_images_path)

    # copy imgs to input_images dir
    for file_path in img_files:
        if file_path.endswith(".jpg") or file_path.endswith(".png"):
            src_dir = file_path
            dst_dir = input_images_path
            shutil.copy(src_dir, dst_dir)

    # change folder to text_detection_model to run text detection model
    os.chdir('./text-detection-model/')
    os.system('python ctpn/demo_pb.py')
    os.chdir('../')


if __name__ == "__main__":

    if os.path.isdir(args.imgs):
        folder = args.imgs
        files = [os.path.join(folder, filename)
                 for filename in os.listdir(folder)]
        bboxes_filenames = [os.path.join(
            results_path,
            BBOX_RESULT_PREFIX + filename.split('.')[0] + '.txt')
            for filename in os.listdir(folder)]
    elif os.path.isfile(args.imgs):
        files = [args.imgs]
        file_name_without_ext = files[0].split('/')[-1].split('.')[0]
        bboxes_filenames = [os.path.join(
            results_path,
            BBOX_RESULT_PREFIX + file_name_without_ext + '.txt')
            for filename in files]
    else:
        print('The entered path is neither a folder nor a file')
        exit()

    # clear contents of results_path if it exists and delete the folder
    if os.path.exists(results_path):
        shutil.rmtree(results_path)
    # create the folder to store results
    os.makedirs(results_path)

    run_text_extraction(files)

    files = sorted(files)
    bboxes_filenames = sorted(bboxes_filenames)

    for file, bboxes_filename in zip(files, bboxes_filenames):

        file_name_without_ext = file[:-4].split('/')[-1]

        color_img = cv2.imread(file)
        img = color_img.copy()
        # color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

        if GRAYSCALE:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if THRESHOLD:
            img = cv2.threshold(img, 0, 255,
                                cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        _, mask = extract_biggest_contour(color_img)
        if mask != []:
            idx = (mask != 0)
            color_img[~idx] = 255
            cv2.imwrite(os.path.join(results_path, "logo_" +
                                     file_name_without_ext + ".png"), color_img)

        height, width = img.shape[:2]
        results = []
        emails = []
        phones = []
        websites = []
        addresses = []
        bboxes = read_text_file(bboxes_filename)

        for bbox in bboxes:
            x1, y1, x2, y2 = bbox

            # in order to obtain a better OCR of the text we can potentially
            # apply a bit of padding surrounding the bounding box -- here we
            # are computing the deltas in both the x and y directions
            dX = int((x2 - x1) * padding)
            dY = int((y2 - y1) * padding)
            # img = rotate_if_necessary(img)

            # apply padding to each side of the bounding box, respectively
            x1 = max(0, x1 - dX)
            y1 = max(0, y1 - dY)
            x2 = min(width, x2 + (dX))
            y2 = min(height, y2 + (dY))

            orig = img.copy()
            roi = orig[y1:y2, x1:x2]
            if THRESHOLD:
                roi = cv2.threshold(roi, 0, 255,
                                    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            # in order to apply Tesseract v4 to OCR text we must supply
            # (1) a language, (2) an OEM flag of 4, indicating that the we
            # wish to use the LSTM neural net model for OCR, and finally
            # (3) an OEM value, in this case, 7 which implies that we are
            # treating the ROI as a single line of text
            config = (
                "-l eng --psm 7 -c tosp_min_sane_kn_sp=2.8")
            text = pytesseract.image_to_string(roi, config=config)
            if not text:
                continue

            # add the bounding box coordinates and OCR'd text to the list
            # of results
            results.append(((x1, y1, x2, y2), text))

        if results == []:
            print('No results found')
            print('Please recheck the image and make sure it has right \
                orientation, high quality and also text to extract')
            exit()
        # sort the results bounding box coordinates from top to bottom
        results = sorted(results, key=lambda r: r[0][1])
        print('\nResults for ', file_name_without_ext, ' are: \n')
        results = analyze_OCR(results, silent=False)
        save_json(results, os.path.join(results_path,
                                        'final_results_' +
                                        file_name_without_ext + '.json'))
