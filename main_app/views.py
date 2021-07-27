from django.shortcuts import render
from store.models import Product

# Create your views here.


def home(request):
    products_for_main_page = Product.objects.all().filter(is_available=True).order_by('-created_date')[:8]

    context = {
        'products': products_for_main_page,
    }
    return render(request, 'index.html', context)


