# Boost.Container debugging helpers

# Copyright (c) 2015 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

def qform__boost__container__vector():
    return [DisplayFormat.ArrayPlot]

def qdump__boost__container__vector(d, value):
    holder = value["m_holder"]
    size = holder["m_size"].integer()
    d.putItemCount(size)

    if d.isExpanded():
        T = value.type[0]
        try:
            d.putPlotData(holder["m_start"].pointer(), size, T)
        except:
            try:
                d.putPlotData(holder["storage"].address(), size, T)
            except:
                pass
                # FIXME: this doesn't work anymore
                # with Children(d, 1):
                    # d.putSubItem("m_holder", holder)

def qform__boost__container__static_vector():
    return [DisplayFormat.ArrayPlot]

def qdump__boost__container__static_vector(d, value):
    qdump__boost__container__vector(d, value)
