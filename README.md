# Django Ads-txt

[![PYPI](https://img.shields.io/pypi/v/django-ads-txt.svg)](https://pypi.python.org/pypi/django-ads-txt)
[![Build Status](https://api.travis-ci.org/flyingelephantlab/django-ads-txt.svg?branch=master)](https://travis-ci.org/flyingelephantlab/django-ads-txt)
[![pep8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Python](https://img.shields.io/pypi/pyversions/django-ads-txt.svg)](https://pypi.python.org/pypi/django-ads-txt)

This is a basic Django application to manage Authorized Digital Sellers (ads.txt) file based on [iabtech lab specification](https://iabtechlab.com/ads-txt/)


### Requirements
Python 2.7, 3.5 or PyPy.

Django 1.9 or higher.

## Installation

Use your favorite Python installer to install it from PyPI:

```bash
pip install django-ads-txt
```

Or get the source from the application site at:

```bash
https://github.com/flyingelephantlab/django-ads-txt/
```


1. Add ``'ads_txt'`` to your [INSTALLED_APPS](https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps) setting.

2. Run the ``migrate`` management command

3. To activate ads.txt generation on your Django site, add this line to your [URLconf](https://docs.djangoproject.com/en/dev/topics/http/urls/):

```python
url(r'', include('ads_txt.urls')),
# Alternative:
# path(r'', include('ads_txt.urls')),
```
4. Add the domains you need to appear from admin panel

### Rules
The instructions are encoded as a formatted plain text object, described here. A complete
description of the syntax of this format:

    <Domain #1>, <Account ID #2>, <Account type #3>, <Authority ID #4>


| Field                   | Description                                                                           | 
| ------------------------|:-------------------------------------------------------------------------------------:|
| Domain (Required)       | Domain name of the advertising system                                                 |
| Account ID (Required)   | The identifier associated with the seller or reseller account                         |
| Account type (Required) | Type of Account/Relationship. It has two values `DIRECT` and `RESELLER`               |
| Authority ID (Optional) | An ID that uniquely identifies the advertising system within a certification authority |

### Examples:
```bash
example.com, 108933, DIRECT, 7857hf1d2fr6d8b34
opexample.com, [538220672 - CC], RESELLER, 6a69ec356744c6
opexample.com, [537120668 - CC], RESELLER, 6a69ec356744c6
ex.com, 7118, RESELLER
```

### Caching

You can optionally cache the generation of the ads.txt. Add or change the ADSTXT_CACHE_TIMEOUT setting with a value in seconds in your Django settings file:
```bash
ADSTXT_CACHE_TIMEOUT = 60*60*24
```

### Bugs and feature requests
As always your mileage may vary, so please don’t hesitate to send feature requests and bug reports:

https://github.com/flyingelephantlab/django-ads-txt/issues


 
