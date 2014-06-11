# Jordan Cazamias
# CFDG Optimizer
# June 2014

# exemplar.py: stores exemplar class

import pickle

from PIL import Image

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

