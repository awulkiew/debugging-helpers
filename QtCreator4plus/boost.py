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
# Boost.Container debugging helpers

# Copyright (c) 2015 Adam Wulkiewicz, Lodz, Poland.
# Copyright (c) 2021 Ihor Dutchak, Kyiv, Ukraine.

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
            start = holder["m_start"].pointer()
        except:
            start = holder["storage"].address()
        d.putPlotData(start, size, T)

def qform__boost__container__static_vector():
    return [DisplayFormat.ArrayPlot]

def qdump__boost__container__static_vector(d, value):
    qdump__boost__container__vector(d, value)
# Boost.Geometry debugging helpers

# Copyright (c) 2015-2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

#################################################################
# geometries
#################################################################

from awulkiew import array_to_str
from dumper import Children

def boost__geometry__model__point(d, value, size):
    array = value["m_values"]
    d.putValue(array_to_str(array, size, 3))
    d.putNumChild(size)
    if d.isExpanded():
        with Children(d, size):
            for i in range(0, int(size)):
                d.putSubItem("<%s>" % i, array[i])

def qdump__boost__geometry__model__point(d, value):
    boost__geometry__model__point(d, value, int(value.type[1]))

def qdump__boost__geometry__model__d2__point_xy(d, value):
    boost__geometry__model__point(d, value, 2)

def qdump__boost__geometry__model__d3__point_xyz(d, value):
    boost__geometry__model__point(d, value, 3)


def boost__geometry__point_dimension(point_t):
    if point_t.name.startswith("boost::geometry::model::point"):
        return int(point_t[1])
    elif point_t.name.startswith("boost::geometry::model::d2::point_xy"):
        return 2
    elif point_t.name.startswith("boost::geometry::model::d3::point_xyz"):
        return 3
    return 0

def boost__geometry__model_indexed(d, value, i0, i1, n0, n1):
    point_t = value.type[0]
    dim = boost__geometry__point_dimension(point_t)
    if dim > 0:
        array0 = i0["m_values"]
        array1 = i1["m_values"]
        val = '{' + array_to_str(array0, dim, 3) + ", "
        val +=      array_to_str(array1, dim, 3) + '}'
        d.putValue(val)
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("<%s>" % n0, i0)
            d.putSubItem("<%s>" % n1, i1)

def qdump__boost__geometry__model__box(d, value):
    boost__geometry__model_indexed(d, value, value["m_min_corner"], value["m_max_corner"], "0:min_corner", "1:max_corner")

def qdump__boost__geometry__model__segment(d, value):
    boost__geometry__model_indexed(d, value, value["first"], value["second"], "0", "1")

def qdump__boost__geometry__model__referring_segment(d, value):
    boost__geometry__model_indexed(d, value, value["first"].dereference(), value["second"].dereference(), "0", "1")


def boost__geometry__model__container(d, value):
    d.putItem(value.members(True)[0])
    d.putBetterType(value.type)

def qdump__boost__geometry__model__linestring(d, value):
    boost__geometry__model__container(d, value)

def qdump__boost__geometry__model__ring(d, value):
    boost__geometry__model__container(d, value)

def qdump__boost__geometry__model__multi_point(d, value):
    boost__geometry__model__container(d, value)

def qdump__boost__geometry__model__multi_linestring(d, value):
    boost__geometry__model__container(d, value)

def qdump__boost__geometry__model__multi_polygon(d, value):
    boost__geometry__model__container(d, value)

def qdump__boost__geometry__model__geometry_collection(d, value):
    boost__geometry__model__container(d, value)


def qdump__boost__geometry__model__polygon(d, value):
    outer = value["m_outer"]
    d.putNumChild(2)
    if d.isExpanded():
        inners = value["m_inners"]
        with Children(d, 2):
            d.putSubItem("outer", outer)
            d.putSubItem("inners", inners)
    d.putItem(outer) # Only for putValue, children are set before

#################################################################
# index
#################################################################

def qdump__boost__geometry__index__detail__varray(d, value):
    size = int(value["m_size"])
    d.putItemCount(size)
    if d.isExpanded():
        d.putArrayData(value["m_storage"]["data_"]["buf"].address(), size, value.type[0])

def qdump__boost__geometry__index__rtree(d, value):
    members = value["m_members"]
    size = int(members["values_count"])
    d.putItemCount(size)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("m_members", members)
            d.putSubItem("root", members["root"])

