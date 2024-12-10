# seller_dashboard/views.py
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product  # Correct import
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    products = Product.objects.filter(seller=request.user.seller_profile)
    return render(request, 'seller_dashboard/dashboard.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller_profile
            product.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'seller_dashboard/add_product.html', {'form': form})

@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user.seller_profile)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'seller_dashboard/update_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user.seller_profile)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request, 'seller_dashboard/delete_product.html', {'product': product})
