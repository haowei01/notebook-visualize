import folium
import s2sphere as s2


def s2cell_to_polygon(s2cell) -> list:
    poly = []
    for i in list(range(4)) + [0]:
        v = s2.LatLng.from_point(s2cell.get_vertex(i))
        poly.append((v.lat().degrees, v.lng().degrees))
    return poly


def plot_s2cell(s2cell_id: int):
    s2cell = s2.Cell(s2.CellId(s2cell_id))
    center = s2.LatLng.from_point(s2cell.get_center())
    m = folium.Map(location=[center.lat().degrees, center.lng().degrees])
    folium.PolyLine(s2cell_to_polygon(s2cell)).add_to(m)
    return m


def s2cell_id_from_lat_lng(lat: float, lng: float, level: int) -> int:
    """Get S2cell id from lat degree, lng degree, and level."""
    s2_cell_id = s2.Cell.from_lat_lng(s2.LatLng.from_degrees(lat, lng)).id()
    return s2_cell_id.parent(level).id()

m = plot_s2cell(9290064014149156864)
m.save('plot_s2_cell.html')
