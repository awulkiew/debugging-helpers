# Utilities for debugging helpers

# Copyright (c) 2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

def is_float(type):
    # TypeCode.Float
    return type.code == 4 and type.size() == 4

def float_to_str(value):
    return "{:.6g}".format(float(value.floatingPoint()))

def array_to_str(array, size, maxsize = 3):
    res = '{'
    if size > 0:
        if is_float(array[0].type):
            res += float_to_str(array[0])
            for i in range(1, min(size, maxsize)):
                res += ", " + float_to_str(array[i])
        else:
            res += array[0].display()
            for i in range(1, min(size, maxsize)):
                res += ", " + array[i].display()
        if size > maxsize:
            res += ", ..."
    res += '}'
    return res
