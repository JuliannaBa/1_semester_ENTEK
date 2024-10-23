from balance.ExitEnergy import ExitEnergy
from misc.CategoryFuelDistribution import CategoryFuelDistribution
from misc.constants.Fuel import FuelType

class EntryOffGridRE():

    def __init__(self, exitEnergyBalance : ExitEnergy) -> None:
        self.productionFuelDistribution = CategoryFuelDistribution()
        self.productionFuelDistribution.setFuelConsumption(FuelType.WIND_SOLAR_ETC, -1 * exitEnergyBalance.getFuelConsumption(FuelType.WIND_SOLAR_ETC))
    