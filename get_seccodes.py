# coding=utf-8
import urllib2
import threading

from conf import DATA_RAW
__author__ = 'zephor'


url = 'http://weixin.sogou.com/antispider/util/seccode.php'
N = 299
L = threading.Lock()


def get_num():
    global N
    L.acquire()
    try:
        N += 1
        return N
    finally:
        L.release()


def fetch(limit=10):
    i = 0
    while i < limit:
        f = urllib2.urlopen(url, timeout=2)
        with open('%scode_%d.jpg' % (DATA_RAW, get_num()), 'w') as _f:
            _f.write(f.read())
        i += 1


def main():
    pool = []
    for i in range(10):
        t = threading.Thread(target=fetch, args=(10,))
        t.start()
        pool.append(t)
    for p in pool:
        p.join()


if __name__ == '__main__':
    main()
