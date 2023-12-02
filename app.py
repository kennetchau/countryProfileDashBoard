"""
    Name: Country Dashboard
    Python version: 3.12.0
    Author: Kenneth Chau
"""

## import modules
from dash import Dash, html, dash_table, dcc,Input,Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_json("data/CountryData.json")

## initiate the app
app = Dash(__name__)

colors = {
    'textcolor': '#777777'
}

## App layout
app.layout = html.Div(children=[
    html.H1(
        children = "Country Data",
        style = {
            'textAlign': 'center',
            'color': colors['textcolor']
        }
    ),
    html.Div(
        children = [
            dcc.Slider(
                df['Year'].min(),
                df['Year'].max(),
                step = None,
                value=df['Year'].min(),
                marks={str(year): str(year) for year in df['Year'].unique()},
                id='year-slider'
            ),
            dcc.Graph(id = "WorldPopulation_Graph",),
        ]
    )
])

## Create callback
@callback(
    Output('WorldPopulation_Graph', 'figure'),
    Input('year-slider','value')
)
def update_figure(selected_year):
    filtered_df = df[(df['Series Code'] == "NY.GDP.MKTP.KD") & (df['Year'] == selected_year)].sort_values(by='value', ascending = False).head(10)
    fig = px.bar(filtered_df, x = 'value', y="Country Name", orientation='h', labels = {'value':"GDP (constant 2015 US$)"})
    fig.update_layout(transition_duration = 500)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)