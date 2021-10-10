# Boost.QVM debugging helpers

# Copyright (c) 2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from awulkiew import array_to_str
from dumper import Children, SubItem

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
                    d.putValue(array_to_str(array[r], cols, 4))

def qdump__boost__qvm__quat(d, value):
    array = value["a"]
    d.putValue(array_to_str(array, 4, 4))
    d.putNumChild(4)
    if d.isExpanded():
        d.putArrayData(array.address(), 4, value.type[0])

def qdump__boost__qvm__vec(d, value):
    array = value["a"]
    size = int(value.type[1])
    d.putValue(array_to_str(array, size, 4))
    d.putNumChild(size)
    if d.isExpanded():
        d.putArrayData(array.address(), size, value.type[0])
