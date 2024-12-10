from django.contrib import admin
from .models import User, Seller

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    list_filter = ('user_type',)

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'store_name')
    search_fields = ('store_name',)
