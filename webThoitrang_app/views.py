from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")
def shop(request):
    return render(request, "shop.html")
def blog(request):
    return render(request, "blog.html")
def about(request):
    return render(request, "about.html")
def shop_details(request):
    return render(request, "shop_details.html")
def shop_cart(request):
    return render(request, "shop_cart.html")
def check_out(request):
    return render(request, "check_out.html")
def blog_details(request):
    return render(request, "blog_details.html")
def contact(request):
    return render(request, "contact.html")

