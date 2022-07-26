# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/03_raster_zonal_stats.ipynb (unless otherwise specified).

__all__ = ["create_raster_zonal_stats"]


# Cell


from pathlib import Path
from typing import Any, Dict, Union

import geopandas as gpd
import pandas as pd
import rasterstats as rs

from .vector_zonal_stats import _expand_aggs, _fillnas, _fix_agg

# Cell
def create_raster_zonal_stats(
    aoi: Union[  # The area of interest geodataframe, or path to the vector file
        str, gpd.GeoDataFrame
    ],
    data: Union[str, Path],  # The path to the raster data file
    aggregation: Dict[str, Any],  # a dict specifying the aggregation
    extra_args: Dict[  # extra arguments passed to `rasterstats.zonal_stats` method
        str, Any
    ] = dict(
        layer=0,
        band_num=1,
        nodata=None,
        affine=None,
        all_touched=False,
    ),
) -> gpd.GeoDataFrame:

    """Compute zonal stats with a vector areas of interest (aoi) from raster data sources.
    This is a thin layer  over the `zonal_stats` method from
    the `rasterstats` python package for compatibility with other geowrangler modules.
    see https://pythonhosted.org/rasterstats/manual.html#zonal-statistics"""
    fixed_agg = _fix_agg(aggregation)

    if "stats" in extra_args:
        extra_args.pop("stats")  # use aggregation

    if "geojson_out" in extra_args:
        extra_args.pop("geojson_out")  # never add features

    if "categorical" in extra_args:
        extra_args.pop("categorical")  # no use for categorical and categorical maps
    if "categorical_map" in extra_args:
        extra_args.pop("categorical_map")

    if "prefix" in extra_args:
        extra_args.pop("prefix")  # use agg['column'] as prefix

    if "add_stats" in extra_args:
        extra_args.pop("add_stats")  # always use stats only

    stats = fixed_agg["func"]
    prefix = fixed_agg["column"] + "_"

    renamed_columns = {
        f"{prefix}{func}": fixed_agg["output"][i]
        for (i, func) in enumerate(fixed_agg["func"])
        if f"{prefix}{func}" != fixed_agg["output"][i]
    }
    results_dict = rs.zonal_stats(
        vectors=aoi,
        raster=data,
        stats=stats,
        geojson_out=False,
        categorical=False,
        category_map=None,
        prefix=prefix,
        **extra_args,
    )

    results = pd.DataFrame.from_records(results_dict)
    results.rename(columns=renamed_columns, inplace=True)
    expanded_aggs = _expand_aggs([fixed_agg])

    if type(aoi) == str:
        aoi = gpd.read_file(aoi)

    _fillnas(expanded_aggs, results, aoi)

    aoi = aoi.merge(results, how="left", left_index=True, right_index=True)

    return aoi
