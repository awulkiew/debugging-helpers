# Boost.Geometry debugging helpers

# Copyright (c) 2015 Adam Wulkiewicz, Lodz, Poland.

# Use, modification and distribution is subject to the Boost Software License,
# Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

#################################################################
# geometries
#################################################################

def boost__geometry__point_array_to_text(array, size):
    res = '{'
    if size > 0:
        res += "%s" % (array[0])
    if size > 1:
        res += ", %s" % (array[1])
    if size > 2:
        res += ", %s" % (array[2])
    if size > 3:
        res += " ..."
    res += '}'
    return res;

def qdump__boost__geometry__model__point(d, value):
    size = d.numericTemplateArgument(value.type, 1)
    array = value["m_values"]
    d.putValue(boost__geometry__point_array_to_text(array, size))
    d.putNumChild(size)
    if d.isExpanded():
        with Children(d, size):
            for i in range(0, int(size)):
                d.putSubItem("<%s>"%i, array[i])

def qdump__boost__geometry__model__d2__point_xy(d, value):
    array = value["m_values"]
    d.putValue(boost__geometry__point_array_to_text(array, 2))
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("<0>", array[0])
            d.putSubItem("<1>", array[1])

def boost__geometry__point_dimension(d, point_type):
    point_str = str(point_type)
    if point_str.startswith("boost::geometry::model::point"):
        return int(d.numericTemplateArgument(point_type, 1))
    elif point_str.startswith("boost::geometry::model::d2::point_xy"):
        return 2
    return 0

def boost__geometry__dump_indexed(d, value, i0, i1, n0, n1):
    P = d.templateArgument(value.type, 0)
    Dim = boost__geometry__point_dimension(d, P)

    if Dim > 0:
        min_array = i0["m_values"]
        max_array = i1["m_values"]
        val = '{' + boost__geometry__point_array_to_text(min_array, Dim) + ", "
        val += boost__geometry__point_array_to_text(max_array, Dim) + '}'
        d.putValue(val);
    else:
        d.putValue("@0x%x" % value.address)

    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("<%s>" % n0, i0)
            d.putSubItem("<%s>" % n1, i1)

def qdump__boost__geometry__model__box(d, value):
    boost__geometry__dump_indexed(d, value, value["m_min_corner"], value["m_max_corner"], "0:min_corner", "1:max_corner")

def qdump__boost__geometry__model__segment(d, value):
    boost__geometry__dump_indexed(d, value, value["first"], value["second"], "0", "1")

def qdump__boost__geometry__model__referring_segment(d, value):
    boost__geometry__dump_indexed(d, value, value["first"], value["second"], "0", "1")


def boost__geometry__dump_derived_from_vector(d, value, container_tparam_id):
    Cont_str = str(value.type)
    if container_tparam_id >= 0:
        Cont_str = d.extractTemplateArgument(str(value.type), container_tparam_id)
    if Cont_str.startswith("std::vector"):
        qdump__std__vector(d, value)
    else:
        d.putPlainChildren(value)

def qdump__boost__geometry__model__linestring(d, value):
    boost__geometry__dump_derived_from_vector(d, value, 1)

def qdump__boost__geometry__model__ring(d, value):
    boost__geometry__dump_derived_from_vector(d, value, 3)

def qdump__boost__geometry__model__multi_point(d, value):
    boost__geometry__dump_derived_from_vector(d, value, 1)

def qdump__boost__geometry__model__multi_linestring(d, value):
    boost__geometry__dump_derived_from_vector(d, value, 1)

def qdump__boost__geometry__model__multi_polygon(d, value):
    boost__geometry__dump_derived_from_vector(d, value, 1)


def qdump__boost__geometry__model__polygon(d, value):
    d.putValue("@0x%x" % value.address)
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            outer = value["m_outer"]
            inners = value["m_inners"]
            with SubItem(d, "external"):
                boost__geometry__dump_derived_from_vector(d, outer, 3)
                d.putBetterType(str(d.templateArgument(inners.type, 0)))
            with SubItem(d, "internal"):
                boost__geometry__dump_derived_from_vector(d, inners, -1)
                d.putBetterType("RingList")

#################################################################
# index
#################################################################

def qdump__boost__geometry__index__detail__varray(d, value):
    size = value["m_size"]
    storage = value["m_storage"]["data_"]["buf"]
    T = d.templateArgument(value.type, 0)
    d.putItemCount(size)
    d.putNumChild(1)
    if d.isExpanded():
        d.putArrayData(T, storage.cast(T.pointer()), size)

