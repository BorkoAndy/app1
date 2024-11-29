from django import template

from goods.models import Category

register = template.Library()

@register.simple_tag()
def tag_all_categories():
    return Category.objects.all()