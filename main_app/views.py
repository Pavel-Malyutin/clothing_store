from django.shortcuts import render
from store.models import Product, ReviewRating


# Create your views here.


def home(request):
    products_for_main_page = Product.objects.all().filter(is_available=True).order_by('-created_date')[:8]
    for product in products_for_main_page:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products_for_main_page,
        'reviews': reviews,
    }
    return render(request, 'index.html', context)