def qdump__boost__geometry__index__rtree(d, value):
    members = value["m_members"]
    size = members["values_count"]
    d.putItemCount(size)
    d.putNumChild(2)
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
    if denominator == 0:
        d.putValue("%s/%s" % (numerator, denominator))
    elif numerator == 0:
        d.putValue(0)
    else:
        approx = approximation / 1000000.0
        d.putValue("%s/%s ~ %s" % (numerator, denominator, approx))
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
    source_index = value["source_index"]
    multi_index = value["multi_index"]
    ring_index = value["ring_index"]
    segment_index = value["segment_index"]
    return "{%s, %s, %s, %s}" % (source_index, multi_index, ring_index, segment_index);

def qdump__boost__geometry__segment_identifier(d, value):
    d.putValue(boost__geometry__segment_identifier_to_str(value))
    d.putNumChild(4)
    if d.isExpanded():
        with Children(d, 4):
            d.putSubItem("source_index", value["source_index"])
            d.putSubItem("multi_index", value["multi_index"])
            d.putSubItem("ring_index", value["ring_index"])
            d.putSubItem("segment_index", value["segment_index"])

def qdump__boost__geometry__detail__overlay__turn_operation(d, value):
    operation = value["operation"]
    simple_op = str(operation)[44:]
    d.putValue(simple_op)
    d.putNumChild(3)
    if d.isExpanded():
        with Children(d, 3):
            with SubItem(d, "operation"):
                d.putValue(simple_op)
                d.putType(operation.type)
                d.putNumChild(0)
            d.putSubItem("seg_id", value["seg_id"])
            d.putSubItem("fraction", value["fraction"])

def qdump__boost__geometry__detail__overlay__turn_operation_linear(d, value):
    operation = value["operation"]
    simple_op = str(operation)[44:]
    d.putValue(simple_op)
    d.putNumChild(5)
    if d.isExpanded():
        with Children(d, 5):
            with SubItem(d, "operation"):
                d.putValue(simple_op)
                d.putType(operation.type)
                d.putNumChild(0)
            d.putSubItem("seg_id", value["seg_id"])
            d.putSubItem("fraction", value["fraction"])
            d.putSubItem("is_collinear", value["is_collinear"])
            with SubItem(d, "position"):
                position = value["position"]
                simple_pos = str(position)[43:]
                d.putValue(simple_pos)
                d.putType(position.type)
                d.putNumChild(0)

def qdump__boost__geometry__detail__overlay__turn_info(d, value):
    point = value["point"]
    method = value["method"]
    discarded = value["discarded"]
    selectable_start = value["selectable_start"]
    operations = value["operations"]
    simple_method = str(method)[41:]
    simple_op0 = str(operations["elems"][0]["operation"])[44:]
    simple_op1 = str(operations["elems"][1]["operation"])[44:]
    simple_operations = simple_op0 + ", " + simple_op1;

    val_str = simple_method
    dim = boost__geometry__point_dimension(d, point.type)
    if dim > 0:
        val_str += " (" + simple_operations + ") " + boost__geometry__point_array_to_text(point["m_values"], dim)
    d.putValue(val_str)

    d.putNumChild(5)
    if d.isExpanded():
        with Children(d, 5):
            d.putSubItem("point", point)
            with SubItem(d, "method"):
                d.putValue(simple_method)
                d.putType(method.type)
                d.putNumChild(0)
            d.putSubItem("discarded", discarded)
            d.putSubItem("selectable_start", selectable_start)
            with SubItem(d, "operations"):
                d.putValue(simple_operations)
                d.putType(operations.type)
                d.putNumChild(2)
                if d.isExpanded():
                    with Children(d, 2):
                        d.putSubItem("[0]", operations["elems"][0])
                        d.putSubItem("[1]", operations["elems"][1])

def qdump__boost__geometry__side_info(d, value):
    sides = value["sides"]
    side0 = sides[0]
    side1 = sides[1]
    side00 = side0["first"]
    side01 = side0["second"]
    side10 = side1["first"]
    side11 = side1["second"]
    d.putValue("{{%s, %s},{%s, %s}}" % (side00, side01, side10, side11))
    d.putType(value.type)
    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("[0]", side0)
            d.putSubItem("[1]", side1)
