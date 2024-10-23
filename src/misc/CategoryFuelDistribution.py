from misc.constants.Fuel import FuelType

class CategoryFuelDistribution():
    
    def __init__(self) -> None:
        self.consumptionDict = {}

    def setFuelConsumption(self, fuel : FuelType, consumption : float):
        self.consumptionDict[fuel] = consumption
    
    def getFuelConsumption(self, fuel: FuelType) -> float:
        return self.consumptionDict[fuel]

    def getCategoryFuelConsumption(self) -> float:

        _consumption = 0

        for fuel in self.consumptionDict:
            _consumption = _consumption + self.consumptionDict[fuel]

        return _consumption
    
    def toString(self) -> str :
        
        string = """
        {0} 
        """.format(self.consumptionDict)

        return string

