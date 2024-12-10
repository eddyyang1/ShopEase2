from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product

@login_required
def seller_dashboard(request):
    if request.user.user_type != 'seller':
        return redirect('home')
    products = Product.objects.filter(category__shop__owner=request.user)
    return render(request, 'products/seller_dashboard.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})