from django.shortcuts import render
from datetime import datetime
from EDA.models import EDAData
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from django.db import connection
import dash
import dash_core_components as dcc
import dash_html_components as html


# Create your views here.


def show(request):
    def scatter():

        
        genderDataFrame = pd.DataFrame()
        with connection.cursor() as cursor:
            cursor.execute('SELECT date FROM EDAData GROUP by date')
            dataDate = cursor.fetchall()
        date = []
        gender = []
        count = []

        for i in range(len(dataDate)):
            date.append(dataDate[i][0])
            date.append(dataDate[i][0])
            gender.append("gender0")
            gender0 = EDAData.objects.values_list('gender').filter(date=dataDate[i][0], gender='0').count()
            count.append(gender0)

            gender.append("gender1")
            gender1 = EDAData.objects.values_list('gender').filter(date=dataDate[i][0], gender='1').count()
            count.append(gender1)

        genderDataFrame["date"] = date
        genderDataFrame["gender"] = gender
        genderDataFrame["count"] = count

        print(genderDataFrame)
        fig = px.bar(genderDataFrame, x="date", y="count", color="gender", barmode="group", title='性別圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'welcome.html', context)