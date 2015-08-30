FFTresize resizes images using zero-padding in the frequency
domain.

[![](https://travis-ci.org/eliteraspberries/fftresize.svg)][build-status]
[![](https://img.shields.io/pypi/v/FFTresize.svg)][pypi]

*New*: Get the app for OS X: <https://www.eliteraspberries.com/hecta/>.


Installation
============

FFTresize requires the [Avena][] and [docopt][] libraries.

Install FFTresize with [pip][],

    pip install fftresize


Usage
=====

The fftresize script accepts two arguments: the file name of
the image to resize, and a decimal factor by which to resize
the image (1.0 meaning no change).

    FFTresize - Resize images using the FFT

    Usage:
        fftresize <factor> <file>...
        fftresize -h | --help
        fftresize -v | --version

    Options:
        -h, --help      Print this help.
        -v, --version   Print version information.


Example
=======

Below is an example image, resized to twice its original size.

![][example-img]

![][resized-img]


[Avena]: https://pypi.python.org/pypi/Avena
[docopt]: http://docopt.org/
[pip]: https://pip.pypa.io/en/stable/
[example-img]: http://www.eliteraspberries.com/images/drink.png
[resized-img]: http://www.eliteraspberries.com/images/drink-2x.png
[build-status]: https://travis-ci.org/eliteraspberries/fftresize
[pypi]: https://pypi.python.org/pypi/FFTresize
