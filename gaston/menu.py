from django.conf import settings

ACTIVE_CLASS = 'active'
if hasattr(settings, 'GASTON_ACTIVE_CLASS'):
    ACTIVE_CLASS = settings.GASTON_ACTIVE_CLASS


class MenuItem:
    def __init__(self, label, url, css_classes='', submenu=None):
        self.label = label
        self.url = url
        self.css_classes = css_classes
        self.submenu = submenu

    def get_active_class(self, request):
        css_class = ''
        if (
            self.url == request.path or
            (self.url != '/' and self.url in request.path)
        ):
            css_class = ACTIVE_CLASS
        return css_class

    def get_css_classes(self):
        return self.css_classes

    def get_all_css_classes(self, request):
        return '%s %s' % \
            (self.get_css_classes(), self.get_active_class(request))
