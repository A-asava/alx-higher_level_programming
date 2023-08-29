#!/usr/bin/python3

import sys


def secure_execute_function(function, *args):
    try:
        result = function(*args)
        return result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
