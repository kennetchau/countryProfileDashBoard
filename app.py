"""
    Name: Country Dashboard
    Python version: 3.12.0
    Author: Kenneth Chau
"""

## import modules
from dash import Dash, html, dash_table, dcc,Input,Output, callback
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_json("data/CountryData.json")

# Get the code detail and name
dfCode = df[['Series Code','Series Name']].drop_duplicates()

## initiate the app
app = Dash(__name__)


## App layout
app.layout = html.Div(children=[
    html.H1(
        children = "Country Data",
        style = {
            'textAlign': 'left',
            'margin-bottom': '10px'
        }
    ),
    html.Div(
        children = [
            # Add a drop down for country selecting
            dcc.Dropdown(
                df['Country Name'].unique(), 
                searchable = True, 
                multi = True, 
                id = 'country-selector',
            ),
            # Add a slider to select the year
            dcc.Slider(
                df['Year'].min(),
                df['Year'].max(),
                step = None,
                value=df['Year'].min(),
                marks={str(year): str(year) for year in df['Year'].unique()},
                id='year-slider'
            ),
            # Add a bar chart to compare data
            dcc.Graph(id = "WorldPopulation_Graph",),
        ],
    )
])

## Create callback
@callback(
    Output('WorldPopulation_Graph', 'figure'),
    Input('year-slider','value'),
    Input('country-selector','value')
)
def update_figure(selected_year, selected_country):
    condition1 = df['Series Code'] == "NY.GDP.MKTP.KD"
    condition2 = df['Year'] == selected_year
    condition3 = np.isin(df,selected_country).any(axis = 1)
    filtered_df = df[condition1 & condition2 & condition3].sort_values(by='value', ascending = False)
    fig = px.bar(filtered_df, x = 'value', y="Country Name", orientation='h', labels = {'value':"GDP (constant 2015 US$)"})
    fig.update_layout(transition_duration = 500)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)