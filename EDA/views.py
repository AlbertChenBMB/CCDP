from django.shortcuts import render
from datetime import datetime
from EDA.models import EDAData
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from django.db import connection
import plotly.figure_factory as ff
import numpy as np
# Create your views here.
def show(request):
    def scatter():

        
        ageDataFrame = pd.DataFrame()
        with connection.cursor() as cursor:
            cursor.execute('SELECT date,age,CDLabel4Month FROM EDAData')
            dataDate = cursor.fetchall()
        
        
        
        date = []
        age = []
        cd4label=[]
        count=[]
        #print(dataDate[0][2])


        for i in range(len(dataDate)):
            date.append(dataDate[i][0])
            age.append(dataDate[i][1])
            cd4label.append(dataDate[i][2])
            count.append(1)
            

        ageDataFrame["date"] = date
        ageDataFrame["age"] = age
        ageDataFrame["cd4label"] = cd4label
        ageDataFrame["count"] = count
        

        fig = px.histogram(ageDataFrame, x="age", y="count", color="cd4label", marginal="rug",
                   hover_data=ageDataFrame.columns, barmode="group", title='性別圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def corr():

        df = pd.read_csv('correlation_matrix.csv')
        fig = px.imshow(df, labels=dict(x="features", y="features", color="Person Correlation"))
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': corr(),
        'plot2': scatter(),
    }

    def sigfig():

        df = pd.read_csv('significant_feature.csv')
        fig = px.histogram(df,x="Features", y="Significant", color="Date", marginal="rug",labels=dict(x="Features", y="Significant", color="Date"))
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': corr(),
        'plot2': scatter(),
        'plot3': sigfig(),
    }

    return render(request, 'welcome.html', context)