# Jordan Cazamias
# CFDG Optimizer
# April 2014

import os.path


# Starting with <rootpath>, finds an appropriate digit to append
# to avoid a filename collision
def first_available_filename(tryname):
    if not os.path.isfile(tryname):
        return tryname

    filepath, extension = os.path.splitext(tryname)

    # Check if file already has a number appended
    i = 1
    dashindex = filepath.rfind('-')
    if dashindex != -1:
        if dashindex != len(filepath) - 1 and filepath[dashindex+1:].isdigit():
            i = int(filepath[dashindex+1:])
            filepath = filepath[:dashindex]

    while True:
        filename = "{0}-{1}{2}".format(filepath, i, extension)
        if not os.path.isfile(filename):
            return filename
        i += 1


# Tries to write out grammar contents to new file <tryfilename>
# and returns actual file name used
#
# If <override> is true, it will write to <tryfilename> without question
# If <override> is false, it will search for the first available filename
# using first_available_filename
def save_grammar(grammar, tryfilename, override=False):
    if override:
        usefilename = tryfilename
    else:
        usefilename = first_available_filename(tryfilename)

    try:
        f = open(usefilename, 'w')
        f.write(grammar.body)
        f.close()
    except IOError as e:
        print "Error saving grammar '{0}' to {1}".format(
            grammar.name, usefilename)
        raise e


# Tries to write out exemplar to an image file <tryfilename>
# and returns actual file name used
#
# If <override> is true, it will write to <tryfilename> without question
# If <override> is false, it will search for the first available filename
# using first_available_filename
def save_exemplar(image, tryfilename, override=False):
    if override:
        usefilename = tryfilename
    else:
        usefilename = first_available_filename(tryfilename)

    try:
        image.save(usefilename)
    except IOError as e:
        print "IOError saving image to {0}".format(usefilename)
        raise e
    except Exception as e:
        print "Some non-io error occurred saving image to {0}:" \
              " perhaps image arg is incorrect".format(usefilename)
        raise e

    return usefilename
