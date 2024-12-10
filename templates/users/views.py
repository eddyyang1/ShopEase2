from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .forms import UserCreationForm

def home(request):
    return render(request, 'index.html')


def admin_required(user):
    return user.is_authenticated and user.user_type == 'admin'


@user_passes_test(admin_required)
def admin_dashboard(request):
    sellers = User.objects.filter(user_type='seller')
    return render(request, 'users/admin_dashboard.html', {'sellers': sellers})

@user_passes_test(admin_required)
def add_seller(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user_type = 'seller'
            seller.save()
            return redirect('admin-dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/add_seller.html', {'form': form})
