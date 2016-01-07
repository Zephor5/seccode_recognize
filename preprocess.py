# coding=utf-8
import os

from PIL import Image, ImageEnhance

from conf import DATA_RAW, DATA_PREPROCESSED
from tools import iter_direct_files

__author__ = 'zephor'


def process(img, img_path):
    im = Image.open(img_path)
    sharp_enhancer = ImageEnhance.Sharpness(im)
    im = sharp_enhancer.enhance(2)
    im = im.resize((200, 46), Image.LANCZOS)
    im.save(os.path.join(DATA_PREPROCESSED, img))


if __name__ == '__main__':
    for fn, p in iter_direct_files(DATA_RAW):
        process(fn, p)
