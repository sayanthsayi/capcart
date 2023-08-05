from django.shortcuts import render
from django .contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='signup')
def home(request):
    main_category = Category.objects.all()
    # sp_brands = SubCategory.objects.filter(main_category__slug=slug)
    context={'main_category':main_category}
    return render(request,"home.html",context)


def Subcategory_show(request,slug):
    main_category = Category.objects.all()
    categorys = Category.objects.filter(slug=slug)
    subcategory = SubCategory.objects.filter(category__slug=slug)

    products = Products.objects.filter(category__slug=slug)
    context = {'subcategory':subcategory,'main_category':main_category,'products':products}
    return render(request,'subcat_view.html',context)


def Product_brands(request,slug):
    main_category = Category.objects.all()
    subcategory = SubCategory.objects.filter(slug=slug)
    products = Products.objects.filter(subcategory__slug=slug)
    category_series = ProductSeries.objects.filter(subcategory__slug=slug)


    context = {'products':products,'main_category':main_category,'category_series':category_series}
    return render(request,'prod_brands.html',context)