#!/usr/bin/env python2
# Copyright 2013, Mansour Moufid <mansourmoufid@gmail.com>

from matplotlib import image, pyplot
from numpy import append, array, real, zeros
from numpy.fft import fft2, ifft2, fftshift, ifftshift
try:
    from os import EX_NOINPUT, EX_USAGE
except ImportError:
    EX_NOINPUT, EX_USAGE = 1, 2
from os.path import basename, exists, splitext
from random import randint
from sys import argv, exit, stderr

def zeropad2(x, shape):
    m, n = x.shape
    p, q = shape
    assert p > m
    assert q > n
    tb = zeros(((p - m) / 2, n))
    lr = zeros((p, (q - n) / 2))
    x = append(tb, x, axis = 0)
    x = append(x, tb, axis = 0)
    x = append(lr, x, axis = 1)
    x = append(x, lr, axis = 1)
    return x

def resize(filename, factor = 1.5):
    img = image.imread(filename)
    fft = fft2(img)
    fft = fftshift(fft)
    reshape = lambda (x, y), a: (int(a * x), int(a * y))
    fft = zeropad2(fft, reshape(img.shape, factor))
    ifft = ifftshift(fft)
    ifft = ifft2(ifft)
    ifft = real(ifft)
    return ifft

def save(img, file):
    while True:
        newfile = splitext(file)[0] + '-'
        newfile = newfile + str(randint(0,1000)) + '.png'
        if not exists(newfile):
            break
    swap = lambda (x, y): (y, x)
    fig = pyplot.figure(figsize = swap(img.shape), dpi = 1)
    fig.figimage(img, cmap = pyplot.cm.gray)
    pyplot.savefig(newfile, dpi = 1)
    return newfile

def fail(code):
    print>>stderr, 'usage: fftresize.py <file> [alpha]'
    exit(code)

if '__main__' in __name__:
    if len(argv) == 2:
        file = argv[1]
        if not exists(file):
            exit(EX_NOINPUT)
    elif len(argv) == 3:
        file = argv[1]
        if not exists(file):
            exit(EX_NOINPUT)
        try:
            factor = float(argv[2])
        except ValueError:
            fail(EX_USAGE)
    else:
        fail(EX_USAGE)
    try:
        x = resize(file, factor)
    except NameError:
        x = resize(file)
    print save(x, file)
