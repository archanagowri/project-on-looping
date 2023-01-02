from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'Gracy','L':[11, 22, 33, 44]}
    return render(request,'looping.html',d)