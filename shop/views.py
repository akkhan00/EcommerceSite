from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    return render(request, "shop/index.html")

def about(request):
    return HttpResponse(b"shop about page")

def contact(request):
    return HttpResponse(b"shop contact page")

def tracker(request):
    return HttpResponse(b"shop Tracker page")

def search(request):
    return HttpResponse(b"shop Search page")

def productView(request):
    return HttpResponse(b"shop ProductView page")

def checkout(request):
    return HttpResponse(b"shop Checkout page")

