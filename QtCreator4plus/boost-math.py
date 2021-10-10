# Boost.Math debugging helpers

# Copyright (c) 2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from awulkiew import array_to_str
from dumper import Children

def qdump__boost__math__octonion(d, value):
    aa = value["a"]
    bb = value["b"]
    cc = value["c"]
    dd = value["d"]
    d.putValue(array_to_str([aa, bb, cc, dd, 0], 5, 4)) # 0 is dummy value
    d.putNumChild(8)
    if d.isExpanded():
        with Children(d, 8):
            d.putSubItem("a", aa)
            d.putSubItem("b", bb)
            d.putSubItem("c", cc)
            d.putSubItem("d", dd)
            d.putSubItem("e", value["e"])
            d.putSubItem("f", value["f"])
            d.putSubItem("g", value["g"])
            d.putSubItem("h", value["h"])

def qdump__boost__math__quaternion(d, value):
    aa = value["a"]
    bb = value["b"]
    cc = value["c"]
    dd = value["d"]
    d.putValue(array_to_str([aa, bb, cc, dd], 4, 4))
    d.putNumChild(4)
    if d.isExpanded():
        with Children(d, 4):
            d.putSubItem("a", aa)
            d.putSubItem("b", bb)
            d.putSubItem("c", cc)
            d.putSubItem("d", dd)
