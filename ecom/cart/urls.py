from django.urls import path
from . import views

urlpatterns = [
    path('AddToCart/',views.AddToCart,name='addtocart'),
    path('Cart/',views.CartView,name='cart'),
    path('Cart-delete/<str:pk>',views.CartDelete,name='cartdelete'),
    path('AddToishlist/',views.Prod_Wishlist,name='addtowishlist'),
    path('wishlist/',views.WishlistView,name='wishlist'),
    path('Wishlist-delete/<str:pk>',views.WishlistDelete,name='wishlistdelete'),
    path('Checkout/',views.Checkout,name='Checkout'),
    path('Place-order/',views.Place_Order,name='placeorder'),
    path('Orders/',views.User_Orders,name='orders'),
]
