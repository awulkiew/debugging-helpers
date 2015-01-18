# Debugging Helpers for QtCreator

![example](example.png)

Currently supported:

* Boost.Geometry
  * boost::geometry::index::detail::rtree::variant_internal_node
  * boost::geometry::index::detail::rtree::variant_leaf
  * boost::geometry::index::detail::varray
  * boost::geometry::index::rtree
  * boost::geometry::model::box
  * boost::geometry::model::d2::point_xy
  * boost::geometry::model::linestring
  * boost::geometry::model::multi_point
  * boost::geometry::model::multi_linestring
  * boost::geometry::model::multi_polygon
  * boost::geometry::model::point
  * boost::geometry::model::polygon
  * boost::geometry::model::referring_segment
  * boost::geometry::model::ring
  * boost::geometry::model::segment
  * boost::geometry::segment_ratio
* Boost.Rational
  * boost::rational
* Boost.Tuple
  * boost::tuple
* Boost.Variant
  * boost::variant

To use, in **~/.gdbinit** or **QtCreator > Tools > Options > Debugger > GDB > Additional Startup Commands** put

    python execfile('path_to_filename.py')

if GDB was linked against python 2 or

    python exec(open('path_to_filename.py').read())

if GDB was linked against python 3.

Additional information: http://doc.qt.io/qtcreator/creator-debugging-helpers.html
