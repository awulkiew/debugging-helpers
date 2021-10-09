# Boost.QVM debugging helpers

# Copyright (c) 2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from dumper import Children, SubItem

def boost__qvm__vec_array_to_text(array, size):
    res = '{'
    if size > 0:
        res += array[0].display()
    if size > 1:
        res += ", " + array[1].display()
    if size > 2:
        res += ", " + array[2].display()
    if size > 3:
        res += ", ..."
    res += '}'
    return res

def qdump__boost__qvm__mat(d, value):
    array = value["a"]
    rows = int(value.type[1])
    cols = int(value.type[2])
    d.putItemCount(rows)
    if d.isExpanded():
        with Children(d, rows):
            for r in range(0, rows):
                with SubItem(d, "[%s]" % r):
                    d.putItem(array[r])
                    d.putValue(boost__qvm__vec_array_to_text(array[r], cols))

def qdump__boost__qvm__quat(d, value):
    array = value["a"]
    d.putValue('{' + array[0].display() + ", " + array[1].display() + ", " + array[2].display() + ", " + array[3].display() + '}')
    d.putNumChild(4)
    if d.isExpanded():
        d.putArrayData(array.address(), 4, value.type[0])

def qdump__boost__qvm__vec(d, value):
    array = value["a"]
    size = int(value.type[1])
    d.putValue(boost__qvm__vec_array_to_text(array, size))
    d.putNumChild(size)
    if d.isExpanded():
        d.putArrayData(array.address(), size, value.type[0])
