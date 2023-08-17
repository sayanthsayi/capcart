from django.shortcuts import render,redirect
from django . http import JsonResponse
from ecomapp.models import Products,Category
from .models import Cart,Wishlist
from django . contrib import messages
# Create your views here.

def AddToCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('id')
            prod_check = Products.objects.get(id=prod_id)

            if prod_check:
                if Cart.objects.filter(product__id=prod_id):
                    return JsonResponse({'status':'Product Already In Cart'})
                else:
                    quantity = request.POST.get('qty')
                    Cart.objects.create(
                        user = request.user,
                        product = prod_check,
                        quantity = quantity
                    )
                    return JsonResponse({'status':'Product Added To Cart'})
        else:
            return JsonResponse({'status':'Login Requered'})
        
def CartView(request):
    main_category = Category.objects.all()
    cart = Cart.objects.filter(user=request.user)
    total = 0
    for item in cart:
        price = item.product.disc_price * item.quantity
        total = total+price 
    famount = 0
    if total > 100000:
        famount = total
    else:
        famount = total+40


    context = {'cart':cart,'famount':famount,'total':total,'main_category':main_category}
    return render(request,'cart.html',context) 

        
def CartDelete(request,pk):
    user = Cart.objects.filter(user=request.user)
    cartdel = user.get(id=pk)
    cartdel.delete()
    messages.success(request,"Item removed..")
    return redirect('cart')
        
def Prod_Wishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('id')
            prod_check = Products.objects.get(id=prod_id)

            if prod_check:
                if Wishlist.objects.filter(product__id=prod_id):
                    return JsonResponse({'status':'Product Already In Wishlist'})
                else:
                    Wishlist.objects.create(
                        user = request.user,
                        product = prod_check,
                    )
                    return JsonResponse({'status':'Product Added to Wishlist'})
        else:
            return JsonResponse({'status':'Login Requered'})


def WishlistView(request):
    main_category = Category.objects.all()
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist,'main_category':main_category}
    return render(request,'wishlist.html',context) 

def WishlistDelete(request,pk):
    user = Wishlist.objects.filter(user=request.user)
    wishlistdel = user.get(id=pk)
    wishlistdel.delete()
    messages.success(request,"Item removed..")
    return redirect('wishlist')