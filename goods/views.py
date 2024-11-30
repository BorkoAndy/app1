from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Product, Category
from goods.utils import q_search

def catalog(request, category_slug=None):
    # Filter data  
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    # Search data
    query = request.GET.get('q', None)

    # Checking url query
    if category_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
         goods = (Product.objects.filter(category__slug=category_slug))   

    # Checking filters
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    # Pagination
    paginator = Paginator(goods, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    # Context formation
    context = {   
        'goods': page_obj,
        # 'slug_url': category_slug
        }
    return render(request, "goods/catalog.html", context)




def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product':  product,
        
        }
    return render(request, "goods/product.html", context=context)
