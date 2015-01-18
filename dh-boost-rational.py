# Boost.Rational debugging helpers

# Copyright (c) 2015 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

def qdump__boost__rational(d, value):
    num = value["num"]
    den = value["den"]
    if den == 0:
        d.putValue("%s/%s" % (num, den))
    elif num == 0:
        d.putValue(0)
    else:
        f = float(int(num)) / float(int(den))
        d.putValue("%s/%s (%s)" % (num, den, f))
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("num", num)
            d.putSubItem("den", den)
