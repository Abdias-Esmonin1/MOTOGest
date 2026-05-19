from django import template

register = template.Library()

@register.filter
def fcfa(value):
    try:
        return "{:,.0f} FCFA".format(float(value)).replace(',', ' ')
    except (ValueError, TypeError):
        return "0 FCFA"

@register.filter
def pourcent(value, total):
    try:
        return round((float(value) / float(total)) * 100, 1)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0
