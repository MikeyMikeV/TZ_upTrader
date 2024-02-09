from django import template
from shop_app.models import Category

register = template.Library()

@register.filter
@register.inclusion_tag("shop_app/tags/tree_menu.html")
def draw_menu(obj, selected = None):
    if obj!='main_menu':
        categories = Category.objects.filter(parent = obj).prefetch_related('children')
    else:
        categories = Category.objects.filter(parent__isnull = True).prefetch_related('children')
    context = {
        'categories':categories,
        'selected':selected,
    }
    return context
