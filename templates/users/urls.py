from django.urls import path, include
from .views import home, admin_dashboard, add_seller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', include('products.urls')),
    path('chat/', include('chat.urls')),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/add-seller/', add_seller, name='add-seller'),
]

