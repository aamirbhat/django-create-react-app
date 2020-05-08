from setuptools import setup

README = open('README.md', 'r').read()
setup(
    name='django-create-react-app',
    packages=['create_react_app', 'create_react_app/templatetags'],
    version='0.1',
    description='Transparently use webpack with django',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Aamir Bhat',
    author_email='aamirbhat260@gmail.com',
    keywords=['django', 'create-react-app', 'react'],  # arbitrary keywords
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
    ],

)
