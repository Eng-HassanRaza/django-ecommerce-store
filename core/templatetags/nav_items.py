from django import template
from core.models import Order

register = template.Library()


@register.filter
def nave_bar_items():
    CATEGORY_CHOICES = (
        ('C', 'Cat'),
        ('D', 'Dog'),
        ('P', 'Parrot')
    )
    categorys = CATEGORY_CHOICES
    return 1