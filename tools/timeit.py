# -*- encoding=utf-8 -*-

import time
import sys


class timeit(object):
    def __init__(self, debug=False):
        self.debug = debug

    def __call__(self, func):
        def wrapper(*arg):
            t = time.clock()
            res = func(*arg)
            if self.debug == True:
                print func.func_name + ': ' + str(time.clock() - t)
            return res
        return wrapper
