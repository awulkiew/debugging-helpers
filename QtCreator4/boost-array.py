# Boost.Array debugging helpers

# Copyright (c) 2015-2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

def qdump__boost__array(d, value):
    size = int(value.type[1])
    d.putItemCount(size)
    if d.isExpanded():
        d.putArrayData(value["elems"].address(), size, value.type[0])
