from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('Productbrands/<str:slug>/',views.Product_brands,name="Productbrands"),
    path('subcategory_show/<str:slug>/',views.Subcategory_show,name="Subcategoryshow"),
    path('Product-Series-Show/<str:slug>',views.Product_Series_Show,name="ProductSeriesShow"),
    path('SegmentView/<str:slug>',views.SegmentView,name="SegmentView"),
    path('ProductView/<str:slug>',views.ProductView,name="ProductView"),
    path('Search/',views.SearchFunc,name="Search"),
    path('OrderSuccess/',views.OrderSuccess,name='ordersuccessfully'),
    ]
