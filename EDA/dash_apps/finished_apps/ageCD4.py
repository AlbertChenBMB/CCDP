from django.shortcuts import render
from datetime import datetime
from EDA.models import EDAData
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from django.db import connection
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

# Create your views here.
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
ageDataFrame = pd.DataFrame()
with connection.cursor() as cursor:
            cursor.execute('SELECT date,age,CDLabel4Month FROM EDAData')
            dataDate = cursor.fetchall()
date = []
age = []
cd4label=[]
count=[]

for i in range(len(dataDate)):
            date.append(dataDate[i][0])
            age.append(dataDate[i][1])
            cd4label.append(dataDate[i][2])
            count.append(1)

ageDataFrame["date"] = date
ageDataFrame["age"] = age
ageDataFrame["cd4label"] = cd4label
ageDataFrame["count"] = count




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('ageCD4', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='date-slider',
        min =0,
        max=len(dataDate)-1,
        marks={i: dataDate[i][0] for i in range(len(dataDate))},
        value=0,
        
        
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('date-slider', 'value')])

def update_figure(selected_date):
    filtered_df = ageDataFrame[ageDataFrame.date==dataDate[selected_date][0]]
    # print()
    # print(selected_date)
    # print(filtered_df.date)
    fig = px.bar(filtered_df, x="age", y="count", color="cd4label", barmode="group", title='CD4年齡分布圖')

    fig.update_layout(transition_duration=100)
    

    return fig