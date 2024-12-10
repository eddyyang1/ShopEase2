from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = request.POST['user_type']  # Get user type from form
            user.save()
            login(request, user)
            if user.user_type == 'seller':
                return redirect('seller-dashboard')
            else:
                return redirect('product-list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
