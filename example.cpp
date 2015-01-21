#include <boost/array.hpp>

#include <boost/container/static_vector.hpp>
#include <boost/container/vector.hpp>

#include <boost/geometry.hpp>
#include <boost/geometry/geometries/geometries.hpp>
#include <boost/geometry/index/rtree.hpp>
#include <boost/geometry/io/wkt/wkt.hpp>

#include <boost/ratio.hpp>

#include <boost/tuple/tuple.hpp>

#include <boost/variant.hpp>

int main()
{
    namespace bg = boost::geometry;
    namespace bgi = boost::geometry::index;

    typedef bg::model::point<double, 2, bg::cs::cartesian> point_t;
    typedef bg::model::polygon<point_t> polygon_t;
    typedef bg::model::multi_polygon<polygon_t> mpolygon_t;
    typedef bg::model::box<point_t> box_t;
    typedef bg::model::segment<point_t> segment_t;
    typedef bg::model::linestring<point_t> linestring_t;
    typedef bg::model::ring<point_t> ring_t;

    typedef boost::tuple<point_t, box_t, linestring_t> tuple_t;
    typedef boost::variant<point_t, box_t, linestring_t> variant_t;

    point_t point;
    box_t box;
    segment_t segment;
    linestring_t linestring;
    ring_t ring;
    polygon_t polygon;
    mpolygon_t mpolygon;

    bg::read_wkt("POINT(0 0)", point);
    bg::read_wkt("BOX(0 0, 1 1)", box);
    bg::read_wkt("SEGMENT(0 0, 1 1)", segment);
    bg::read_wkt("LINESTRING(0 0, 1 1, 2 2)", linestring);
    bg::read_wkt("POLYGON((0 0,0 5,5 0,0 0))", ring);
    bg::read_wkt("POLYGON((0 0,0 5,5 0,0 0),(1 1,2 1,1 2,1 1),(3 3,4 3,3 4,3 3))", polygon);
    bg::read_wkt("MULTIPOLYGON(((0 0,0 1,1 0,0 0)),((4 4,4 5,5 4,4 4)))", mpolygon);

    bg::model::referring_segment<point_t> ref_segment(point, point);

    bg::segment_ratio<int> sratio1;
    bg::segment_ratio<int> sratio2(5, 6);

    bg::segment_identifier seg_id(0, -1, 0, 1);

    bg::detail::overlay::turn_operation< bg::segment_ratio<int> > turn_op;
    bg::detail::overlay::turn_info<
        point_t, bg::segment_ratio<int> > turn_inf;

    bgi::detail::varray<point_t, 10> varray(5, point);

    bgi::rtree<point_t, bgi::linear<4, 2> > rtree;
    rtree.insert(point_t(0, 0));
    rtree.insert(point_t(1, 1));
    rtree.insert(point_t(2, 2));
    rtree.insert(point_t(3, 3));
    rtree.insert(point_t(4, 4));

    boost::array<int, 5> arr;

    boost::container::static_vector<int, 5> svec(5, 0);
    boost::container::vector<int> vec(5, 0);

    for ( int i = 0 ; i < 5 ; ++i )
    {
        arr[i] = svec[i] = vec[i] = i;
    }

    boost::rational<int> r1;
    boost::rational<int> r2(1);
    boost::rational<int> r3(2,3);

    tuple_t tuple = boost::make_tuple(point, box, linestring);

    variant_t variant0 = point;
    variant_t variant1 = box;
    variant_t variant2 = linestring;

    return 0;
}
