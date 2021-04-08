from setuptools import setup

README = open('README.md', 'r').read()
install_requires=['requests']
setup(
    name='django-create-react-app',
    packages=['create_react_app', 'create_react_app/templatetags'],
    version='0.8.4',
    description='use create react app with django',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Aamir Bhat',
    author_email='aamirbhat.pro@gmail.com',
    keywords=['django', 'create-react-app', 'react','django react','django integration  react',' create react app'],  # arbitrary keywords
    url='https://github.com/aamirbhat/django-create-react-app.git',
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
    install_requires=install_requires,

)
