#!/usr/bin/env python2

from os.path import exists, splitext
from random import randint


_depth = lambda x, y, z=1: z

_invert_dict = lambda d: dict((v, k) for k, v in d.iteritems())

_PREFERRED_RGB = {
    'R': 0,
    'G': 1,
    'B': 2,
}


def depth(array):
    '''Return the depth (the third dimension) of an array.'''
    return _depth(*array.shape)


def rand_filename(filename, ext=None):
    '''Return a unique file name based on the given file name.'''
    file_name, file_ext = splitext(filename)
    if ext is None:
        ext = file_ext
    while True:
        rand_file_name = file_name
        rand_file_name += '-'
        rand_file_name += str(randint(0, 10000))
        rand_file_name += ext
        if not exists(rand_file_name):
            break
    return rand_file_name


def swap_rgb(img, rgb):
    '''Swap the RBG channels of an image array.'''
    if depth(img) == 3 and not rgb == _PREFERRED_RGB:
        rgb_inv = _invert_dict(rgb)
        rgb_order = [rgb_inv[k] for k in [0, 1, 2]]
        swap_indices = [_PREFERRED_RGB[k] for k in rgb_order]
        img = img[:, :, swap_indices]
    return img


if __name__ == '__main__':
    pass
