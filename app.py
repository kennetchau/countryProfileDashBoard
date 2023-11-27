"""
    Name: Country Dashboard
    Python version: 3.12.0
    Author: Kenneth Chau
"""

## import modules
from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/WorldPop.csv", index_col = 0)
df2 = df.loc[(df['Population, density and surface area'] == "Total, all countries or areas") & (df['Series'] == "Population mid-year estimates (millions)")]

## initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'textcolor': '#777777'
}

## Create a function to make graphs
def linePlot(dataFrame, xValue:str, yValue:str, titleName:str,xAlias=None, yAlias=None):
    fig = px.line(dataFrame, x=xValue, y=yValue, title=titleName)
    if xAlias != None:
        fig.update_layout(xaxis_title = xAlias)
    if yAlias != None:
        fig.update_layout(yaxis_title = yAlias)
    return fig


## App layout
app.layout = html.Div(children=[
    html.H1(
        children = "World Population",
        style = {
            'textAlign': 'center',
            'color': colors['textcolor']
        }
    ),
    html.Div(
        children = [
            dcc.Graph(
                id = "World Population",
                figure = linePlot(df2, "Year", "Value", titleName = "World Population overtime" ,yAlias="Population (millions)")
            )
        ]
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)