#!/usr/bin/env python2

'''Resize images using the FFT

FFTresize resizes images using zero-padding in the frequency domain.
'''


from fftinterp import interp2
import imutils
from numpy import zeros as _zeros
try:
    from os import EX_NOINPUT as _EX_NOINPUT
    from os import EX_USAGE as _EX_USAGE
except ImportError:
    _EX_NOINPUT, _EX_USAGE = 1, 2
from os.path import exists
from sys import argv as _argv, exit as _exit, stderr as _stderr


__author__ = 'Mansour Moufid'
__copyright__ = 'Copyright 2013, Mansour Moufid'
__license__ = 'ISC'
__version__ = '0.2'
__email__ = 'mansourmoufid@gmail.com'
__status__ = 'Development'


def resize(filename, factor=1.5):
    '''Resize an image by zero-padding in the frequency domain.

    Return the filename of the resized image.
    '''
    img = imutils.read(filename)
    nchannels = imutils.channels(img)
    if nchannels == 1:
        new = interp2(img, factor)
    else:
        new = None
        for i in range(nchannels):
            rgb = img[:, :, i]
            newrgb = interp2(rgb, factor)
            if new is None:
                newsize = list(newrgb.shape)
                newsize.append(imutils.channels(img))
                new = _zeros(tuple(newsize))
            new[:, :, i] = newrgb
    return imutils.save(new, filename)


def _fail(code):
    print>>_stderr, 'usage: fftresize.py <file> [alpha]'
    _exit(code)


if '__main__' in __name__:
    if len(_argv) == 2:
        file = _argv[1]
        if not exists(file):
            _exit(_EX_NOINPUT)
    elif len(_argv) == 3:
        file = _argv[1]
        if not exists(file):
            _exit(_EX_NOINPUT)
        try:
            factor = float(_argv[2])
        except ValueError:
            _fail(_EX_USAGE)
    else:
        _fail(_EX_USAGE)
    try:
        x = resize(file, factor)
    except NameError:
        x = resize(file)
    print x
