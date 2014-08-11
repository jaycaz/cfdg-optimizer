# Jordan Cazamias
# August 2014
# CFDG Optimizer

# exsave: Utilities for saving exemplars

import pickle as p

from PIL import Image

from cfdg_optimizer.utils import saveutils


# Serializes exemplar object to file
def pickle(exemplar, tofile):
    image_data = None
    if exemplar.image is not None:
        image_data = {
            'mode': exemplar.image.mode,
            'size': exemplar.image.size,
            'data': exemplar.image.tostring(),
            }

    exemplar_data = {
        'image_data': image_data,
        'score': exemplar.score
    }

    p.dump(exemplar_data, tofile)


# Unpickles an exemplar object from existing file
# and stores values in this object
def unpickle(exemplar, fromfile):
    exemplar_data = p.load(fromfile)
    image_data = exemplar_data['image_data']
    image = Image.frombytes(
        image_data['mode'],
        image_data['size'],
        image_data['data']
    )
    score = exemplar_data['score']

    exemplar.image = image
    exemplar.score = score


# Tries to write out exemplar to an image file <tryfilename>
# and returns actual file name used
#
# If <override> is true, it will write to <tryfilename> without question
# If <override> is false, it will search for the first available filename
# using first_available_filename
def save_image(exemplar, tryfilename, override=False):
    if override:
        usefilename = tryfilename
    else:
        usefilename = saveutils.first_available_filename(tryfilename)

    try:
        exemplar.image.save(usefilename)
    except IOError as e:
        print "IOError saving image to {0}".format(usefilename)
        raise e
    except Exception as e:
        print "Some non-io error occurred saving image to {0}:" \
              " perhaps image arg is incorrect".format(usefilename)
        raise e

    return usefilename
