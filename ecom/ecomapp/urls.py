from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('Productbrands/<str:slug>/',views.Product_brands,name="Productbrands"),
    path('subcategory_show/<str:slug>/',views.Subcategory_show,name="Subcategoryshow"),
]
