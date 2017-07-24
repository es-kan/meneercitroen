from django import template

register = template.Library()


@register.filter('format')
def format_currency(floatingpoint):
    return u'{:,.2f}'.format(floatingpoint)
