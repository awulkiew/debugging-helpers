# Boost.Geometry debugging helpers

# Copyright (c) 2015-2021 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

#################################################################
# geometries
#################################################################

from dumper import Children, SubItem

def boost__geometry__point_array_to_text(array, size):
    res = '{'
    if size > 0:
        res += array[0].display()
    if size > 1:
        res += ", " + array[1].display()
    if size > 2:
        res += ", " + array[2].display()
    if size > 3:
        res += ", ..."
    res += '}'
    return res

def boost__geometry__model__point(d, value, size):
    array = value["m_values"]
    d.putValue(boost__geometry__point_array_to_text(array, size))
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
        val = '{' + boost__geometry__point_array_to_text(array0, dim) + ", "
        val +=      boost__geometry__point_array_to_text(array1, dim) + '}'
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
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            outer = value["m_outer"]
            inners = value["m_inners"]
            d.putSubItem("exterior", outer)
            d.putSubItem("interior", inners)

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

def boost__geometry__segment_identifier_to_str(value):
    source_index = value["source_index"].display()
    multi_index = value["multi_index"].display()
    ring_index = value["ring_index"].display()
    segment_index = value["segment_index"].display()
    return "{%s, %s, %s, %s}" % (source_index, multi_index, ring_index, segment_index)

def qdump__boost__geometry__segment_identifier(d, value):
    d.putValue(boost__geometry__segment_identifier_to_str(value))
    d.putNumChild(4)
    if d.isExpanded():
        with Children(d, 4):
            d.putSubItem("source_index", value["source_index"])
            d.putSubItem("multi_index", value["multi_index"])
            d.putSubItem("ring_index", value["ring_index"])
            d.putSubItem("segment_index", value["segment_index"])
