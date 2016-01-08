# coding=utf-8
import os
import cPickle as pickle
from PIL import Image

from conf import ROOT, DATA_PREPROCESSED, DATA_NAMED
from tools import iter_direct_files

__author__ = 'zephor'

handled = set()
handled_tmp = os.path.join(ROOT, '.handled')

if os.path.exists(handled_tmp):
    with open(handled_tmp) as _f:
        handled = pickle.load(_f)


def main():
    for _, p in iter_direct_files(DATA_PREPROCESSED):
        if _ in handled:
            continue
        im = Image.open(p)
        im.show()
        try:
            code = raw_input('验证码：')
        except KeyboardInterrupt:
            with open(handled_tmp, 'w') as f:
                pickle.dump(handled, f)
            break
        else:
            im.save(os.path.join(DATA_NAMED, code), 'jpeg')
            handled.add(_)
            print 'code:', code


if __name__ == '__main__':
    main()
