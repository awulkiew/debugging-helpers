# Debugging Helpers for QtCreator

![example](example.png)

Currently supported:

* Boost.Array
  * boost::array
* Boost.Container
  * boost::container::static_vector
  * boost::container::vector
* Boost.Geometry
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
* Boost.Rational
  * boost::rational
* Boost.Tuple
  * boost::tuple
* Boost.Variant
  * boost::variant

To use, specify the location of custom helpers in **Tools > Options > Debugger > Locals & Expressions > Extra Debugging Helpers**

Additional information: https://doc.qt.io/qtcreator/creator-debugging-helpers.html

Originally Developed for [QtCreator 3](QtCreator3), and may not work with newer versions.
Some of the Debugging Helpers are explicitly ported to [QtCreator 4](QtCreator4).
