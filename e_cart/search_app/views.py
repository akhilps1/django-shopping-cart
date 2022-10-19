from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.


def search_result(request):
    query = request.GET['query']
    products = Product.objects.filter(name__contains=query)
    return render(request, 'search.html', {'products': products, 'query': query})