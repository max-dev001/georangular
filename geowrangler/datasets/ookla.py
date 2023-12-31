# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/05_datasets_ookla.ipynb (unless otherwise specified).

__all__ = ["list_ookla_files", "download_ookla_file"]


# Internal Cell
import os
import shutil
import xml.etree.ElementTree as ET
from collections import namedtuple
from functools import lru_cache
from pathlib import Path
from typing import List
from urllib.parse import urlparse

import requests

OoklaFile = namedtuple("OoklaQuarter", ["type", "year", "quarter"])

# Cell
@lru_cache(maxsize=None)
def list_ookla_files() -> dict:
    """Get list of ookla data"""
    # Query parquet files as they are easier to deal with then shapefiles
    resp = requests.get(
        "https://ookla-open-data.s3.us-west-2.amazonaws.com/?list-type=2&prefix=parquet"
    )
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    keys = {}
    # Get keys. This would require pagination once there are more than 1000 keys under the parquet folder
    # but that would only happen after ~125 years
    for child in root.findall("{http://s3.amazonaws.com/doc/2006-03-01/}Contents"):
        key = child.find("{http://s3.amazonaws.com/doc/2006-03-01/}Key").text
        path_key = Path(key)
        type_ = path_key.parts[2].rsplit("=")[-1]
        year = path_key.parts[3].rsplit("=")[-1]
        quarter = path_key.parts[4].rsplit("=")[-1]
        file = path_key.parts[5]
        keys.update({OoklaFile(type_, year, quarter): file})
    return keys


# Cell
def download_ookla_file(
    type_: str,  # Internet connection type: 'fixed' or 'mobile'
    year: str,  # Year (e.g. '2020')
    quarter: str,  # Quarter (valid values: '1','2','3','4')
    directory: str = "data/",  # Download directory
    overwrite: bool = False,  # Overwrite if existing
) -> List[Path]:
    """Download ookla file to path"""
    if not os.path.isdir(directory):
        os.makedirs(directory)
    ookla_info = list_ookla_files()
    key = OoklaFile(type_, str(year), str(quarter))
    if key not in ookla_info:
        raise ValueError(
            f"{key} not found in ookla. Run list_ookla_data() to learn more about available files"
        )
    file = ookla_info[key]
    url = f"https://ookla-open-data.s3.us-west-2.amazonaws.com/parquet/performance/type={type_}/year={year}/quarter={quarter}/{file}"
    parsed_url = urlparse(url)
    filename = Path(os.path.basename(parsed_url.path))
    filepath = directory / filename
    if not filepath.exists() or overwrite:
        response = requests.get(url, stream=True)
        with open(filepath, "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
    return filepath
