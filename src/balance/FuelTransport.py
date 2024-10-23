
from balance.ExitEnergy import ExitEnergy
from balance.EntryElectricityHeatOil import EntryElectricityHeatOil
from misc.CategoryFuelDistribution import CategoryFuelDistribution
from misc.constants.Fuel import FuelType

class FuelTransport:
    
    def __init__(self, exitEnergy : ExitEnergy, entryElectricityHeatOil : EntryElectricityHeatOil) -> None:
        self.exitEnergy = exitEnergy
        self.entryElectricityHeatOil = entryElectricityHeatOil

        self.productionFuelDistribution = CategoryFuelDistribution()

        self.productionFuelDistribution.setFuelConsumption(FuelType.COAL, -1 * (self.exitEnergy.getFuelConsumption(FuelType.COAL) + self.entryElectricityHeatOil.getFuelConsumption(FuelType.COAL)))
        self.productionFuelDistribution.setFuelConsumption(FuelType.CRUDE_OIL, -1 * (self.exitEnergy.getFuelConsumption(FuelType.CRUDE_OIL) + self.entryElectricityHeatOil.getFuelConsumption(FuelType.CRUDE_OIL)))
        self.productionFuelDistribution.setFuelConsumption(FuelType.NATURAL_GAS, -1 * (self.exitEnergy.getFuelConsumption(FuelType.NATURAL_GAS) + self.entryElectricityHeatOil.getFuelConsumption(FuelType.NATURAL_GAS)))
        self.productionFuelDistribution.setFuelConsumption(FuelType.NUCLEAR, -1 * (self.exitEnergy.getFuelConsumption(FuelType.NUCLEAR) + self.entryElectricityHeatOil.getFuelConsumption(FuelType.NUCLEAR)))
        self.productionFuelDistribution.setFuelConsumption(FuelType.BIOFUELS_AND_WASTE, -1 * (self.exitEnergy.getFuelConsumption(FuelType.BIOFUELS_AND_WASTE) + self.entryElectricityHeatOil.getFuelConsumption(FuelType.BIOFUELS_AND_WASTE)))

        self.consumptionFuelDistribution = CategoryFuelDistribution()
        
        self.consumptionFuelDistribution.setFuelConsumption(FuelType.COAL, -1 * self.productionFuelDistribution.getFuelConsumption(FuelType.COAL))
        self.consumptionFuelDistribution.setFuelConsumption(FuelType.CRUDE_OIL, -1 * self.productionFuelDistribution.getFuelConsumption(FuelType.CRUDE_OIL))
        self.consumptionFuelDistribution.setFuelConsumption(FuelType.NATURAL_GAS, -1 * self.productionFuelDistribution.getFuelConsumption(FuelType.NATURAL_GAS))
        self.consumptionFuelDistribution.setFuelConsumption(FuelType.NUCLEAR, -1 * self.productionFuelDistribution.getFuelConsumption(FuelType.NUCLEAR))
        self.consumptionFuelDistribution.setFuelConsumption(FuelType.BIOFUELS_AND_WASTE, -1 * self.productionFuelDistribution.getFuelConsumption(FuelType.BIOFUELS_AND_WASTE))
    
    def getTotalConsumption(self) -> float:
        return self.consumptionFuelDistribution.getCategoryFuelConsumption()
    
    def getTotalProduction(self) -> float:
        return self.productionFuelDistribution.getCategoryFuelConsumption()