FFTresize resizes images using zero-padding in the frequency
domain.

Installation
============

FFTresize requires docopt, PIL, NumPy, and matplotlib.

FFTresize consists of a package and a script.

To install these from the source code,

::

    gunzip < FFTresize-0.4.1.tar.gz | tar -xf -
    cd FFTresize-0.4.1/
    python setup.py install

or with pip,

::

    pip install fftresize

Usage
=====

The fftresize script accepts two arguments: the file name of
the image to resize, and a decimal factor by which to resize
the image (1.0 meaning no change).

::

    FFTresize - Resize images using the FFT

    Usage:
        fftresize <image> <factor>
        fftresize -h | --help
        fftresize -v | --version

    Options:
        -h, --help      Print this help.
        -v, --version   Print version information.
