#!/usr/bin/env python2

'''Resize images using the FFT

FFTresize resizes images using zero-padding in the frequency domain.
'''


from matplotlib import image, pyplot
from numpy import append, around, real, zeros as _zeros
from numpy import amax, amin
from numpy.fft import fft2, ifft2, fftshift, ifftshift
try:
    from os import EX_NOINPUT as _EX_NOINPUT
    from os import EX_USAGE as _EX_USAGE
except ImportError:
    _EX_NOINPUT, _EX_USAGE = 1, 2
from os.path import exists, splitext
from random import randint
from sys import argv as _argv, exit as _exit, stderr as _stderr
from sys import float_info as _float_info


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


_channels = lambda x, y, z=1: z


def resize(filename, factor=1.5):
    '''Resize an image by zero-padding in the frequency domain.

    Return the filename of the resized image.
    '''
    img = image.imread(filename)
    reshape = lambda a, x, y, z=1: (int(a * x), int(a * y), z)
    newsize = reshape(factor, *img.shape)
    if (newsize[0] - img.shape[0]) % 2 != 0:
        newsize = (newsize[0] + 1, newsize[1]) + newsize[2:]
    if (newsize[1] - img.shape[1]) % 2 != 0:
        newsize = (newsize[0], newsize[1] + 1) + newsize[2:]
    nchannels = _channels(*img.shape)
    if nchannels == 1:
        new = _fft_interp(img, newsize[:2])
    else:
        new = _zeros(newsize)
        for i in range(nchannels):
            rgb = img[:, :, i]
            newrgb = _fft_interp(rgb, newsize[:2])
            new[:, :, i] = newrgb
    return _save(new, filename)


def _normalize(array):
    min = amin(array)
    max = amax(array)
    array -= min
    array /= max - min
    eps = 10.0 * _float_info.epsilon
    negs = array < 0.0 + eps
    array[negs] = 0.0
    bigs = array > 1.0 - eps
    array[bigs] = 1.0
    return


def _save(img, file):
    while True:
        newfile = splitext(file)[0] + '-'
        newfile = newfile + str(randint(0, 1000)) + '.png'
        if not exists(newfile):
            break
    _normalize(img)
    touint8 = lambda x: around(x * 255, decimals=0).astype('uint8')
    if _channels(*img.shape) == 1:
        cmap = pyplot.cm.gray
    else:
        cmap = None
    pyplot.imsave(newfile, touint8(img), cmap=cmap)
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
