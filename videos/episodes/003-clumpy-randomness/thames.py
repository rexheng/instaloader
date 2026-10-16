"""Episode 3: the River Thames centreline for the real V-1 map.

Source: Ordnance Survey, OS Open Rivers (GeoPackage, GB, downloaded 2026-10-15 from
api.os.uk/downloads/v1/products/OpenRivers; zip md5 4b62effb1c7980f3320d400b76b4f4b0).
Open Government Licence v3: "Contains OS data (c) Crown copyright and database right 2026".
The data is already in British National Grid metres, the same grid as the V-1 sites.

    python3 thames.py /path/to/oprvrs_gb.gpkg      # writes thames_os_open_rivers.csv

Walks the tidal Thames main channel downstream through the watercourse_link network (by
start/end node), from Putney (E 521.3 km) to past Woolwich, and writes the vertices.
"""
import csv
import os
import sqlite3
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
START = (521347, 176289)          # first vertex of the main-channel link at Putney
STOP_E = 549000                   # stop once the channel passes this easting


def parse(blob):
    """GeoPackage geometry blob -> list of (x, y) for a (2D or Z) LineString."""
    env = (blob[3] >> 1) & 7
    w = blob[8 + {0: 0, 1: 32, 2: 48, 3: 48, 4: 64}[env]:]
    bo = "<" if w[0] == 1 else ">"
    typ = struct.unpack(bo + "I", w[1:5])[0]
    dim = 3 if typ in (1002, 0x80000002) else 2
    n = struct.unpack(bo + "I", w[5:9])[0]
    vals = struct.unpack(bo + "%dd" % (n * dim), w[9:9 + 8 * n * dim])
    return [(vals[i * dim], vals[i * dim + 1]) for i in range(n)]


def main(gpkg):
    c = sqlite3.connect(gpkg)
    q = """select w.fid, w.watercourse_name, w.start_node, w.end_node, w.geometry
           from watercourse_link w join rtree_watercourse_link_geometry r on w.fid = r.id
           where r.minx < 560000 and r.maxx > 512000 and r.miny < 190000 and r.maxy > 165000
           and w.form = 'tidalRiver'"""
    links, by_start = {}, {}
    for fid, name, s, e, g in c.execute(q):
        links[fid] = (name, s, e, parse(g))
        by_start.setdefault(s, []).append(fid)
    cur = next(f for f, v in links.items()
               if abs(v[3][0][0] - START[0]) < 2 and abs(v[3][0][1] - START[1]) < 2)
    pts, seen = list(links[cur][3]), {cur}
    while pts[-1][0] < STOP_E:
        nxt = [f for f in by_start.get(links[cur][2], []) if f not in seen]
        if not nxt:
            break
        # at a junction keep the named main channel (tributaries such as the Lea join here)
        nxt.sort(key=lambda f: (links[f][0] in ("River Lea", "Warpools Reach"), -len(links[f][3])))
        cur = nxt[0]
        seen.add(cur)
        pts += links[cur][3][1:]
    out = os.path.join(HERE, "thames_os_open_rivers.csv")
    with open(out, "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["easting", "northing"])
        for x, y in pts:
            wr.writerow([round(x, 1), round(y, 1)])
    print(f"{len(pts)} vertices, E {pts[0][0]:.0f} -> {pts[-1][0]:.0f}; wrote {out}")


if __name__ == "__main__":
    main(sys.argv[1])
