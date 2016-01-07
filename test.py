# coding=utf-8
import os
import time
from PIL import Image, ImageEnhance, ImageFilter

__author__ = 'zephor'

ROOT = os.path.abspath(os.path.dirname(__file__))

_256to128 = (
    0.0625, 0, 0, 0,
    0, 0.0625, 0, 0,
    0, 0, 0.0625, 0
)

_128to256 = (
    8, 0, 0, 0,
    0, 8, 0, 0,
    0, 0, 8, 0
)


def main():
    im = Image.open(os.path.join(ROOT, 'images/v4191j.jpg'))
    sharp_enhancer = ImageEnhance.Sharpness(im)
    im = sharp_enhancer.enhance(5)
    im = im.resize((120, 27), Image.LANCZOS)
    im.show('original')
    # im = im.convert('RGB', _256to128, colors=16)
    # white = (255, 255, 255)
    # data = im.getdata()
    colors = {}
    # im = im.convert('P')
    # for i in xrange(im.size[0]):
    #     for j in xrange(im.size[1]):
    #         _c = im.getpixel((i, j))
    #         if 5 < (max(_c) - min(_c)) < 7:
    #             im.putpixel((i, j), white)
    #             _c = white
    #         if _c is white:
    #             continue
    #         if _c not in colors:
    #             colors[_c] = 1
    #         else:
    #             colors[_c] += 1
    # res = sorted(colors.items(), key=lambda x: x[1])
    # res.reverse()
    # print res
    # im = im.convert('RGB', _128to256)
    # im.save(os.path.join(ROOT, 'images/test.jpg'))
    # im.show('converted')


if __name__ == '__main__':
    _st = time.time()
    main()
    print 'take', time.time() - _st

