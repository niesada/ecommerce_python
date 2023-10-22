from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def purchase_start_view(request):
    return HttpResponse("Started")

def purchase_success_view(request):
    return HttpResponse("Started")

def purchase_stopped_view(request):
    return HttpResponse("Started")