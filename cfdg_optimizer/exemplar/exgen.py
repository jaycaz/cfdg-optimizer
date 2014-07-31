# Jordan Cazamias
# CFDG Optimizer
# June 2014

# exgen.py: Exemplar Generation

import subprocess as proc
from PIL.ImageFile import Parser

from cfdg_optimizer.grammar.gramparse import clean_body
from cfdg_optimizer.exemplar import Exemplar


MAX_SHAPES = 1000000


def generate_exemplar(grammar, **kwargs):
    """
    Using CFDG, creates an exemplar from the provided grammar,
    retrieves the image data, and returns the image data

    Available kwargs:
    'maxshapes': maximum number of shapes
    'width': width, in pixels, of image
    'height': height, in pixels, of image

    :return: Exemplar instance
    """
    commandstr = "cfdg"

    # process keyword arguments
    if 'maxshapes' in kwargs:
        commandstr += " -m {0}".format(kwargs['maxshapes'])
    else:
        commandstr += " -m {0}".format(MAX_SHAPES)

    if 'width' in kwargs:
        commandstr += " -w {0}".format(kwargs['width'])
    if 'height' in kwargs:
        commandstr += " -h {0}".format(kwargs['height'])

    commandstr += " -" # specifies to cfdg that grammar file will come from stdin

    # run cfdg, passing in grammar.body as the input
    try:
        cfdg_proccess = proc.Popen(commandstr, shell=True,
                                   stdin=proc.PIPE, stdout=proc.PIPE)
        comm = cfdg_proccess.communicate(input=clean_body(grammar))
        cfdg_output = comm[0]
        if cfdg_output == '':
            raise Exception("CFDG output is empty.")
    except Exception as e:
        print("Error using CFDG to parse grammar '{0}'".format(grammar.name))
        raise e

    # parse output of cfdg into an image file, ready to save
    try:
        p = Parser()
        p.feed(cfdg_output)
        image = p.close()
    except IOError as e:
        print("Error parsing CFDG output for grammar '{0}' into an image file".format(grammar.name))
        raise e

    ex = Exemplar(image=image)
    return ex


def generate_exemplars(grammar, numexemplars, debug=False, **kwargs):
    """
    Convenience function to create many different exemplars
    from one grammar at once

    :param debug: if true, prints debug information

    :return: List of Exemplar instances
    """
    exemplars = []

    for i in range(numexemplars):
        try:
            img = generate_exemplar(grammar, **kwargs)
            exemplars.append(img)
            if debug:
                print "Created exemplar {0} of {1}".format(i+1, numexemplars)
        except Exception as e:
            print "Error creating exemplar number {0} in n_generate_exemplars".format(i)
            raise e

    return exemplars


