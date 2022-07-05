# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/00_grids.ipynb (unless otherwise specified).

__all__ = ["SquareGridBoundary", "SquareGridGenerator", "H3GridGenerator"]

# Internal Cell
import logging
from typing import List, Tuple, Union

import h3
import numpy as np
from fastcore.basics import patch
from geopandas import GeoDataFrame
from pandas import DataFrame
from pyproj import Transformer
from shapely.geometry import Polygon

logger = logging.getLogger(__name__)

# Cell


class SquareGridBoundary:
    """Reusing Boundary. x_min, y_min, x_max, and y_max are in the the target crs"""

    def __init__(self, x_min: float, y_min: float, x_max: float, y_max: float):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def get_range_subset(
        self, x_min: float, y_min: float, x_max: float, y_max: float, cell_size: float
    ) -> Tuple[float, List[float], float, List[float]]:
        """Returns a subset of grids from the orginal boundary based on the boundary and a grid size"""
        xrange = np.arange(self.x_min, self.x_max, cell_size)
        yrange = np.arange(self.y_min, self.y_max, cell_size)
        x_mask = (xrange >= x_min) & (xrange <= x_max + cell_size)
        y_mask = (yrange >= y_min) & (yrange <= y_max + cell_size)
        x_idx = np.flatnonzero(x_mask)
        x_idx_offset = None if len(x_idx) == 0 else x_idx[0]
        y_idx = np.flatnonzero(y_mask)
        y_idx_offset = None if len(y_idx) == 0 else y_idx[0]
        return (
            x_idx_offset,
            xrange[x_mask],
            y_idx_offset,
            yrange[y_mask],
        )


# Cell


class SquareGridGenerator:
    def __init__(
        self,
        cell_size: float,  # height and width of a square cell in meters
        grid_projection: str = "EPSG:3857",  # projection of grid output
        boundary: Union[SquareGridBoundary, List[float]] = None,  # original boundary
    ):
        self.cell_size = cell_size
        self.grid_projection = grid_projection
        self.boundary = boundary


# Cell


@patch
def create_cell(
    self: SquareGridGenerator,
    x: float,  # x coord of top left
    y: float,  # y coord of top left
) -> Polygon:
    """Create a square cell based on the top left coordinates and cell_size"""
    return Polygon(
        [
            (x, y),
            (x + self.cell_size, y),
            (x + self.cell_size, y + self.cell_size),
            (x, y + self.cell_size),
        ]
    )


# Cell


@patch
def generate_grid(self: SquareGridGenerator, gdf: GeoDataFrame) -> GeoDataFrame:
    reprojected_gdf = gdf.to_crs(self.grid_projection)
    if self.boundary is None:
        boundary = SquareGridBoundary(*reprojected_gdf.total_bounds)
    elif isinstance(self.boundary, SquareGridBoundary):
        boundary = self.boundary
    else:
        transformer = Transformer.from_crs(gdf.crs, reprojected_gdf.crs, always_xy=True)
        x_min, y_min = transformer.transform(self.boundary[0], self.boundary[1])
        x_max, y_max = transformer.transform(self.boundary[2], self.boundary[3])
        boundary = SquareGridBoundary(x_min, y_min, x_max, y_max)

    # TODO: Catch case where no geometries are within the boundary
    x_idx_offset, xrange, y_idx_offset, yrange = boundary.get_range_subset(
        *reprojected_gdf.total_bounds, cell_size=self.cell_size
    )
    polygons = []
    for x_idx, x in enumerate(xrange):
        for y_idx, y in enumerate(yrange):
            polygons.append(
                {
                    "x": x_idx + x_idx_offset,
                    "y": y_idx + y_idx_offset,
                    "geometry": self.create_cell(x, y),
                }
            )
    # Catch case where no cell intersect with the aoi
    if polygons:
        dest = GeoDataFrame(polygons, geometry="geometry", crs=self.grid_projection)
        dest_reproject = dest.to_crs(gdf.crs)
        final = dest_reproject[dest_reproject.intersects(gdf.unary_union)]
        return final
    else:
        return GeoDataFrame(
            {"x": [], "y": [], "geometry": []}, geometry="geometry", crs=gdf.crs
        )


# Cell
class H3GridGenerator:
    def __init__(
        self,
        resolution: int,  # Resolution of hexagon. See: https://h3geo.org/docs/core-library/restable/ for more info
        return_geometry: bool = True,  # If geometry should be returned. Setting this to false will only return hex_ids
    ):
        self.resolution = resolution
        self.return_geometry = return_geometry


# Cell
@patch
def get_hexes_for_polygon(self: H3GridGenerator, poly: Polygon):
    return h3.polyfill(
        poly.__geo_interface__,
        self.resolution,
        geo_json_conformant=True,
    )


# Cell
@patch
def generate_grid(self: H3GridGenerator, gdf: GeoDataFrame) -> DataFrame:
    reprojected_gdf = gdf.to_crs("epsg:4326")  # h3 hexes are in epsg:4326 CRS
    hex_ids = set()
    unary_union = reprojected_gdf.unary_union
    if isinstance(unary_union, Polygon):
        hex_ids.update(self.get_hexes_for_polygon(unary_union))
    else:
        for geom in reprojected_gdf.unary_union.geoms:
            _hexes = self.get_hexes_for_polygon(geom)
            hex_ids.update(_hexes)
    df = DataFrame({"hex_id": list(hex_ids)})
    if self.return_geometry is False:
        return df
    hexes = df.hex_id.apply(
        lambda id: Polygon(h3.h3_to_geo_boundary(id, geo_json=True))
    )
    h3_gdf = GeoDataFrame(
        df,
        geometry=hexes,
        crs="epsg:4326",
    )
    h3_gdf.set_crs(gdf.crs)
    return h3_gdf
