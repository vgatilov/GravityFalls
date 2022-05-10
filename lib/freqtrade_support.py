import pandas as pd
from matplotlib import pyplot as plt


class Candles:
    def __init__(self, json_path:str):
        self.import_candles(json_path)
        
    def import_candles(self, json_path:str) -> None:
        self.df = pd.read_json(json_path)
        self.df.columns = ['unix_ds', 'O', 'H', 'L', 'C', 'V']
        self.df['ds'] = pd.to_datetime(self.df['unix_ds'],unit='ms')
        self.df = self.df[['unix_ds', 'ds', 'O', 'H', 'L', 'C', 'V']]
        
    def plot(self) -> None:
        self.df.set_index('ds').loc[:, ['O', 'H', 'L', 'C']].plot(figsize=(15, 5))
        plt.show()
        self.df.set_index('ds').loc[:, 'V'].plot(figsize=(15, 5))
        plt.show()