# Jordan Cazamias
# CFDG Optimizer
# July 2014

import ssim
from PIL import Image

MIN_VALUE = -1.0
MAX_VALUE = 1.0


# Blackbox comparison function to perform PIL
# Image comparison in the rest of the module
def compare(img1, img2, **kwargs):
    # Optional keyword arguments:
    # - gaussian_kernel_width
    # - gaussian_kernel_sigma

    score = ssim.compute_ssim(img1, img2, **kwargs)

    return score


def compare_from_file(imgfilename1, imgfilename2, **kwargs):

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

