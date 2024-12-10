from rest_framework import generics
from .models import Shop, Category, Product
from .serializers import ShopSerializer, CategorySerializer, ProductSerializer
from django.db.models import Q
from .forms import ProductSearchForm

class ShopListView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_list(request):
    query = request.GET.get('query', '')
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )

    search_form = ProductSearchForm(initial={'query': query})
    return render(request, 'products/product_list.html', {
        'products': products,
        'search_form': search_form,
    })