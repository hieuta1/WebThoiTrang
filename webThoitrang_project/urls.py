"""
URL configuration for webThoitrang_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from webthoitrang_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("shop_details/<int:pk>/", views.shop_details, name="shop_details"),
    path("shop_cart/", views.shop_cart, name="shop_cart"),
    path("check_out/", views.check_out, name="check_out"),
    path("blog_details/", views.blog_details, name="blog_details"),
    path("contact/", views.contact, name="contact"),

    path("admin/", admin.site.urls),
]
