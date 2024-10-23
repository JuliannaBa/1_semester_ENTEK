
from balance.ExitEnergy import ExitEnergy
from misc.CategoryFuelDistribution import CategoryFuelDistribution
from misc.constants.Fuel import FuelType

class TransportElectricityHeatOil:
    
    def __init__(self, key_figures : dict, exitEnergyBalance : ExitEnergy) -> None:
        self.exitEnergyBalance = exitEnergyBalance
        self.keyFigures = key_figures

        self.productionFuelDistribution = CategoryFuelDistribution()
        self.productionFuelDistribution.setFuelConsumption(FuelType.OIL_PRODUCTS, -1 * self.exitEnergyBalance.getFuelConsumption(FuelType.OIL_PRODUCTS))
        self.productionFuelDistribution.setFuelConsumption(FuelType.ELECTRICITY, -1 * self.exitEnergyBalance.getFuelConsumption(FuelType.ELECTRICITY))
        self.productionFuelDistribution.setFuelConsumption(FuelType.HEAT, -1 * self.exitEnergyBalance.getFuelConsumption(FuelType.HEAT))

        self.consumptionFuelDistribution = CategoryFuelDistribution()
        self.consumptionFuelDistribution.setFuelConsumption(FuelType.OIL_PRODUCTS, -1 * self.productionFuelDistribution.getFuelConsumption(FuelType.OIL_PRODUCTS))


        raise(Exception("Calculate the required electricity and heat production, taking losses into account..."))
    
        """
        Hint: The transport losses are given as a percentage of the consumption in the key figures...

        total_electricity_production = ?
        total_heat_production = ?
        """

        self.consumptionFuelDistribution.setFuelConsumption(FuelType.ELECTRICITY, total_electricity_production)
        self.consumptionFuelDistribution.setFuelConsumption(FuelType.HEAT, total_heat_production)
        
    def getFuelConsumption(self, fuel : FuelType) -> float:
        return self.consumptionFuelDistribution.getFuelConsumption(fuel)