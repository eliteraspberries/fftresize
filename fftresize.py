#!/usr/bin/env python2

'''Resize images using the FFT

FFTresize resizes images using zero-padding in the frequency domain.

Only monochromatic images with no transparency are supported.
'''


from matplotlib import image, pyplot
from numpy import append, around, real, zeros as _zeros
from numpy.fft import fft2, ifft2, fftshift, ifftshift
try:
    from os import EX_NOINPUT as _EX_NOINPUT
    from os import EX_USAGE as _EX_USAGE
except ImportError:
    _EX_NOINPUT, _EX_USAGE = 1, 2
from os.path import exists, splitext
from random import randint
from sys import argv as _argv, exit as _exit, stderr as _stderr


__author__ = 'Mansour Moufid'
__copyright__ = 'Copyright 2013, Mansour Moufid'
__license__ = 'ISC'
__version__ = '0.1'
__email__ = 'mansourmoufid@gmail.com'
__status__ = 'Development'


def _zeropad2(x, shape):
    '''Pad a two-dimensional NumPy array with zeros along its borders
    to the specified shape.
    '''
    m, n = x.shape
    p, q = shape
    assert p > m
    assert q > n
    tb = _zeros(((p - m) / 2, n))
    lr = _zeros((p, (q - n) / 2))
    x = append(tb, x, axis=0)
    x = append(x, tb, axis=0)
    x = append(lr, x, axis=1)
    x = append(x, lr, axis=1)
    return x


def _fft_interp(array, dim):
    '''Interpolate a two-dimensional NumPy array using zero-padding
    in the frequency domain.
    '''
    fft = fft2(array)
    fft = fftshift(fft)
    fft = _zeropad2(fft, dim)
    ifft = ifftshift(fft)
    ifft = ifft2(ifft)
    ifft = real(ifft)
    return ifft


def resize(filename, factor=1.5):
    '''Resize an image by zero-padding in the frequency domain.

    Return the filename of the resized image.
    '''
    img = image.imread(filename)
    reshape = lambda (x, y), a: (int(a * x), int(a * y))
    new = _fft_interp(img, reshape(img.shape, factor))
    return _save(new, filename)


def _save(img, file):
    while True:
        newfile = splitext(file)[0] + '-'
        newfile = newfile + str(randint(0, 1000)) + '.png'
        if not exists(newfile):
            break
    touint8 = lambda x: around(x * 255, decimals=0).astype('uint8')
    pyplot.imsave(newfile, touint8(img), cmap=pyplot.cm.gray)
    return newfile


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
