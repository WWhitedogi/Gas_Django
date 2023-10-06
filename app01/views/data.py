from django.shortcuts import render

def data(request):
    return render(request, 'data.html')
