from dataclasses import dataclass
from typing import Union

from dacite import from_dict


@dataclass
class Project:
    id: Union[int, None] = None
    name: Union[str, None] = None
    company_wide: Union[bool, None] = None
    owner: Union[str, None] = None
    well_groups: Union[dict, None] = None
    custom_attributes: Union[dict, None] = None
    note: Union[str, None] = None
    well_count: Union[int, None] = None
    analysis_count: Union[int, None] = None


@dataclass
class Field:
    name: Union[str, None] = None
    id: Union[int, None] = None
    projects: Union[list, None] = None

    def __post_init__(self):
        if self.projects:
            self.projects = [
                from_dict(data=p, data_class=Project) for p in self.projects
            ]


@dataclass
class Well:
    name: Union[str, None] = None
    id: Union[int, None] = None

    {
        "Sw_i": 35.47724393292561,
        "bothole_lat": 55.109579999999994,
        "bothole_long": -119.34174,
        "bounded": "bounded",
        "clusters": None,
        "county": "07009W60",
        "cr": 4e-06,
        "created": "2023-07-07T04:26:54",
        "custom_attributes": None,
        "external_id": None,
        "fluid_pumped": 29081.565516000002,
        "gamma_f": 0.0,
        "gamma_m": 0.0,
        "groups": None,
        "h": 164.05,
        "h_f": 164.05,
        "id": 227045,
        "l_w": 4106.9555119999995,
        "n_f": 100.0,
        "name": "A01-32-070-09W6",
        "note": None,
        "p_res_i": 4482.93447673951,
        "phi": 0.0289740754782467,
        "process_id": 12,
        "project_id": 159,
        "prop_pumped": 3039725.64676,
        "reservoir": "G",
        "salinity": 0.0,
        "spacing": None,
        "stages": 11,
        "state": "1-32-70-9W6 PAD",
        "surf_lat": 55.09881,
        "surf_long": -119.32231,
        "t_res": 187.76821850857257,
        "uwi_api": "406344",
    }
