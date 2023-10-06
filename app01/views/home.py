from django.shortcuts import render
from django import  forms
from django.core.validators import RegexValidator
from django.utils.safestring import  mark_safe
from django.http import JsonResponse
from app01.models import Measurement
def home_main(request):
    return render(request,'home_main.html')
def home_dashboard(request):
    latest_data=Measurement.objects.latest('id')
    data={
        'methane_concentration':latest_data.methane_concentration,
        'formaldehyde_concentration':latest_data.formaldehyde_concentration
    }
    return JsonResponse(data)

