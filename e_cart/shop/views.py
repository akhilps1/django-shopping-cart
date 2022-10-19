from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def allProductCat(request, c_slug=None):
    c_page = None
    products_list = None
    products = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    paginator = Paginator(products_list, 4)
    try:
        page_no = int(request.GET.get('page', '1'))
        products = paginator.page(page_no)
    except (EmptyPage, InvalidPage):
        page = 1

    return render(request, "category.html", {"category": c_page, "products": products})


def productDetail(request, c_slug, p_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request, "product.html", {"product": product})
