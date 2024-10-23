

from misc.constants.EntryElectricityHeatOilCategories import EntryEnergyCategory
from balance.TransportElectricityHeatOil import TransportElectricityHeatOil
from misc.CategoryFuelDistribution import CategoryFuelDistribution
from misc.constants.Fuel import FuelType

class EntryElectricityHeatOil():
    
    def __init__(self, key_figures, transportElectricityHeatOil : TransportElectricityHeatOil) -> None:
        self.entry_key_figures = key_figures
        self.transportElectricityHeatOil = transportElectricityHeatOil

        self.categoryFuelDistribution = {}
        self.categoryFuelDistribution[EntryEnergyCategory.ENERGY_INDUSTRY] = self.__industryOwnUse(self.entry_key_figures['Entry energy']['Energy industry own use'])

        self.productionFuelDistribution = {}
        self.productionFuelDistribution[EntryEnergyCategory.ENERGY_INDUSTRY] = CategoryFuelDistribution()
        self.productionFuelDistribution[EntryEnergyCategory.CHP_PLANTS] = self.__CHPPlantsProduction()
        self.productionFuelDistribution[EntryEnergyCategory.HEAT_PLANTS] = self.__HeatPlantsProduction()

        self.categoryFuelDistribution[EntryEnergyCategory.HEAT_PLANTS] = self.__HeatPlantsConsumption(self.productionFuelDistribution[EntryEnergyCategory.HEAT_PLANTS])
        self.productionFuelDistribution[EntryEnergyCategory.ELECTRICITY_ONLY_PLANTS] = self.__ElectricityOnlyPlantsProduction(self.productionFuelDistribution[EntryEnergyCategory.CHP_PLANTS])
        
        self.categoryFuelDistribution[EntryEnergyCategory.ELECTRICITY_ONLY_PLANTS] = self.__ElectricityOnlyPlantsConsumption(self.productionFuelDistribution[EntryEnergyCategory.ELECTRICITY_ONLY_PLANTS])
        self.categoryFuelDistribution[EntryEnergyCategory.CHP_PLANTS] = self.__CHPPlantsConsumption(self.productionFuelDistribution[EntryEnergyCategory.CHP_PLANTS])

        self.productionFuelDistribution[EntryEnergyCategory.OIL_REFINERIES] = self.__OilRefineriesProduction(self.getFuelConsumption(FuelType.OIL_PRODUCTS))
        self.categoryFuelDistribution[EntryEnergyCategory.OIL_REFINERIES] = self.__OilRefineriesConsumption(self.productionFuelDistribution[EntryEnergyCategory.OIL_REFINERIES])


    def __OilRefineriesProduction(self, oilProductsConsumption : float) -> CategoryFuelDistribution:
        
        _totalOilProduction = oilProductsConsumption + self.transportElectricityHeatOil.getFuelConsumption(FuelType.OIL_PRODUCTS)

        _fuelDistribution = CategoryFuelDistribution()
        
        _fuelDistribution.setFuelConsumption(FuelType.OIL_PRODUCTS, _totalOilProduction)
        
        return _fuelDistribution
    
    def __OilRefineriesConsumption(self, OilRefineriesProductionFuelDistribution : CategoryFuelDistribution) -> CategoryFuelDistribution:
        
        _totalOilConsumption = OilRefineriesProductionFuelDistribution.getFuelConsumption(FuelType.OIL_PRODUCTS) / self.entry_key_figures['Entry energy']['Thermal plant efficiencies']['Oil refineries']

        _fuelDistribution = CategoryFuelDistribution()
        
        _fuelDistribution.setFuelConsumption(FuelType.CRUDE_OIL, _totalOilConsumption)
        
        return _fuelDistribution
    
    def __ElectricityOnlyPlantsProduction(self, CHPCategoryProductionFuelDistribution : CategoryFuelDistribution) -> CategoryFuelDistribution:
        
        _consumptionSide = -1 * (self.transportElectricityHeatOil.getFuelConsumption(FuelType.ELECTRICITY) + self.getFuelConsumption(FuelType.ELECTRICITY))

        _electricityProduction = CHPCategoryProductionFuelDistribution.getFuelConsumption(FuelType.ELECTRICITY)

        raise(Exception("Calculate the required production on electricity only plants..."))
    
        """
        Hint: Electricity not produced on CHP plants must come from somewhere else...

        _electricityOnlyPlantsProduction = ?
        """

        _electricityOnlyPlantsProduction = _consumptionSide - _electricityProduction

        _fuelDistribution = CategoryFuelDistribution()
        _fuelDistribution.setFuelConsumption(FuelType.ELECTRICITY, _electricityOnlyPlantsProduction)

        return _fuelDistribution
    
    def __ElectricityOnlyPlantsConsumption(self, electricityOnlyPlantsProduction : CategoryFuelDistribution) -> CategoryFuelDistribution:
        
        _hydroShare = -1 * electricityOnlyPlantsProduction.getFuelConsumption(FuelType.ELECTRICITY) * self.entry_key_figures['Entry energy']['Electricity only fuel share']['Hydro']
        _windSolarShare = -1 * electricityOnlyPlantsProduction.getFuelConsumption(FuelType.ELECTRICITY) * self.entry_key_figures['Entry energy']['Electricity only fuel share']['Wind, solar, etc.']

        _combinedFuelShare = (electricityOnlyPlantsProduction.getFuelConsumption(FuelType.ELECTRICITY) 
                              + _hydroShare 
                              + _windSolarShare)/self.entry_key_figures['Entry energy']['Thermal plant efficiencies']['Electricity plants']
        
        _coalShare = -1 * (_combinedFuelShare * self.entry_key_figures['Entry energy']['Fuel distribution']['Electricity plants']['Coal'])


        raise(Exception("Use the _combinedFuelShare to calculate the energy shares on the different fuels..."))
    
        """
        Hint: Missing fuels:

        _hydroShare = ?
        _windSolarShare = ?
        _coalShare = ?
        _crudeOilShare = ?
        _oilProductsShare = ?
        _naturalGasShare = ?
        _nuclearShare = ?
        _biofuelsShare = ?
        """

        _fuelDistribution = CategoryFuelDistribution()
        _fuelDistribution.setFuelConsumption(FuelType.HYDRO, _hydroShare)
        _fuelDistribution.setFuelConsumption(FuelType.WIND_SOLAR_ETC, _windSolarShare)
        _fuelDistribution.setFuelConsumption(FuelType.COAL, _coalShare)
        _fuelDistribution.setFuelConsumption(FuelType.CRUDE_OIL, _crudeOilShare)
        _fuelDistribution.setFuelConsumption(FuelType.OIL_PRODUCTS, _oilProductsShare)
        _fuelDistribution.setFuelConsumption(FuelType.NATURAL_GAS, _naturalGasShare)
        _fuelDistribution.setFuelConsumption(FuelType.NUCLEAR, _nuclearShare)
        _fuelDistribution.setFuelConsumption(FuelType.BIOFUELS_AND_WASTE, _biofuelsShare)

        return _fuelDistribution
    
    def __CHPPlantsConsumption(self, CHPCategoryProductionFuelDistribution : CategoryFuelDistribution) -> CategoryFuelDistribution:

        _windSolarShare = -1 * CHPCategoryProductionFuelDistribution.getFuelConsumption(FuelType.ELECTRICITY) * self.entry_key_figures['Entry energy']['CHP fuel share']['Wind, solar, etc.']

        _combinedFuelShare = (CHPCategoryProductionFuelDistribution.getFuelConsumption(FuelType.ELECTRICITY) 
                              + CHPCategoryProductionFuelDistribution.getFuelConsumption(FuelType.HEAT) 
                              + _windSolarShare)/self.entry_key_figures['Entry energy']['Thermal plant efficiencies']['CHP plants']

        _coalShare = -1 * (_combinedFuelShare * self.entry_key_figures['Entry energy']['Fuel distribution']['CHP plants']['Coal'])
        
        
        raise(Exception("Use the _combinedFuelShare to calculate the energy shares on the different fuels..."))
    
        """
        Hint: Missing fuels:

        _windSolarShare = ?
        _coalShare = ?
        _crudeOilShare = ?
        _oilProductsShare = ?
        _naturalGasShare = ?
        _nuclearShare = ?
        _biofuelsShare = ?
        """

        _fuelDistribution = CategoryFuelDistribution()
        _fuelDistribution.setFuelConsumption(FuelType.HYDRO, 0)
        _fuelDistribution.setFuelConsumption(FuelType.WIND_SOLAR_ETC, _windSolarShare)
        _fuelDistribution.setFuelConsumption(FuelType.COAL, _coalShare)
        _fuelDistribution.setFuelConsumption(FuelType.CRUDE_OIL, _crudeOilShare)
        _fuelDistribution.setFuelConsumption(FuelType.OIL_PRODUCTS, _oilProductsShare)
        _fuelDistribution.setFuelConsumption(FuelType.NATURAL_GAS, _naturalGasShare)
        _fuelDistribution.setFuelConsumption(FuelType.NUCLEAR, _nuclearShare)
        _fuelDistribution.setFuelConsumption(FuelType.BIOFUELS_AND_WASTE, _biofuelsShare)

        return _fuelDistribution

    def __CHPPlantsProduction(self) -> CategoryFuelDistribution:
        
        _totalHeatProduction = -1 * (self.transportElectricityHeatOil.getFuelConsumption(FuelType.HEAT) + self.getCategoryFuelConsumption(EntryEnergyCategory.ENERGY_INDUSTRY, FuelType.HEAT))
        
        raise(Exception("Calculate the heat production on CHP plants based on _totalHeatProduction and the key figures..."))
    
        """
        Hint: 

        _heatProduction = ?
        _electricityProduction = ?

        Remember the electricity production on CHP plants can be calculated from the heat production using the cm-value

        """

        _fuelDistribution = CategoryFuelDistribution()
        
        _fuelDistribution.setFuelConsumption(FuelType.HEAT, _heatProduction)
        _fuelDistribution.setFuelConsumption(FuelType.ELECTRICITY, _electricityProduction)

        return _fuelDistribution
    
    def __HeatPlantsProduction(self) -> CategoryFuelDistribution:
        
        _totalHeatProduction = -1 * (self.transportElectricityHeatOil.getFuelConsumption(FuelType.HEAT) + self.getCategoryFuelConsumption(EntryEnergyCategory.ENERGY_INDUSTRY, FuelType.HEAT))
        
        _fuelDistribution = CategoryFuelDistribution()
        
        _fuelDistribution.setFuelConsumption(FuelType.HEAT, _totalHeatProduction * self.entry_key_figures['Entry energy']['Heat production distribution']['Heat plants'])

        return _fuelDistribution


    def __HeatPlantsConsumption(self, heatPlantProductionFuelDistribution : CategoryFuelDistribution) -> CategoryFuelDistribution:
        
        _fuelDistribution = CategoryFuelDistribution()

        _fuelDistribution.setFuelConsumption(FuelType.ELECTRICITY, -1 * heatPlantProductionFuelDistribution.getFuelConsumption(FuelType.HEAT) * self.entry_key_figures['Entry energy']['Electricity consumption on heat plants']['Share of heat production on Heat plants'])

        _windSolarShare = -1 * heatPlantProductionFuelDistribution.getFuelConsumption(FuelType.HEAT) * self.entry_key_figures['Entry energy']['Heat plants fuel share']['Wind, solar, etc.']

        _combinedFuelShare = (heatPlantProductionFuelDistribution.getFuelConsumption(FuelType.HEAT) 
                              + _windSolarShare)/self.entry_key_figures['Entry energy']['Thermal plant efficiencies']['Heat plants']

        _coalShare = -1 * (_combinedFuelShare * self.entry_key_figures['Entry energy']['Fuel distribution']['Heat plants']['Coal'])

        raise(Exception("Use the _combinedFuelShare to calculate the energy shares on the different fuels..."))
    
        """
        Hint: Missing fuels:

        _crudeOilShare = ?
        _oilProductsShare = ?
        _naturalGasShare = ?
        _nuclearShare = ?
        _biofuelsShare = ?
        """

        _fuelDistribution.setFuelConsumption(FuelType.HYDRO, 0)
        _fuelDistribution.setFuelConsumption(FuelType.WIND_SOLAR_ETC, _windSolarShare)
        _fuelDistribution.setFuelConsumption(FuelType.COAL, _coalShare)
        _fuelDistribution.setFuelConsumption(FuelType.CRUDE_OIL, _crudeOilShare)
        _fuelDistribution.setFuelConsumption(FuelType.OIL_PRODUCTS, _oilProductsShare)
        _fuelDistribution.setFuelConsumption(FuelType.NATURAL_GAS, _naturalGasShare)
        _fuelDistribution.setFuelConsumption(FuelType.NUCLEAR, _nuclearShare)
        _fuelDistribution.setFuelConsumption(FuelType.BIOFUELS_AND_WASTE, _biofuelsShare)

        return _fuelDistribution

    def __industryOwnUse(self, energy_industry_key_figures) -> CategoryFuelDistribution:
        
        categoryTotalConsumption = energy_industry_key_figures['Share of total final consumption'] * self.entry_key_figures['Total final consumption']
        
        fuelDistribution = CategoryFuelDistribution()
        
        _coal_share = energy_industry_key_figures['Share of energyforms']['Coal'] * categoryTotalConsumption
        raise(Exception("Calculate the energy share for the other fuel types..."))
    
        """
        Hint: Missing fuels:

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

        #print(fuelDistribution)

        return fuelDistribution
    
    def getFuelConsumption(self, fuel : FuelType) -> float:

        _consumption = 0

        for category in self.categoryFuelDistribution.keys():

            try:
                _consumption = _consumption + self.categoryFuelDistribution[category].getFuelConsumption(fuel)
            except:
                return _consumption
        
        return _consumption
    
    def getTotalConsumption(self) -> float:

        _consumption = 0

        for category in self.categoryFuelDistribution:
            _consumption = _consumption + self.categoryFuelDistribution[category].getCategoryFuelConsumption()

        return _consumption


    def getCategoryTotalConsumption(self, category: EntryEnergyCategory) -> float:

        return self.categoryFuelDistribution[category].getCategoryFuelConsumption()


    def getCategoryFuelConsumption(self, category: EntryEnergyCategory, fuel: FuelType) -> float:

        return self.categoryFuelDistribution[category].getFuelConsumption(fuel)
    
    def getCategoryFuelProduction(self, category: EntryEnergyCategory, fuel: FuelType) -> float:

        return self.productionFuelDistribution[category].getFuelConsumption(fuel)