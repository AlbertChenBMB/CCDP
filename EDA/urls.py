from django.urls import path
from . import views
from EDA.dash_apps.finished_apps import simpleexample
from EDA.dash_apps.finished_apps import simpleexample2
# name 是要告訴說在哪個資料夾底下
urlpatterns = [
    path('', views.show, name='EDA')
]