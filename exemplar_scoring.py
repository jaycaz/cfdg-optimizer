# Jordan Cazamias
# CFDG Optimizer
# June 2014

# exemplar_scoring.py: functionality for scoring exemplars

import os

from PIL import Image

import image_compare

# Returns compiled score by comparing exemplar
# to all images in test_img_dir
# Currently, compiled score is simply the mean score
def score_exemplar(exemplar, test_image_dir):
    individual_scores = []

    try:
        testfiles = os.listdir(test_image_dir)
    except OSError as e:
        print "Error: directory '{0}' could not be opened.".format(
            test_image_dir)
        raise e

    for filename in testfiles:
        try:
            test_image = Image.open("{0}/{1}".format(
                test_image_dir.rstrip('/'), filename))
        except IOError:
            continue

        image_score = image_compare.compare(exemplar.image, test_image)
        individual_scores.append(image_score)

    if not individual_scores:
        raise Exception("ERROR: no files in {0} could be opened as images"
                        .format(test_image_dir))

    compiled_score = sum(individual_scores) / len(individual_scores)
    return compiled_score

# Given a list of scores for a grammar variant, calculates
# the overall score for the variant.
# Currently, compiled score is simply the mean score
def compile_scores(scores):
    compiled_score = sum(scores) / len(scores)
    return compiled_score
