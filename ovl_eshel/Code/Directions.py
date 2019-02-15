# Copyright 2018 Ori Ben-Moshe - All rights reserved.
from numpy import ndarray
from . import Geometry
from sys import version_info


if version_info[0] == 3:
    xrange = range


def validate(contour, target_amount):
    if contour is None:
        return False
    elif contour is []:
        return False
    elif type(contour) is ndarray and target_amount > 1:
       return False
#    elif type(contour) is list and len(contour) < target_amount:
#        return False
    elif type(contour) is list and len(contour) == 0:
        return False
    else:
        return True


def alert_directions(contour, target_amount, img_size=(320, 240)):
    width, height = img_size
    if validate(contour, target_amount):
        return '1'
    else:
        return '0'
    

def xy_center_directions(contour, target_amount, img_size=(320, 240), invert=False):
    width, height = img_size
    x_ratio = 2000 / width
    y_ratio = 2000 / height
    if not validate(contour, target_amount):
        return False
    if type(contour) is ndarray:
        contour = [contour]
    x_sum = 0
    y_sum = 0
    for currentContour in contour:
        x, y = Geometry.get_contour_center(currentContour)
        x_sum += x
        y_sum += y
    x_res = x_sum / len(contour)
    y_res = y_sum / len(contour)
    x_res *= x_ratio
    y_res *= y_ratio
    if invert:
        return str(2000 - x_res) + str(2000 - y_res)
    return str(x_res) + ' ' + str(y_res)


def y_center_directions(contour, target_amount, img_size=(320, 240), invert=False):
    _, height = img_size
    y_ratio = 2000 / height
    if not validate(contour, target_amount):
        return False
    if type(contour) is ndarray:
        contour = [contour]
    y_sum = 0
    for currentContour in contour:
        x, y = Geometry.get_contour_center(currentContour)
        y_sum += y
    y_res = y_sum / len(contour)
    if invert:
        return 2000 - (y_res * y_ratio)
    return y_res * y_ratio


def x_center_directions(contour, target_amount, img_size=(320, 240), invert=False):
    width, _ = img_size
    x_ratio = 2000 / width
    if not validate(contour, target_amount):
        return False
    if type(contour) is ndarray:
        contour = [contour]
    x_sum = 0
    for currentContour in contour:
        x, y = Geometry.get_contour_center(currentContour)
        x_sum += x
    x_res = x_sum / len(contour)
    if invert:
        return 2000 - (x_res * x_ratio)
    return x_res * x_ratio



