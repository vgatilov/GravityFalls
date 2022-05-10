from turtle import fillcolor, title
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class Candles:
    def __init__(self, json_path:str):
        self.import_candles(json_path)
        
    def import_candles(self, json_path:str) -> None:
        self.df = pd.read_json(json_path)
        self.df.columns = ['unix_ds', 'O', 'H', 'L', 'C', 'V']
        self.df['ds'] = pd.to_datetime(self.df['unix_ds'],unit='ms')
        self.df = self.df[['unix_ds', 'ds', 'O', 'H', 'L', 'C', 'V']]
        
    def plot(self) -> None:
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_traces(
            go.Candlestick(
                x=self.df['ds'],
                open=self.df['O'],
                high=self.df['H'],
                low=self.df['L'],
                close=self.df['C']
                ),
            secondary_ys=[True]
            )
        fig.add_traces(
            go.Bar(
                x=self.df['ds'],
                y=self.df['V'],
                marker_color='rgb(0,0,255)',
                opacity=0.5
                ),
            secondary_ys=[False]
            )
        fig.update_layout(
            margin=dict(l=5, r=5, t=5, b=5),
        )
        fig.show()