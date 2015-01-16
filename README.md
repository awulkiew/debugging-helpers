# Debugging Helpers for QtCreator

![example](example.png)

Currently supported:

* Boost.Geometry
  * boost::geometry::model::box
  * boost::geometry::model::d2::point_xy
  * boost::geometry::model::linestring
  * boost::geometry::model::multi_point
  * boost::geometry::model::multi_linestring
  * boost::geometry::model::multi_polygon
  * boost::geometry::model::point
  * boost::geometry::model::polygon
  * boost::geometry::model::ring
  * boost::geometry::model::segment
* Boost.Tuple
  * boost::tuple
* Boost.Variant
  * boost::variant

Additional information:
http://doc.qt.io/qtcreator/creator-debugging-helpers.html

In
    ~/.gdbinit
or
    Tools > Options > Debugger > GDB > Additional Startup Commands
put
    python execfile('path_to_filename.py')
e.g.
    python execfile('/home/john/dh-boost-geometry.py')