def qdump__boost__geometry__index__detail__rtree__variant_internal_node(d, value):
    d.putItem(value["elements"])

def qdump__boost__geometry__index__detail__rtree__variant_leaf(d, value):
    d.putItem(value["elements"])

#################################################################
# policies
#################################################################

def qdump__boost__geometry__segment_ratio(d, value):
    numerator = value["m_numerator"]
    denominator = value["m_denominator"]
    approximation = value["m_approximation"]
    num = numerator.integer()
    den = denominator.integer()
    app = approximation.floatingPoint()
    if den == 0:
        d.putValue("%s/%s" % (num, den))
    elif num == 0:
        d.putValue(0)
    else:
        a = float(app) / 1000000.0
        d.putValue("%s/%s ~ %s" % (num, den, a))
    d.putNumChild(3)
    if d.isExpanded():
        with Children(d, 3):
            d.putSubItem("m_numerator", numerator)
            d.putSubItem("m_denominator", denominator)
            d.putSubItem("m_approximation", approximation)

#################################################################
# algorithms
#################################################################

def qdump__boost__geometry__segment_identifier(d, value):
    so = value["source_index"]
    mu = value["multi_index"]
    ri = value["ring_index"]
    se = value["segment_index"]
    d.putValue(array_to_str([so, mu, ri, se], 4, 4))
    d.putNumChild(4)
    if d.isExpanded():
        with Children(d, 4):
            d.putSubItem("source_index", so)
            d.putSubItem("multi_index", mu)
            d.putSubItem("ring_index", ri)
            d.putSubItem("segment_index", se)

def qdump__boost__geometry__ring_identifier(d, value):
    so = value["source_index"]
    mu = value["multi_index"]
    ri = value["ring_index"]
    d.putValue(array_to_str([so, mu, ri], 3, 3))
    d.putNumChild(3)
    if d.isExpanded():
        with Children(d, 3):
            d.putSubItem("source_index", so)
            d.putSubItem("multi_index", mu)
            d.putSubItem("ring_index", ri)

#################################################################
# srs
#################################################################

def qdump__boost__geometry__srs__sphere(d, value):
    r = value["m_r"]
    d.putValue(array_to_str([r], 1, 1))
    d.putNumChild(1)
    if d.isExpanded():
        with Children(d, 1):
            d.putSubItem("radius", r)

def qdump__boost__geometry__srs__spheroid(d, value):
    a = value["m_a"]
    b = value["m_b"]
    d.putValue(array_to_str([a, b], 2, 2))
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("a", a)
            d.putSubItem("b", b)# Boost.Math debugging helpers

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
# Boost.Rational debugging helpers

# Copyright (c) 2015-2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from dumper import Children

def qdump__boost__rational(d, value):
    numerator = value["num"]
    denominator = value["den"]
    num = numerator.integer()
    den = denominator.integer()
    if den == 0:
        d.putValue("%s/%s" % (num, den))
    elif num == 0:
        d.putValue(0)
    else:
        f = float(int(num)) / float(int(den))
        d.putValue("%s/%s ~ %s" % (num, den, f))
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("num", numerator)
            d.putSubItem("den", denominator)
# Boost.Tuple debugging helpers

# Copyright (c) 2015-2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from dumper import Children, SubItem

def boost__tuple__put_children(d, value, current, i, count):
    if i < count:
        val = current["head"]
        with SubItem(d, "<%s>" % i):
            d.putItem(val)
        next_i = i + 1
        if next_i < count:
            boost__tuple__put_children(d, value, current["tail"], next_i, count)

def qdump__boost__tuples__tuple(d, value):
    count = 0
    while (count < 10):
       type = value.type[count]
       if type.name == "boost::tuples::null_type":
           break
       count = count + 1
    d.putItemCount(count)
    if d.isExpanded():
        with Children(d, count):
            boost__tuple__put_children(d, value, value, 0, count)
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
    if ix > 0:
        which = ix - 1
        type = value.type[which]
        type_name = str(type.unqualified())
        type_name = type_name[:type_name.find('<')]
        type_name = type_name[type_name.rfind("::")+2:]
        d.putValue("<%s:%s>" % (which, type_name))
    else:
        d.putValue("<none>")
    d.putNumChild(1)
    if d.isExpanded():
        with Children(d, 1):
            count = len(value.type.templateArguments())
            boost__variant2__variant_put(d, value, value["st1_"], 0, ix, count)
