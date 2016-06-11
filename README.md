[![PyPI](https://img.shields.io/pypi/v/django-crum.svg)](https://pypi.python.org/pypi/django-crum/)
[![PyPI](https://img.shields.io/pypi/l/django-crum.svg)](https://pypi.python.org/pypi/django-crum/)
[![PyPI](https://img.shields.io/pypi/pyversions/django-crum.svg)](https://pypi.python.org/pypi/django-crum/)
[![Build Status](http://img.shields.io/travis/ninemoreminutes/django-crum.svg)](https://travis-ci.org/ninemoreminutes/django-crum)

Django-CRUM
===========

Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It provides a signal to extend the built-in function for getting the current
user, which could be helpful when using custom authentication methods or user
models.

It is tested against:
 * Django 1.8 (Python 2.7, 3.3, 3.4 and 3.5)
 * Django 1.9 (Python 2.7, 3.4 and 3.5)
 * Django 1.10 (Python 2.7, 3.4 and 3.5)
 * Django master (Python 2.7, 3.4 and 3.5)
