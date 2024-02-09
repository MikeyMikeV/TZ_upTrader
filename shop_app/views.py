from django.shortcuts import render
from .models import Category

def home_page(request):
    context = {

    }
    return render(request, 'shop_app/home_page.html', context)

def show_category(request, cat_id):
    context = {
        'cat_id':cat_id
    }
    return render(request, 'shop_app/category.html', context)
