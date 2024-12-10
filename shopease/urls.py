from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('users/', include('users.urls')), # Include user URLs here
    path('login/', views.login, name='login'),
    path('seller/', include('seller_dashboard.urls')),
]

# This will add the settings for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
