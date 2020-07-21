from django.shortcuts import render
from EDA.models import EDAData

# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
        'check': EDAData.objects.get(pk =1),
    })