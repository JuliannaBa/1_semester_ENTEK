
from misc.constants.ExitEnergyCategories import ExitEnergyCategory
from misc.constants.Fuel import FuelType
from misc.CategoryFuelDistribution import CategoryFuelDistribution

class ExitEnergy():
    
    def __init__(self, key_figures: dict) -> None:
        self.key_figures = key_figures
        self.totalFinalConsumption = self.key_figures['Total final consumption']
        self.categoryFuelDistribution = {}
        
        self.categoryFuelDistribution[ExitEnergyCategory.INDUSTRY] = self.__setCategoryFuelConsumption(self.key_figures['Exit energy']['Industry'])
        self.categoryFuelDistribution[ExitEnergyCategory.TRANSPORT] = self.__setCategoryFuelConsumption(self.key_figures['Exit energy']['Transport'])
        self.categoryFuelDistribution[ExitEnergyCategory.RESIDENTIAL] = self.__setCategoryFuelConsumption(self.key_figures['Exit energy']['Residential'])
        self.categoryFuelDistribution[ExitEnergyCategory.COMMERCIAL] = self.__setCategoryFuelConsumption(self.key_figures['Exit energy']['Commercial and public services'])
        self.categoryFuelDistribution[ExitEnergyCategory.AGRICULTURE] = self.__setCategoryFuelConsumption(self.key_figures['Exit energy']['Agriculture / forestry'])
        self.categoryFuelDistribution[ExitEnergyCategory.FISHING] = self.__setCategoryFuelConsumption(self.key_figures['Exit energy']['Fishing'])
        self.categoryFuelDistribution[ExitEnergyCategory.NON_SPECIFIED] = self.__setCategoryFuelConsumption(self.key_figures['Exit energy']['Non-specified'])

    def __setCategoryFuelConsumption(self, exit_key_figures : dict) -> CategoryFuelDistribution:
        
        # Calculate the category-specific total consumption
        categoryTotalConsumption = exit_key_figures['Share of total final consumption']*self.totalFinalConsumption
        

        # Divide the consumption into categories using your key-figures
        fuelDistribution = CategoryFuelDistribution()

        _coal_share = exit_key_figures['Share of energyforms']['Coal'] * categoryTotalConsumption


        raise(Exception("Continue the calculations on the exit energy fuel shares for a given category..."))
    
        """
        Hint: Missing fuel types:

        _crude_oil_share = ?
        _oil_products_share = ?
        _natural_gas_share = ?
        _nuclear_share = ?
        _hydro_share = ?
        _wind_solar_etc_share = ?
        _biofuels_and_waste_share = ?
        _electricity_share = ?
        _heat_share = ?
        """

        fuelDistribution.setFuelConsumption(FuelType.COAL, _coal_share)
        fuelDistribution.setFuelConsumption(FuelType.CRUDE_OIL, _crude_oil_share)
        fuelDistribution.setFuelConsumption(FuelType.OIL_PRODUCTS, _oil_products_share)
        fuelDistribution.setFuelConsumption(FuelType.NATURAL_GAS, _natural_gas_share)
        fuelDistribution.setFuelConsumption(FuelType.NUCLEAR, _nuclear_share)
        fuelDistribution.setFuelConsumption(FuelType.HYDRO, _hydro_share)
        fuelDistribution.setFuelConsumption(FuelType.WIND_SOLAR_ETC, _wind_solar_etc_share)
        fuelDistribution.setFuelConsumption(FuelType.BIOFUELS_AND_WASTE, _biofuels_and_waste_share)
        fuelDistribution.setFuelConsumption(FuelType.ELECTRICITY, _electricity_share)
        fuelDistribution.setFuelConsumption(FuelType.HEAT, _heat_share)

        
        return fuelDistribution

    def getFuelConsumption(self, fuel : FuelType) -> float:
        _consumption = 0

        raise(Exception("Calculate the total consumption across all 'ExitEnergyCategory' fields for a given fuel"))

        """
        Hint: The fuel consumption for a given category an fuel is given by:
        self.categoryFuelDistribution[<INSERT CATEGORY>].getFuelConsumption(<INSERT FUEL>) method on each 

        """
        return _consumption

    def getExitEnergyTotalConsumption(self) -> float:

        _consumption = 0

        for category in self.categoryFuelDistribution:
            _consumption = _consumption + self.categoryFuelDistribution[category].getCategoryFuelConsumption()

        return _consumption


    def getCategoryTotalConsumption(self, category: ExitEnergyCategory) -> float:

        return self.categoryFuelDistribution[category].getCategoryFuelConsumption()


    def getCategoryFuelConsumption(self, category: ExitEnergyCategory, fuel: FuelType) -> float:

        return self.categoryFuelDistribution[category].getFuelConsumption(fuel)

    def toString(self) -> str :
        
        string = """
        Exit energy: {0} 
        """.format(self.categoryFuelDistribution)

        return string