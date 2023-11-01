from django.shortcuts import render
from django .contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
@login_required(login_url='signup')
def home(request):
    main_category = Category.objects.all()
    context={'main_category':main_category}
    return render(request,"home.html",context)


def Subcategory_show(request,slug):
    main_category = Category.objects.all()
    categorys = Category.objects.filter(slug=slug)
    subcategory = SubCategory.objects.filter(category__slug=slug)

    products = Products.objects.filter(category__slug=slug)
    page_number = request.GET.get("page")
    paginator = Paginator(products,3)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger :
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'subcategory':subcategory,'main_category':main_category,'products':products}
    return render(request,'subcat_view.html',context)


def Product_brands(request,slug):
    main_category = Category.objects.all()
    subcategory = SubCategory.objects.filter(slug=slug)
    products = Products.objects.filter(subcategory__slug=slug)
    category_series = ProductSeries.objects.filter(subcategory__slug=slug)
    segment = ProductSegment.objects.filter(subcategory__slug=slug)

    context = {'products':products,'main_category':main_category,'category_series':category_series,'subcategory':subcategory,'segment':segment}
    return render(request,'prod_brands.html',context)

def Product_Series_Show(request,slug):
    main_category = Category.objects.all()
    # product_series = ProductSeries.objects.filter(slug=slug)
    product = Products.objects.filter(productseries__slug=slug)
    context = {'main_category':main_category,'product':product}
    return render(request,"Product_series_show.html",context)

def SegmentView(request,slug):
    main_category = Category.objects.all()
    subcategory = SubCategory.objects.filter(slug=slug)
    # segment = ProductSegment.objects.filter(subcategory__slug=slug)
    product = Products.objects.filter(productsegment__slug=slug)

    context = {'main_category':main_category,'product':product}
    return render(request,'segment_view.html',context) 

def ProductView(request,slug):
    main_category = Category.objects.all()
    product = Products.objects.filter(slug=slug)
    

    for p in product:
        value =100-(p.disc_price/p.org_price)*100
        off_price = value

    for p in product:
        value = p.disc_price-p.org_price
        disc_price = value

    sub_category=SubCategory.objects.filter(slug=slug)
    # category_series = ProductSeries.objects.filter(subcategory__slug=slug)
    prod_series = ProductSeries.objects.filter(products__slug=slug)

    context ={'main_category':main_category,'product':product,'off_price':off_price,'disc_price':disc_price,'prod_series':prod_series,}
    return render(request,'product_view.html',context)

def SearchFunc(request):
    main_category = Category.objects.all()
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Products.objects.filter(name__contains = query)
            context={'products':products,'main_category':main_category}
            return render(request,'Search.html',context)
        else:
            print("no information to show")
            return render(request,'Search.html',{})
 
def OrderSuccess(request):
    main_category = Category.objects.all()

    context={'main_category':main_category}
    return render(request,'ordersuccess.html',context)