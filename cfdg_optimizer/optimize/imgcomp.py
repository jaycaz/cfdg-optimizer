# Jordan Cazamias
# CFDG Optimizer
# July 2014

# imgcomp.py: Image comparison

import copy
import sys

import ssim
from PIL import Image
from cfdg_optimizer.utils.imgcomputils.imgcmp import *

MIN_VALUE = -1.0
MAX_VALUE = 1.0


def compare(img1, img2, **kwargs):
    """
    General image comparison function. Currently, SSIM is used as
    the comparison algorithm.

    :param img1, img2: PIL Images
    :keyword gaussian_kernel_width:
    :keyword gaussian_kernel_sigma:

    return: Image comparison score. Currently a double in range [-1.0, 1.0]
    """

    # Optional keyword arguments:

    # score = ssim.compute_ssim(img1, img2, **kwargs)
    cmp = FuzzyImageCompare(img1, img2)
    print cmp.compare()
    score = cmp.similarity()

    return score


def compare_from_file(imgfilename1, imgfilename2, **kwargs):
    """
    Create PIL Images from two image files and compare

    :param imgfilename1, imgfilename2: Image files to be parsed and compared
    :param kwargs: See compare for optional keywords
    :return: See compare for return value
    """

    try:
        img1 = Image.open(imgfilename1)
    except IOError as e:
        print "Error: Could not open image file '{0}'".format(imgfilename1)
        raise e

    try:
        img2 = Image.open(imgfilename2)
    except IOError as e:
        print "Error: Could not open image file '{0}'".format(imgfilename2)
        raise e

    return compare(img1, img2, **kwargs)

