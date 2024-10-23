
from balance.ExitEnergy import ExitEnergy
from balance.EntryElectricityHeatOil import EntryElectricityHeatOil
from balance.EntryOffGridRE import EntryOffGridRE
from balance.TransportElectricityHeatOil import TransportElectricityHeatOil
from balance.EntryOnGridRE import EntryOnGridRE
from balance.FuelTransport import FuelTransport
from balance.EntryFuels import EntryFuels
from misc.constants.Fuel import FuelType
from misc.CarbonEquivalentCoefficients import EmissionFactor

class EnergyBalance():
    
    def __init__(self, key_figures : dict, year):
        
        self.key_figures = key_figures
        self.year = year
        self._co2Emissions = 0

        self.__initialize()
    
    def __initialize(self):
        print("Loading energy balance model for year {}".format(self.year))
        print("----------------------------")
        self.__setExitEnergyConsumption()
        print("Exit energy OK")
        self.__setOffGridRenewables()
        print("Off grid renewables OK")
        self.__setTransportElectricityHeatOil()
        print("Electricity, heat, oil transport OK")
        self.__setEntryEnergy()
        print("Entry energy OK")
        self.__setOnGridRenewables()
        print("On grid renewables OK")
        self.__setFuelTransport()
        print("Fuel transport OK")
        self.__setEntryFuels()
        print("Entry fuels OK")
        print("----------------------------")
        print("\n")
    
    def __setExitEnergyConsumption(self):
        self.exitEnergy = ExitEnergy(self.key_figures)

    def __setOffGridRenewables(self):
        self.entryOffGridRE = EntryOffGridRE(self.exitEnergy)

    def __setTransportElectricityHeatOil(self):
        self.transportElectricityHeatOil = TransportElectricityHeatOil(self.key_figures, self.exitEnergy)

    def __setEntryElectricityHeatOil(self):
        self.entryElectricityHeatOil = EntryElectricityHeatOil(self.key_figures, self.transportElectricityHeatOil)

    def __setOnGridRenewables(self):
        self.entryOnGridRenewables = EntryOnGridRE(self.entryElectricityHeatOil)

    def __setFuelTransport(self):
        self.fuelTransport = FuelTransport(self.exitEnergy, self.entryElectricityHeatOil)

    def __setEntryFuels(self):
        self.entryFuels = EntryFuels(self.fuelTransport)

    def getCarbonEmissions(self) -> float:
        _co2Emissions = 0
        _co2Emissions = _co2Emissions + self.entryElectricityHeatOil.getFuelConsumption(FuelType.COAL) * EmissionFactor.COAL.value
        raise(Exception("Add the emissions for the rest of the fuels..."))
    

        """
        Hint: Think about which fuels are used for combustion and where combustion happens in the energy system. 

        _co2Emissions = _co2Emissions + ?
        _co2Emissions = _co2Emissions + ?
        _co2Emissions = _co2Emissions + ?

        .
        .
        .
        """
        
        return abs(_co2Emissions)/1000 # Convert to gigatons
    
    def getYear(self):
        return self.year

    def toString(self) -> str :
        
        string = """
        {0} 
        """.format(self.exitEnergy.toString())

        return string

