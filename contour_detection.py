"""Script to extract biggest contour in the image
"""
import cv2
import numpy as np
import imutils


def get_biggest_contour(img, edge_detection=True):
    """gets the biggest contour given the processed image

    Args:
        img : the processed image
        edge_detection (bool, optional): Whether to do edge detection

    Returns:
        contour points of the biggest contour
    """
    if edge_detection:
        img = cv2.Canny(img, 30, 200)
    cnts = cv2.findContours(img.copy(), cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # assuming logo is the second biggest contour in the image
    # the first being the whole card itself
    biggest_contour = sorted(cnts, key=cv2.contourArea, reverse=True)[1]
    return biggest_contour


def extract_biggest_contour(image):
    """Takes an image and processes it with various techniques and returns the
    biggest detected contour

    Args:
        image: Image

    Returns:
        contour points of the biggest contour and a mask of the contour region
    """
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(grey, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    cnts = []
    cnts.append(get_biggest_contour(image))
    cnts.append(get_biggest_contour(grey))
    cnts.append(get_biggest_contour(thresh, False))

    biggest_contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    mask = np.zeros(image.shape[:2] + (1,), np.uint8)
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
    mask = np.dstack([mask] * 3)

    return biggest_contour, mask
