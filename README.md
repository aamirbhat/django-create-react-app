django-create-react-app
----------------------
This app helps us to integrate the react in django project through create react app template. This app works both in dev and production mode of the react. 


### Why django-create-react-app 
* works with the asset-manifest plugin on the frontend which is used/maintained by create react app 
* No Frontend code modification needed for SPA 
* Dev Mode works with frontend server through http (localhost:3000) 


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
This command creates the build directory inside the react app folder.

```
REACT_BUILD_DIRECTORY = os.path.join(BASE_DIR, 'app', 'react', 'build')
This is the path in which build is created

```

### Add Below code for Collectstatic Finder to find the build folder ::
```
Build Directory created django needs to treat it static directory
STATICFILES_DIRS = (
    os.path.join(REACT_BUILD_DIRECTORY, 'static'),
)
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

#### is_dev: True 
make sure react app is running on FRONT_END_SERVER on same port which is declared 
### is_dev: False
make sure build path is pointed to the right build directory 


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
