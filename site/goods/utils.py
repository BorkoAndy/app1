from re import search
from goods.models import Product
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

def q_search(query):
    # Search by id
    if query.isdigit() and len(query) <=5:
        return Product.objects.filter(id=int(query))
    
    # Django imported full-text search with sorting by rank
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)
    return Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    
    # Full-text search with Q-objects
    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    # return Product.objects.filter(q_objects) 
