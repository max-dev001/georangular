# AUTOGENERATED BY NBDEV! DO NOT EDIT!

__all__ = ["index", "modules", "custom_doc_links", "git_url"]

index = {
    "logger": "01_validation.ipynb",
    "SquareGridBoundary": "00_grids.ipynb",
    "SquareGridGenerator": "00_grids.ipynb",
    "SquareGridGenerator.create_cell": "00_grids.ipynb",
    "SquareGridGenerator.create_grid_for_polygon": "00_grids.ipynb",
    "SquareGridGenerator.generate_grid": "00_grids.ipynb",
    "H3GridGenerator": "00_grids.ipynb",
    "H3GridGenerator.get_hexes_for_polygon": "00_grids.ipynb",
    "H3GridGenerator.generate_grid": "00_grids.ipynb",
    "BingTileGridGenerator": "00_grids.ipynb",
    "BingTileGridGenerator.generate_grid": "00_grids.ipynb",
    "ValidationError": "01_validation.ipynb",
    "BaseValidator": "01_validation.ipynb",
    "BaseValidator.validate": "01_validation.ipynb",
    "OrientationValidator": "01_validation.ipynb",
    "OrientationValidator.check": "01_validation.ipynb",
    "OrientationValidator.fix": "01_validation.ipynb",
    "CrsBoundsValidator": "01_validation.ipynb",
    "CrsBoundsValidator.get_check_arguments": "01_validation.ipynb",
    "CrsBoundsValidator.check": "01_validation.ipynb",
    "CrsBoundsValidator.fix": "01_validation.ipynb",
    "SelfIntersectingValidator": "01_validation.ipynb",
    "SelfIntersectingValidator.check": "01_validation.ipynb",
    "SelfIntersectingValidator.fix": "01_validation.ipynb",
    "NullValidator": "01_validation.ipynb",
    "NullValidator.check": "01_validation.ipynb",
    "NullValidator.fix": "01_validation.ipynb",
    "AreaValidator": "01_validation.ipynb",
    "AreaValidator.check": "01_validation.ipynb",
    "AreaValidator.fix": "01_validation.ipynb",
    "GeometryValidation": "01_validation.ipynb",
    "GeometryValidation.validate_all": "01_validation.ipynb",
    "GEO_INDEX_NAME": "02_vector_zonal_stats.ipynb",
    "create_zonal_stats": "02_vector_zonal_stats.ipynb",
    "tms": "02_vector_zonal_stats.ipynb",
    "get_quadkey": "02_vector_zonal_stats.ipynb",
    "compute_quadkey": "02_vector_zonal_stats.ipynb",
    "validate_aoi_quadkey": "02_vector_zonal_stats.ipynb",
    "validate_data_quadkey": "02_vector_zonal_stats.ipynb",
    "create_bingtile_zonal_stats": "02_vector_zonal_stats.ipynb",
    "create_raster_zonal_stats": "03_raster_zonal_stats.ipynb",
    "PH_COLUMN_CONFIG": "04_dhs.ipynb",
    "KH_COLUMN_CONFIG": "04_dhs.ipynb",
    "MM_COLUMN_CONFIG": "04_dhs.ipynb",
    "TL_COLUMN_CONFIG": "04_dhs.ipynb",
    "COLUMN_CONFIG": "04_dhs.ipynb",
    "load_column_config": "04_dhs.ipynb",
    "load_dhs_file": "04_dhs.ipynb",
    "apply_threshold": "04_dhs.ipynb",
    "assign_wealth_index": "04_dhs.ipynb",
    "DEFAULT_CACHE_DIR": "05_datasets_geofabrik.ipynb",
    "load_geofabrik_data": "05_datasets_geofabrik.ipynb",
    "list_geofabrik_regions": "05_datasets_geofabrik.ipynb",
    "get_osm_download_url": "05_datasets_geofabrik.ipynb",
    "get_download_filepath": "05_datasets_geofabrik.ipynb",
    "download_geofabrik_region": "05_datasets_geofabrik.ipynb",
    "download_osm_region_data": "05_datasets_geofabrik.ipynb",
    "OsmDataManager": "05_datasets_geofabrik.ipynb",
    "OsmDataManager.load_pois": "05_datasets_geofabrik.ipynb",
    "OsmDataManager.load_roads": "05_datasets_geofabrik.ipynb",
    "OoklaFile": "05_datasets_ookla.ipynb",
    "list_ookla_files": "05_datasets_ookla.ipynb",
    "download_ookla_file": "05_datasets_ookla.ipynb",
    "extract_func": "06_area_zonal_stats.ipynb",
    "fix_area_agg": "06_area_zonal_stats.ipynb",
    "get_source_column": "06_area_zonal_stats.ipynb",
    "INTERSECT_AREA_AGG": "06_area_zonal_stats.ipynb",
    "build_agg_area_dicts": "06_area_zonal_stats.ipynb",
    "validate_area_aoi": "06_area_zonal_stats.ipynb",
    "validate_area_data": "06_area_zonal_stats.ipynb",
    "expand_area_aggs": "06_area_zonal_stats.ipynb",
    "compute_intersect_stats": "06_area_zonal_stats.ipynb",
    "compute_imputed_stats": "06_area_zonal_stats.ipynb",
    "create_area_zonal_stats": "06_area_zonal_stats.ipynb",
    "build_agg_distance_dicts": "07_distance_zonal_stats.ipynb",
    "INTERNAL_DISTANCE_COL": "07_distance_zonal_stats.ipynb",
    "create_distance_zonal_stats": "07_distance_zonal_stats.ipynb",
    "TileClustering": "08_tile_clustering.ipynb",
    "TileClustering.cluster_tiles": "08_tile_clustering.ipynb",
    "query_window_by_polygon": "09_raster_process.ipynb",
    "query_window_by_gdf": "09_raster_process.ipynb",
    "generate_mask": "10_vector_to_raster_mask.ipynb",
    "GRID_ID": "10_vector_to_raster_mask.ipynb",
    "read_bands": "11_raster_to_dataframe.ipynb",
    "get_highest_intersection": "12_spatialjoin_highest_intersection.ipynb",
    "urlretrieve": "13_datasets_utils.ipynb",
    "make_report_hook": "13_datasets_utils.ipynb",
}

modules = [
    "grids.py",
    "validation.py",
    "vector_zonal_stats.py",
    "raster_zonal_stats.py",
    "dhs.py",
    "datasets/geofabrik.py",
    "datasets/ookla.py",
    "area_zonal_stats.py",
    "distance_zonal_stats.py",
    "tile_clustering.py",
    "raster_process.py",
    "vector_to_raster_mask.py",
    "raster_to_dataframe.py",
    "spatialjoin_highest_intersection.py",
    "datasets/utils.py",
]

doc_url = "https://geowrangler.thinkingmachin.es/"

git_url = "https://github.com/thinkingmachines/geowrangler/tree/master/"


def custom_doc_links(name):
    return None
