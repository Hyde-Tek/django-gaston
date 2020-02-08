from django import template

register = template.Library()


@register.inclusion_tag('gaston/menu.html', takes_context=True)
def menu(context, menu):
    return {
        'menu': menu,
        'request': context['request'],
    }


@register.simple_tag(takes_context=True)
def get_all_css_classes(context, item):
    request = context['request']
    return item.get_all_css_classes(request)
