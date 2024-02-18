from django import template

def currency_birr(value):
    return f"{value:.2f} birr"

register = template.Library()

register.filter("currency_birr", currency_birr)