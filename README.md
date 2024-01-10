# Gaston

A django menu generator.

## CSS Classes

### Menu

A `depth-{{ depth_count }}` CSS class is added to every `<ul>`, indicating its depth, 0-indexed.
### Submenu

Gaston automatically adds the following CSS classes to your `MenuItem` elements:

class|description
-|-
`active`|If the current URL exactly matches the `MenuItem`'s URL
`selected`|If the current URL contains the `MenuItem`'s `url`<br />If any submenu `MenuItem`'s `url` exatly matches the current URL

## Menu Items

Gaston defines a `MenuItem` class. Each `MenuItem` accepts the following parameters:

Parameter|Decsription
-|-
`label`|The label to be displayed.
`url`|The URL of the menu item.
`css_classes`|Additional CSS classes for the specific element.
`submenu`|A list of `MenuItem` that will be rendered as a nested `<ul>`.

## Available `tempaltetags`

Gaston provides the following templatetags:

tag|description
-|-
`menu`|Renders a given menu.
`get_item_css_classes`|Returns a string with the item's CSS classes.

## Usage

### Installation

- install `django-gaston`

- Add `gaston` to your `INSTALLED_APPS` in `settings.py`:

```py
INSTALLED_APPS = [
    ...
    "gaston",
    ...
]
```

### Definitions

- Define a `menus.py` with your menu layout:

```py
from django.urls import reverse

from gaston.menu import MenuItem

about_menu = [
    MenuItem("Company", url=reverse("company")),
    MenuItem("FAQ", url=reverse("faq")),
]

main_menu = [
    MenuItem("Home", url=reverse("home")),
    MenuItem("About", url=reverse("about"), css_classes="with-submenu", submenu=about_menu),
]
```

- Define a context processor inside an app (e.g. `PROJECT_NAME/context_processors.py`):

```py
from .menus import main_menu


def menus(request):
    return {
        "main_menu": main_menu,
    }
```

- Add the above context processor in your list of context processors (in `settings.py`):
```py
TEMPLATES = [
    {
        ...
        "OPTIONS": {
            "context_processors": [
                ...
                "APP_NAME.context_processors.menus",
            ],
        },
    },
]
```

Where `APP_NAME` is the name of the app where you defined your `menus.py`.

### Templates

Finally, load `gaston_tags` inside your template and call it as follows:

```html
{% load gaston_tags %}

<nav>{% menu main_menu %}</nav>
```

Where `main_menu` is the key from your context processor dictionary.

## Build and Publish

### Build

In the root folder run:

```bash
python3 setup.py sdist bdist_wheel
```

This will create a folder named `dist` with the code ready to be published to pypi.

### Publish to PYPI

Install `twine` with pipx by running
```bash
pipx install twine
```

Run the command bellow to publish the package

```bash
twine upload dist/*
```

Username and Password will be asked. For username, use `__token__` and for password the token that
was generated in the PYPI site.
