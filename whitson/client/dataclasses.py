from dataclasses import dataclass
from datetime import datetime
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
    # TODO: Are any of these required for analysis?
    Sw_i: Union[float, None] = None
    bothole_lat: Union[float, None] = None
    bothole_long: Union[float, None] = None
    bounded: Union[str, None] = None
    clusters: Union[int, None] = None
    county: Union[str, None] = None
    cr: Union[float, None] = None
    created: Union[str, None] = None
    custom_attributes: Union[dict, None] = None  # guessed this type
    external_id: Union[str, None] = None
    fluid_pumped: Union[float, None] = None
    gamma_f: Union[float, None] = None
    gamma_m: Union[float, None] = None
    groups: Union[list, None] = None  # guessed this type
    h: Union[float, None] = None
    h_f: Union[float, None] = None
    id: Union[int, None] = None  # Whitson well id
    l_w: Union[float, None] = None
    n_f: Union[float, None] = None
    name: Union[str, None] = None
    note: Union[str, None] = None
    p_res_i: Union[float, None] = None
    phi: Union[float, None] = None
    process_id: Union[int, None] = None
    project_id: Union[int, None] = None
    prop_pumped: Union[float, None] = None
    reservoir: Union[str, None] = None
    salinity: Union[float, None] = None
    spacing: Union[float, None] = None
    stages: Union[int, None] = None
    state: Union[str, None] = None
    surf_lat: Union[float, None] = None
    surf_long: Union[float, None] = None
    t_res: Union[float, None] = None
    uwi_api: Union[str, None] = None  # Ovintiv License Number

    def __post_init__(self):
        # Check to see if bounded parameter has correct values
        well_classification = ("bounded", "unbounded", "half-bounded")
        if self.bounded not in well_classification:
            return ValueError(
                f"Value for 'bounded' ({self.bounded}) is not one of: {well_classification}"
            )

        # TODO: Change created to a datetime format


@dataclass
class ProductionData:
    well_id: str
    qg_sc: list[tuple[datetime, Union[float, None]]]
    gor_sep: list[tuple[datetime, Union[float, None]]]
    qg_sep: list[tuple[datetime, Union[float, None]]]
    qo_sc: list[tuple[datetime, Union[float, None]]]
    qg_gas_lift: list[tuple[datetime, Union[float, None]]]
    gor_sc: list[tuple[datetime, Union[float, None]]]
    liquid_level: list[tuple[datetime, Union[float, None]]]
    p_tubing: list[tuple[datetime, Union[float, None]]]
    p_casing: list[tuple[datetime, Union[float, None]]]
    choke_size: list[tuple[datetime, Union[float, None]]]
    qo_sep: list[tuple[datetime, Union[float, None]]]
    p_sep: list[tuple[datetime, Union[float, None]]]
    qw_sc: list[tuple[datetime, Union[float, None]]]
    t_sep: list[tuple[datetime, Union[float, None]]]
    qw_sep: list[tuple[datetime, Union[float, None]]]
    p_wf_measured: list[tuple[datetime, Union[float, None]]]
