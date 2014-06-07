# Jordan Cazamias
# CFDG Optimizer
# April 2014

import os.path
import Image
from pycurl import IOE_FAILRESTART
import sys


# Starting with <rootpath>, finds an appropriate digit to append
# to avoid a file collision
def first_available_filename(rootpath):
    if not os.path.isfile(rootpath):
        return rootpath

    if rootpath[-5:] == ".cfdg":
        strippath = rootpath[0:-5]
    else:
        strippath = rootpath
    i = 1
    while 1:
        filename = "{0}-{1}.cfdg".format(strippath, i)
        if not os.path.isfile(filename):
            return filename
        i += 1


# Writes out grammar contents to new file <outfilename>
# If <override> is true, it will write to <outfilename> without question
# If <override> is false, it will search for the first available filename
#    using first_available_filename
def save_grammar(grammar, outfilename, override=False):
    if override:
        usefilename = outfilename
    else:
        usefilename = first_available_filename(outfilename)

    try:
        f = open(usefilename, 'w')
        f.write(grammar.body)
        f.close()
    except IOError as e:
        print "Error saving grammar '{0}' to {1}".format(
            grammar.name, usefilename)
        raise e


# Writes out exemplar to an image file <outfilename>
# If <override> is true, it will write to <outfilename> without question
# If <override> is false, it will search for the first available filename
#    using first_available_filename
def save_exemplar(image, outfilename, override=False):
    if override:
        usefilename = outfilename
    else:
        usefilename = first_available_filename(outfilename)


    try:
        image.save(usefilename)
    except IOError as e:
        print "IOError saving image to {0}".format(usefilename)
        raise e
    except Exception as e:
        print "Some non-io error occurred saving image to {0}:" \
              " perhaps image arg is incorrect".format(usefilename)
        raise e


