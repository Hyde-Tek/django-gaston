ACTIVE_CLASS = 'active'
SELECTED_CLASS = 'selected'


class MenuItem:
    def __init__(self, label, url, css_classes='', submenu=None):
        self.label = label
        self.url = url
        self.css_classes = css_classes
        self.submenu = submenu

    def status_class(self, request):
        css_class = ''

        if self.url == request.path:
            css_class = ACTIVE_CLASS

        if (
            self.url != '/' and
            self.url in request.path and
            not self.url == request.path
        ):
            css_class = SELECTED_CLASS
        return css_class

    def get_css_classes(self):
        return self.css_classes

    def get_all_css_classes(self, request):
        return '%s %s' % \
            (self.get_css_classes(), self.status_class(request))
