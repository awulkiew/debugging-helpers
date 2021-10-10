# Boost.Variant debugging helpers

# Copyright (c) 2015-2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from dumper import Children

def qdump__boost__variant(d, value):
    which = int(value["which_"].integer())
    type = value.type[which]
    type_name = str(type.unqualified())
    type_name = type_name[:type_name.find('<')]
    type_name = type_name[type_name.rfind("::")+2:]
    d.putValue("<%s:%s>" % (which, type_name))
    d.putNumChild(1)
    if d.isExpanded():
        storage = value["storage_"]["data_"]["buf"]
        with Children(d, 1):
            d.putSubItem("value", storage.cast(type))
