django-create-react-app
----------------------


This app is a Django app that helps to integrating the integrate the React that has been added in your Project through
create React App

Detailed documentation is in the "docs" directory.

Quick start
-----------

### Install 

```
pip install django-create-react-app

```




1. Add "create_react_app" to your INSTALLED_APPS setting like this::

```
    INSTALLED_APPS = [
        ...
        'create_react_app',
    ]

```

2. Add create react app configuration into your settings::
```
    CREATE_REACT_APP = {
        'DEFAULT': {
            'BUNDLE_DIR_NAME': '<path to bundle folder>',
            'FRONT_END_SERVER': "http://localhost:3000/",
            'is_dev': False,
        }
    }
```


3. Use it in your templates ::
```
{% load react_bundle_loader %}

<html>
  <head>
    {% render_bundle_css  %}
  </head>
  <body>
    ....
     {% render_bundle_js %}
  </body>
</head>
    
```
