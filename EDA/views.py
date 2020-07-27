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
        # ageDataFrame0 = ageDataFrame[ageDataFrame['cd4label']=='0']
        # print(ageDataFrame0)
        # ageDataFrame1=ageDataFrame[ageDataFrame['cd4label']=='1']
        # print(ageDataFrame1)
        # ageDataFrame2=ageDataFrame[ageDataFrame['cd4label']=='2']
        # print(ageDataFrame2)
        # ageDataFrame3=ageDataFrame[ageDataFrame['cd4label']=='3']
        # print(ageDataFrame3)
        # ageDataFrame4=ageDataFrame[ageDataFrame['cd4label']=='4']
        # print(ageDataFrame4)
        # ageDataFrame5=ageDataFrame[ageDataFrame['cd4label']=='5']
        # print(ageDataFrame5)


        fig = px.histogram(ageDataFrame, x="age", y="count", color="cd4label", marginal="rug",
                   hover_data=ageDataFrame.columns, barmode="group", title='性別圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    # def genderDist():

        
    #     genderDataFrame = pd.DataFrame()
    #     with connection.cursor() as cursor:
    #         cursor.execute('SELECT date FROM EDAData GROUP by date')
    #         dataDate = cursor.fetchall()
    #     date = []
    #     gender = []
    #     count = []
    #     genderCD4 = []

    #     for i in range(len(dataDate)):
    #         for j in range(6):
    #             date.append(dataDate[i][0])
    #             date.append(dataDate[i][0])
    #             gender.append("gender0")
    #             gender0 = EDAData.objects.values_list('gender').filter(date=dataDate[i][0], gender='0', CDLabel4Month=j).count()
    #             count.append(gender0)
    #             genderCD4.append(j)

    #             gender.append("gender1")
    #             gender1 = EDAData.objects.values_list('gender').filter(date=dataDate[i][0], gender='1', CDLabel4Month=j).count()
    #             # print(gender1)
    #             count.append(gender1)
    #             genderCD4.append(j)

    #     genderDataFrame["date"] = date
    #     genderDataFrame["gender"] = gender
    #     genderDataFrame["count"] = count
    #     genderDataFrame["genderCD4"] = genderCD4

    #     print(genderDataFrame)
    #     fig = px.bar(genderDataFrame, x="date", y="count", color="genderCD4", barmode="group", title='CD4性別分布圖')
    #     plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    #     return plot_div

    context ={
        'plot1': scatter(),
        #'genderDist': genderDist()
    }

    return render(request, 'welcome.html', context)