# coding=utf-8
import os

__author__ = 'zephor'


def iter_direct_files(d):
    for _, __, files in os.walk(d):
        for _f in files:
            yield _f, os.path.join(_, _f)
