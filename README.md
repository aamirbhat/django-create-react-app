django-create-react-app
----------------------
This app helps us to integrate the react in django project through create react app template. This app works both in dev and production mode of the react. 



Quick start
-----------

### Install 

```
pip install django-create-react-app

```



Add "create_react_app" to your INSTALLED_APPS setting like this::

```
    INSTALLED_APPS = [
        ...
        'create_react_app',
    ]

```

---

# Settings Configuration

### Add Build Directory in the Settings

```
yarn build or npm run build

```
This creates the build directory inside the react folder. Add this build directory in the django settings e.g

```

REACT_BUILD_DIRECTORY = os.path.join(BASE_DIR, 'app', 'react', 'build')

```


### Add create react app configuration into your settings::



```
    CREATE_REACT_APP = {
        'DEFAULT': {
            'BUNDLE_DIR_NAME': REACT_BUILD_DIRECTORY,  
            'FRONT_END_SERVER': "http://localhost:3000/",
            'is_dev': False,
        }
    }
```


### Use it in your templates ::
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

### Add Below code for Collectstatic Finder to find the build folder ::
```
STATICFILES_DIRS = (
    os.path.join(REACT_BUILD_DIRECTORY, 'static'),
)
```





#Adding Multiple React Apps inside django Project

```

CREATE_REACT_APP = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': CLIENT_FRONTEND_BUILD,
        'FRONT_END_SERVER': "http://localhost:3000/",
        'is_dev':  True,
    },
    'ADMIN': {
        'BUNDLE_DIR_NAME': ADMIN_FRONTEND_BUILD,
        'FRONT_END_SERVER': "http://localhost:3001/",
        'is_dev': True,
    },
}


```

### Rendering react admin app inside templates :: 
```
{% load react_bundle_loader %}

<html>
  <head>
    {% render_bundle_css ADMIN %}
  </head>
  <body>
    <div id="root"></div>
     {% render_bundle_js ADMIN %}
  </body>
</head>
    
```