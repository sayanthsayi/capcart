from django.shortcuts import render,redirect
from django . http import JsonResponse
from ecomapp.models import Products,Category
from .models import Cart,Wishlist,Orders,Profile,OrderItems
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
                    quantity = int(request.POST.get('qty'))
                    if quantity > prod_check.qty:
                        return JsonResponse({'status':'only {} available'.format(prod_check.qty)})
                    else:
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

def Checkout(request):
    main_category = Category.objects.all()
    cart_checkout = Cart.objects.filter(user=request.user)
    total = 0
    for item in cart_checkout:
        price = item.product.disc_price * item.quantity
        total = total+price 
    famount = 0
    if total > 100000:
        famount = total
    else:
        famount = total+40

    default_profile = Profile.objects.filter(user=request.user).first()



    context = {'main_category':main_category,'cart_checkout':cart_checkout,'famount':famount,'default_profile':default_profile}
    return render(request,"checkout.html",context)

def Place_Order(request):
    if request.method == 'POST':
        Check_address =Orders()
        Check_address.First_name = request.POST.get('firstName')
        Check_address.Second_name = request.POST.get('lastName')
        Check_address.address = request.POST.get('address')
        Check_address.country = request.POST.get('country')
        Check_address.state = request.POST.get('state')
        Check_address.pincode = request.POST.get('zip')
        Check_address.user = request.user
        Check_address.email = request.POST.get('email')
        Check_address.district = request.POST.get('district')
        Check_address.save()

        if not Profile.objects.filter(user=request.user):
            default_profile = Profile()
            default_profile.First_name = request.POST.get('firstName')
            default_profile.Second_name = request.POST.get('lastName')
            default_profile.address = request.POST.get('address')
            default_profile.country = request.POST.get('country')
            default_profile.state = request.POST.get('state')
            default_profile.pincode = request.POST.get('zip')
            default_profile.user = request.user
            default_profile.email = request.POST.get('email')
            default_profile.district = request.POST.get('district')
            default_profile.save()

        cart = Cart.objects.filter(user=request.user)

        for items in cart:
            OrderItems.objects.create(
                orders = Check_address,
                products = items.product,
                quantity = items.quantity,
                price = items.product.disc_price
            )
            avail_qty = Products.objects.filter(id=items.product.id).first()
            avail_qty.qty = avail_qty.qty - items.quantity
            avail_qty.save()




        cart.delete()
        messages.success(request,'Order Placed Successfully...')
        return redirect('home')
    else:
        messages.error(request,'Something Went Wrong!')
        return redirect('home')
    

def User_Orders(request):
    orders = Orders.objects.filter(user=request.user)
    
   

    context = {'orders':orders}
    return render(request,'orders.html',context)