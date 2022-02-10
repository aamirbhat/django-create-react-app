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
            'IS_DEV': False,
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
        'BUNDLE_DIR_NAME': REACT_BUILD,
        'FRONT_END_SERVER': "http://localhost:3000/",
        'IS_DEV': False,
        "PUBLIC_PATH_DEV": "http://localhost:3000/",
        "PUBLIC_PATH": "/static/"
    }
    'ADMIN': {
        'BUNDLE_DIR_NAME': REACT_BUILD,
        'FRONT_END_SERVER': "http://localhost:3000/",
        'IS_DEV': False,
    },
}


```




### Rendering react admin app inside templates :: 
```
{% load react_bundle_loader %}

<html>
  <head>
    {% render_bundle_css "ADMIN" %}
  </head>
  <body>
    <div id="root"></div>
     {% render_bundle_js "ADMIN" %}
  </body>
</head>
    
```


### Using Preloading ::
The is_preload=True option in the render_bundle_css or render_bundle_js template tag can be used to add rel="preload" link tags.
```
{% render_bundle_css is_preload=True %}

```

### Add attributes
add some extra attributes to the tag
```
{% render_bundle_js  attrib="async" %}

{% render_bundle_js  attrib="disabled" %}
```


### migration from 0.8.4 to 0.9
"is_dev" changed to "IS_DEV" 
is_dev in lowercase will not work 


### docker support
PUBLIC_PATH_DEV default value will be FRONT_END_SERVER, which will be used for incase of docker

PUBLIC_PATH_DEV will be used in case of docker to http://localhost:3000/
FRONT_END_SERVER: host.docker.internal

### django storage support

change PUBLIC_PATH to storagepath e.g

PUBLIC_PATH:"https://234234234.aws.com/static/"
