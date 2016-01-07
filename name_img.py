# coding=utf-8
import os
import cPickle as pickle
from PIL import Image

from conf import DATA_PREPROCESSED
from tools import iter_direct_files

__author__ = 'zephor'

handled = set()


def main():
    for _, p in iter_direct_files(DATA_PREPROCESSED):
        im = Image.open(p)
        im.show()
        try:
            code = raw_input('验证码：')
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
