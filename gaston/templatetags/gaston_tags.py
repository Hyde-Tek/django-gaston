from django import template

register = template.Library()


@register.inclusion_tag('gaston/menu.html', takes_context=True)
def menu(context, menu):
    return {
        'menu': menu,
        'request': context['request'],
    }


@register.filter()
def get_partial_path(path):
    if path == '/':
        return path
    else:
        split_path = path.split('/')
        return ('/' + split_path[1] + '/')
