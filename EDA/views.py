from django.shortcuts import render
from EDA.models import EDAData
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Create your views here.
def show(request):
    def scatter():
        #df = px.data.iris()
        df = EDAData.objects.values_list('date','gender','age','CDLabel4Month' )
        df= pd.DataFrame(df)
        #x1 = [1,2,3,4]
        #y1 = [30, 35, 25, 45]

        #trace = go.Scatter(
            #x=x1,
            #y = y1
        #)
        # layout = dict(
        #     title='Simple Graph',
        #     xaxis=dict(range=[min(x1), max(x1)]),
        #     yaxis = dict(range=[min(y1), max(y1)])
        # )

        #fig = go.Figure(data=[trace], layout=layout)

        fig = px.scatter(df, x="CDLabel4Month", y="age")
        #fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
        #         size='petal_length', hover_data=['petal_width'])
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'home/welcome.html', context)