from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return render(request, "index.html")
def items(request):
    return render(request, "items.html")
def about(request):
    return render(request, "about.html")

