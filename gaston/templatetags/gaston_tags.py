from django import template

register = template.Library()


@register.inclusion_tag('gaston/menu.html', takes_context=True)
def menu(context, menu, depth_count=None):
	depth_count = depth_count + 1 if depth_count is not None else 0

	return {
	    'menu': menu,
	    'request': context['request'],
	    'depth_count': depth_count,
    }


@register.simple_tag(takes_context=True)
def get_item_css_classes(context, item):
    request = context['request']
    return item.get_all_css_classes(request)
