
from enum import Enum

class EntryEnergyCategory(Enum):
    ELECTRICITY_ONLY_PLANTS = 0
    CHP_PLANTS = 1
    HEAT_PLANTS = 2
    OIL_REFINERIES = 3
    ENERGY_INDUSTRY = 4