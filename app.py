"""
    Name: Country Dashboard
    Python version: 3.12.0
    Author: Kenneth Chau
"""

## import modules
from dash import Dash, html, dash_table, dcc
import pandas as pd

df = pd.read_csv("data/WorldPop.csv")

## initiate the app
app = Dash(__name__)

## App layout
app.layout = html.Div([
    html.Div(children = "Country data no modification"),
    dash_table.DataTable(data = df.to_dict('records'), page_size = 10),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)