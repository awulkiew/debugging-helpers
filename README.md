# Debugging Helpers for QtCreator

![example](example.png)

Currently supported:

* Boost.Array
  * boost::array
* Boost.Container
  * boost::container::static_vector
  * boost::container::vector
* Boost.Geometry
  * boost::geometry::detail::overlay::turn_info
  * boost::geometry::detail::overlay::turn_operation
  * boost::geometry::detail::overlay::turn_operation_linear
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
  * boost::geometry::segment_identifier
  * boost::geometry::segment_ratio
  * boost::geometry::side_info
* Boost.Rational
  * boost::rational
* Boost.Tuple
  * boost::tuple
* Boost.Variant
  * boost::variant

To use, in **~/.gdbinit** or **QtCreator > Tools > Options > Debugger > GDB > Additional Startup Commands** put

```sh
python exec(open('path_to_filename.py').read())
```

if GDB was linked against python 3 or

```sh
python execfile('path_to_filename.py')
```

if GDB was linked against python 2.

Additional information: http://doc.qt.io/qtcreator/creator-debugging-helpers.html

Originally Developed for [QtCreator 3](QtCreator3), and may not work with newer versions.
Some of the Debugging Helpers are explicitly ported to [QtCreator 4](QtCreator4).
