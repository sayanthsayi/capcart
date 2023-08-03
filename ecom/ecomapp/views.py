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
