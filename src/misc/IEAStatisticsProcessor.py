import pandas as pd
import numpy as np
import json

class IEAStatisticsProcessor():
    
    def __init__(self):
        pass

    def get_key_figures(self, filename: str=None, sheetname:str=None) -> dict:

        raise(Exception("Paste your code from portfolio 1 here..."))

        return self.key_figures
    
    def exportToJSON(self, key_figures : dict, name : str):
        import json
        with open(name, 'w') as fp:
            json.dump(key_figures, fp)

    def loadFromJSON(self, name : str):
        with open(name) as f:
            key_figures = json.load(f)

        return key_figures