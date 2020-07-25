import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
import dash


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = DjangoDash('SimpleExample2', external_stylesheets=external_stylesheets)


# app.layout = html.Div([
#     html.H1('XXX', style={'margin-top': 10}),
#     dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
#     dcc.Slider(
#         id='slider-updatemode',
#         marks={i: '{}'.format(i) for i in range(20)},
#         max=20,
#         value=2,
#         step=1,
#         updatemode='drag',
#     ),
# ])


# @app.callback(
#                Output('slider-graph', 'figure'),
#               [Input('slider-updatemode', 'value')])
# def display_value(value):


#     x = []
#     for i in range(value):
#         x.append(i)

#     y = []
#     for i in range(value):
#         y.append(i)

#     graph = [
#                 {'x': [1, 2, value], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [value, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
#             ]
#     layout = {
#                 'title': 'Dash Data Visualization'
#             }
#     return {'data': graph, 'layout': layout}

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = DjangoDash('SimpleExample2', external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])
