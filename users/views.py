from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import User, Seller

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = request.POST['user_type']  # Get user type from form
            user.save()
            if user.user_type == 'seller':
                Seller.objects.create(user=user, store_name=request.POST.get('store_name', ''))  # Create Seller profile
            login(request, user)
            if user.user_type == 'seller':
                return redirect('dashboard')  # Redirect to seller dashboard
            else:
                return redirect('product-list')  # Redirect to product list
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'seller':
                return redirect('dashboard')  # Redirect to seller dashboard
            else:
                return redirect('product-list')  # Redirect to product list
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout
