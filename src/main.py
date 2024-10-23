from misc.IEAStatisticsProcessor import IEAStatisticsProcessor
from balance.EnergyBalance import EnergyBalance


###### PORTFOLIO 2 ######

# Running this file will generate some errors.
# This is on purpose and it is your job to fix them.
# When you encounter an error, go to the line where the error was raised and fill in the missing code.
# Repeat this until you can run this file and produce the correct amount of CO2 emissions. 


_IEAStatisticsProcessor = IEAStatisticsProcessor()
key_figures_2020 = _IEAStatisticsProcessor.get_key_figures(r'iea_raw_data (shareable).xlsx',sheetname='2020')
_IEAStatisticsProcessor.exportToJSON(key_figures_2020, 'result2020.json')

# Example on loading from json. 
# This might be important later when you create scenarios.
# Then you can edit your key figures in your json file, save the file, and load it for use it as input in the EnergyBalance class.
# Be careful not to overwrite your changes with the "_IEAStatisticsProcessor.exportToJSON()" command!
key_figures_2020 = _IEAStatisticsProcessor.loadFromJSON('result2020.json')

# Load the key figures into the EnergyBalance class
e2020 = EnergyBalance(key_figures_2020, 2020)


print(e2020.getCarbonEmissions()) # You should get 30920.51596807954 gigatons for year 2020
tol = 1
target = 30920.51596807954
assert abs(e2020.getCarbonEmissions()-target)<=tol, "You seem to get the wrong CO2 emissions."





