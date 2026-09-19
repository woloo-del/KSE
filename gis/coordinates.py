"""Explicit offline longitude/latitude -> Polish metric CRS adapter."""
import math

import pyproj
from pyproj import CRS, Transformer
from shapely.geometry.base import BaseGeometry
from shapely.ops import transform


class PolishMetricProjection:
    def __init__(self) -> None:
        self.area = CRS('EPSG:2180').area_of_use
        self.forward = Transformer.from_crs('EPSG:4326', 'EPSG:2180', always_xy=True,
                                            allow_ballpark=False, only_best=True)
        self.inverse = Transformer.from_crs('EPSG:2180', 'EPSG:4326', always_xy=True,
                                            allow_ballpark=False, only_best=True)
        # Fail rather than silently depend on remotely downloaded transformation grids.
        if self.forward.is_network_enabled or self.inverse.is_network_enabled:
            raise ValueError('PROJ_NETWORK_MUST_BE_DISABLED')

    def project(self, geometry: BaseGeometry) -> BaseGeometry:
        if geometry.is_empty or not geometry.is_valid or geometry.has_z:
            raise ValueError('INVALID_GEOGRAPHIC_GEOMETRY')
        west, south, east, north = geometry.bounds
        if not all(math.isfinite(v) for v in geometry.bounds) or not (
            self.area.west <= west <= east <= self.area.east and
            self.area.south <= south <= north <= self.area.north
        ):
            raise ValueError('OUTSIDE_CRS_AREA_OR_SWAPPED_AXES')
        result = transform(lambda x, y: self.forward.transform(x, y, errcheck=True), geometry)
        if result.is_empty or not result.is_valid or not all(math.isfinite(v) for v in result.bounds):
            raise ValueError('INVALID_PROJECTED_GEOMETRY')
        return result

    def geographic(self, geometry: BaseGeometry) -> BaseGeometry:
        return transform(lambda x, y: self.inverse.transform(x, y, errcheck=True), geometry)

    def metadata(self) -> dict:
        return {'source_crs': 'EPSG:4326', 'target_crs': 'EPSG:2180', 'always_xy': True,
                'allow_ballpark': False, 'network_enabled': False,
                'pyproj': pyproj.__version__, 'proj': pyproj.proj_version_str,
                'pipeline': self.forward.definition, 'accuracy_m_reported_by_proj': self.forward.accuracy,
                'note': 'Transformation accuracy is not source geometry accuracy.'}
