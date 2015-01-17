# Boost.Tuple debugging helpers

# Copyright (c) 2015 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

def boost__tuple__put_children(d, value, current, i, count):
    if i < count:
        val = current["head"]
        with SubItem(d, "<%s>" % i):
            d.putItem(val)
            d.putBetterType(str(d.templateArgument(value.type, i)))
        next_i = i + 1
        if next_i < count:
            boost__tuple__put_children(d, value, current["tail"], next_i, count)

def qdump__boost__tuples__tuple(d, value):
    count = 0
    while (count < 10):
       type = d.templateArgument(value.type, count)
       if str(type) == "boost::tuples::null_type":
           break
       count = count + 1
    #d.putValue("<length: %s>" % count)
    d.putItemCount(count)
    d.putNumChild(count)
    if d.isExpanded():
        with Children(d, count):
            boost__tuple__put_children(d, value, value, 0, count)
