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
    if d.isExpanded():
        CT = d.templateArgument(value.type, 0)
        d.putArrayData(CT, d.addressOf(array), size)

def qdump__boost__geometry__model__d2__point_xy(d, value):
    array = value["m_values"]
    d.putValue(boost__geometry__point_array_to_text(array, 2))
    if d.isExpanded():
        CT = d.templateArgument(value.type, 0)
        d.putArrayData(CT, d.addressOf(array), 2)


def boost__geometry__dump_indexed(d, value, i0, i1):
    P = d.templateArgument(value.type, 0)

    # the following lines could probably be replaced by something better
    Dim = 0
    Pstr = str(P)
    if Pstr.find("boost::geometry::model::point") != -1:
        Dim = d.numericTemplateArgument(P, 1)
    elif Pstr.find("boost::geometry::model::d2::point_xy") != -1:
        Dim = 2

    if Dim > 0:
        min_array = i0["m_values"]
        max_array = i1["m_values"]
        val = '{' + boost__geometry__point_array_to_text(min_array, Dim) + ", "
        val += boost__geometry__point_array_to_text(max_array, Dim) + '}'
        d.putValue(val);

    d.putNumChild(2)
    if d.isExpanded():
        with Children(d, 2):
            d.putSubItem("[0]", i0)
            d.putSubItem("[1]", i1)

def qdump__boost__geometry__model__box(d, value):
    boost__geometry__dump_indexed(d, value, value["m_min_corner"], value["m_max_corner"])

def qdump__boost__geometry__model__segment(d, value):
    boost__geometry__dump_indexed(d, value, value["first"], value["second"])


def boost__geometry__dump_derived_from_vector(d, value, container_tparam_id):
    Cont_str = str(value.type)
    if container_tparam_id >= 0:
        Cont_str = d.extractTemplateArgument(str(value.type), container_tparam_id)
    if Cont_str.startswith("std::vector") != -1:
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
        d.putValue("%s/%s (%s)" % (numerator, denominator, approx))
    d.putNumChild(3)
    if d.isExpanded():
        with Children(d, 3):
            d.putSubItem("m_numerator", numerator)
            d.putSubItem("m_denominator", denominator)
            d.putSubItem("m_approximation", approximation)
