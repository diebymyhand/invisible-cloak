import cv2 as cv
import numpy as np


def create_mask(frame, lower_boundary, upper_boundary):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_boundary, upper_boundary)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    mask = cv.dilate(mask, kernel, iterations=1)

    return mask


def apply_cloak_effect(frame, background, mask):
    mask_inv = cv.bitwise_not(mask)

    bg_part = cv.bitwise_and(background, background, mask=mask)
    fg_part = cv.bitwise_and(frame, frame, mask=mask_inv)

    return cv.add(bg_part, fg_part)