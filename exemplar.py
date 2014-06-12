# Jordan Cazamias
# CFDG Optimizer
# June 2014

# exemplar.py: stores exemplar class

import pickle

from PIL import Image
import save_utils


class Exemplar:
    def __init__(self, image=None, score=None):
        self.image = image
        self.score = score

    # Serializes exemplar object to file
    def pickle(self, tofile):
        image_data = None
        if self.image is not None:
            image_data = {
                'mode': self.image.mode,
                'size': self.image.size,
                'data': self.image.tostring(),
            }

        exemplar_data = {
            'image_data': image_data,
            'score': self.score
        }

        pickle.dump(exemplar_data, tofile)

    # Unpickles an exemplar object from existing file
    # and stores values in this object
    def unpickle(self, fromfile):
        exemplar_data = pickle.load(fromfile)
        image_data = exemplar_data['image_data']
        image = Image.frombytes(
            image_data['mode'],
            image_data['size'],
            image_data['data']
        )
        score = exemplar_data['score']

        self.image = image
        self.score = score

    # Tries to write out exemplar to an image file <tryfilename>
    # and returns actual file name used
    #
    # If <override> is true, it will write to <tryfilename> without question
    # If <override> is false, it will search for the first available filename
    # using first_available_filename
    def save_image(self, tryfilename, override=False):
        if override:
            usefilename = tryfilename
        else:
            usefilename = save_utils.first_available_filename(tryfilename)

        try:
            self.image.save(usefilename)
        except IOError as e:
            print "IOError saving image to {0}".format(usefilename)
            raise e
        except Exception as e:
            print "Some non-io error occurred saving image to {0}:" \
                  " perhaps image arg is incorrect".format(usefilename)
            raise e

        return usefilename
