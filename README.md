django-create-react-app


This app is a Django app that helps to integrating the integrate the React that has been added in your Project through
create React App

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'create-react-app',
    ]

2. Add create react app configuration into your settings::

    CREATE_REACT_APP = {
        'DEFAULT': {
            'CACHE': True,
            'BUNDLE_DIR_NAME': '/Users/aamirbhatt/workspace/hack_django_react/dashboard/static',
            'LOADER_CLASS': 'create_react_app.loader.CreateReactLoader',
            'FRONT_END_SERVER': "http://localhost:3000/",
            'is_dev': False,
        }
    }

3. Use it in your templates ::
    {% load react_bundle_loader %}

    add this tag in the html head
        {% render_bundle_css  %}

    add this tag in the html body
        {% render_bundle_js %}

