# Boost.Container debugging helpers

# Copyright (c) 2015 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

def qdump__boost__container__vector(d, value):
    holder = value["m_holder"]
    size = holder["m_size"]
    d.putItemCount(size)
#    d.putNumChild(size)
    if d.isExpanded():
        T = d.templateArgument(value.type, 0)
        try:
            d.putArrayData(T, holder["m_start"], size)
        except:
            try:
                d.putArrayData(T, d.addressOf(holder["storage"]), size)
            except:
                with Children(d, 1):
                    d.putSubItem("m_holder", holder)

def qdump__boost__container__static_vector(d, value):
    qdump__boost__container__vector(d, value)
