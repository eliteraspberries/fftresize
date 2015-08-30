#!/usr/bin/env python

'''FFTresize resizes images using zero-padding in the frequency
domain.
'''

from avena import image, interp


__author__ = 'Mansour Moufid'
__copyright__ = 'Copyright 2013-2015, Mansour Moufid'
__license__ = 'ISC'
__version__ = '0.7'
__email__ = 'mansourmoufid@gmail.com'
__status__ = 'Development'


_EXT = '.png'


def resize(filename, factor=1.5):
    '''Resize an image by zero-padding in the frequency domain.

    Return the filename of the resized image.
    '''
    img = image.read(filename)
    new = interp.interp2(img, factor)
    return image.save(new, filename, random=True, ext=_EXT, normalize=True)


if '__main__' in __name__:
    pass
