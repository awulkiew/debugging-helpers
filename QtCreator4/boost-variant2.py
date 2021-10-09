# Boost.Variant2 debugging helpers

# Copyright (c) 2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from dumper import Children

def boost__variant2__variant_put(d, value, current, i, ix, count):
    if i > count:
        return
    if i == ix:
        d.putSubItem("value", current["first_"])
    else:
        boost__variant2__variant_put(d, value, current["rest_"], i + 1, ix, count)

def qdump__boost__variant2__variant(d, value):
    ix = int(value["ix_"].integer())
    if ix < 0:
        return # TODO: handle double-buffered
    count = len(value.type.templateArguments())
    v = "<none>"
    if (ix > 0):
        which = ix - 1
        type = value.type[which]
        type_name = str(type.unqualified())
        type_name = type_name[:type_name.find('<')]
        type_name = type_name[type_name.rfind("::")+2:]
        v = "<%s:%s>" % (which, type_name)
    d.putValue(v)
    d.putNumChild(1)
    if d.isExpanded():
        with Children(d, 1):
            boost__variant2__variant_put(d, value, value["st1_"], 0, ix, count)
