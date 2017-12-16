from django.http import HttpResponse
from django.shortcuts import render

def basic_stats(request):
    return HttpResponse(render(request, "base.html"))