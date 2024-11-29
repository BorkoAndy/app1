from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Product, Category

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Product.objects.all()
    else:
         goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))
       
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)    


    context = {   
        'goods': page_obj,
        }
    return render(request, "goods/catalog.html", context)




def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product':  product,
        
        }
    return render(request, "goods/product.html", context=context)
