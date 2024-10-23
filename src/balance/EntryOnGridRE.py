
from balance.EntryElectricityHeatOil import EntryElectricityHeatOil

from misc.CategoryFuelDistribution import CategoryFuelDistribution

from misc.constants.Fuel import FuelType

class EntryOnGridRE:
    def __init__(self, entryElectricityHeatOil : EntryElectricityHeatOil) -> None:
        self.entryElectricityHeatOil = entryElectricityHeatOil
        self.productionFuelDistribution = CategoryFuelDistribution()
        self.productionFuelDistribution.setFuelConsumption(FuelType.HYDRO, -1 * self.entryElectricityHeatOil.getFuelConsumption(FuelType.HYDRO))
        self.productionFuelDistribution.setFuelConsumption(FuelType.WIND_SOLAR_ETC, -1 * self.entryElectricityHeatOil.getFuelConsumption(FuelType.WIND_SOLAR_ETC))
    
    def getTotalConsumption(self) -> float:
        
        return self.productionFuelDistribution.getCategoryFuelConsumption()
