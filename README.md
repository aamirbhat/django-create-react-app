
# django-create-react-app

`django-create-react-app` is a package that seamlessly integrates React with a Django project using the Create React App (CRA) template. It supports both development and production modes of a React application.

## Why Use `django-create-react-app`?
- Works with the `asset-manifest` plugin on the frontend, maintained by Create React App.
- No frontend code modifications are needed for Single Page Applications (SPA).
- In development mode, it works with the frontend server via HTTP (`localhost:3000`).

---

## Quick Start

### Installation

Install the package via `pip`:

```bash
pip install django-create-react-app
```

Add `"create_react_app"` to your `INSTALLED_APPS` in Django:

```python
INSTALLED_APPS = [
    # Other apps...
    'create_react_app',
]
```

---

## Settings Configuration

### Add Build Directory in the Settings

To create the build directory for the React app, run:

```bash
yarn build
# or
npm run build
```

This will create a `build` directory inside your React app folder. Configure Django to reference this directory:

```python
REACT_BUILD_DIRECTORY = os.path.join(BASE_DIR, 'app', 'react', 'build')
```

### Configure Django to Use the Build Directory for Static Files

Tell Django to treat the build folder as a static directory:

```python
STATICFILES_DIRS = (
    os.path.join(REACT_BUILD_DIRECTORY, 'static'),
)
```

### Configure `django-create-react-app` in Django Settings

Add the following settings to manage the React app configuration:

```python
CREATE_REACT_APP = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': REACT_BUILD_DIRECTORY,  
        'FRONT_END_SERVER': "http://localhost:3000/",
        'IS_DEV': False,
    }
}
```

### Using React in Django Templates

To load your React app in Django templates, use the following template tags:

```django
{% load react_bundle_loader %}

<html>
  <head>
    {% render_bundle_css %}
  </head>
  <body>
    ...
    {% render_bundle_js %}
  </body>
</html>
```

---

## Adding Multiple React Apps in a Django Project

If your project has multiple React apps, configure them like this:

```python
CREATE_REACT_APP = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': REACT_BUILD,
        'FRONT_END_SERVER': "http://localhost:3000/",
        'IS_DEV': False,
        "PUBLIC_PATH_DEV": "http://localhost:3000/",
        "PUBLIC_PATH": "/static/",
    },
    'ADMIN': {
        'BUNDLE_DIR_NAME': REACT_BUILD,
        'FRONT_END_SERVER': "http://localhost:3000/",
        'IS_DEV': False,
    },
}
```

### `IS_DEV` Configuration

- **`IS_DEV: True`**: Ensure the React app is running on the `FRONT_END_SERVER` at the specified port.
- **`IS_DEV: False`**: Ensure the build path points to the correct build directory.

### Rendering a React App in Django Admin Templates

```django
{% load react_bundle_loader %}

<html>
  <head>
    {% render_bundle_css "ADMIN" %}
  </head>
  <body>
    <div id="root"></div>
    {% render_bundle_js "ADMIN" %}
  </body>
</html>
```

---

## Additional Features

### Preloading Assets

You can use the `is_preload=True` option to preload assets in your template:

```django
{% render_bundle_css is_preload=True %}
```

### Adding Attributes

You can add extra attributes to the generated tags:

```django
{% render_bundle_js attrib="async" %}
{% render_bundle_js attrib="disabled" %}
```

---

## Migration Notes

When upgrading from version `0.8.4` to `0.9`, the `is_dev` setting has been renamed to `IS_DEV`. Ensure you update your configuration as lowercase `is_dev` will no longer work.

---

## Docker Support

- The `PUBLIC_PATH_DEV` default value is `FRONT_END_SERVER`, useful for Docker setups.
- Use `PUBLIC_PATH_DEV` with Docker for `http://localhost:3000/`.
- `FRONT_END_SERVER`: `host.docker.internal`.

---

## Django Storage Support

When using Django's storage systems (e.g., AWS), change `PUBLIC_PATH` to your storage path:

```python
PUBLIC_PATH = "https://234234234.aws.com/static/"
```
