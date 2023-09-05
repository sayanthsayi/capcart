from django.contrib import admin
from .models import Cart,Wishlist,Orders,Profile,OrderItems
# Register your models here.

admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Orders)
admin.site.register(Profile)
admin.site.register(OrderItems)