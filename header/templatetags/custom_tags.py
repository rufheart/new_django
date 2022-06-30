from django.template import Library
from header.models import Add_To_Card,Detail_Product


register = Library()

@register.simple_tag 
def get_add_to_card():
    return Add_To_Card.objects.all()


