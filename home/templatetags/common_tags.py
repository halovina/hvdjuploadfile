# Rp 6,000.00 
from django import template

register = template.Library()

@register.simple_tag
def convert_idr_currency(**kwargs):
    amount = kwargs.get('amount')
    return "Rp {:,.2f}".format(amount)