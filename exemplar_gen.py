# Jordan Cazamias
# CFDG Optimizer
# June 2014
from reportlab.platypus.para import Para

import subprocess as proc
import save_utils as save
from ImageFile import Parser

MAX_SHAPES = 1000000
COMMAND_STR = "cfdg"

# Using CFDG, creates an exemplar from the provided grammar,
# retrieves the image data, and returns the image data
#
# Available kwargs:
# 'maxshapes': maximum number of shapes
# 'width': width, in pixels, of image
# 'height': height, in pixels, of image
def generate_exemplar(grammar, **kwargs):
    commandargs = "-" # specifies to cfdg that grammar file will come from stdin

    # process keyword arguments
    if 'maxshapes' in kwargs:
        commandargs += " -m {0}".format(kwargs['maxshapes'])
    if 'width' in kwargs:
        commandargs += " -w {0}".format(kwargs['width'])
    if 'height' in kwargs:
        commandargs += " -h {0}".format(kwargs['height'])

    # run cfdg, passing in grammar.body as the input
    try:
        cfdg_proccess = proc.Popen([COMMAND_STR, commandargs], stdin=proc.PIPE, stdout=proc.PIPE)
        comm = cfdg_proccess.communicate(input=grammar.body)
        cfdg_output = comm[0]
    except Exception as e:
        print("Error using CFDG to parse grammar '{0}'".format(grammar.name))
        raise e

    # parse output of cfdg into an image file, ready to save
    try:
        p = Parser()
        p.feed(cfdg_output)
        img = p.close()
    except IOError as e:
        print("Error parsing CFDG output for grammar '{0}' into an image file".format(grammar.name))
        raise e

    return img

# Convenience function to create many different exemplars
# from one grammar at once
#
# debug: if true, prints debug information
def generate_exemplars(grammar, numexemplars, debug=False, **kwargs):
    images = []

    for i in range(numexemplars):
        try:
            img = generate_exemplar(grammar, **kwargs)
            images.append(img)
            if debug:
                print "Created exemplar {0} of {1}".format(i+1, numexemplars)
        except Exception as e:
            print "Error creating exemplar number {0} in n_generate_exemplars".format(i)
            raise e

    return images


