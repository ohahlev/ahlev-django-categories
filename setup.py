# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import categories


setup(
    name='ahlev-django-categories',
    version=categories.__version__,
    description='categories app using django framework',
    author='ahlev',
    author_email='ohahlev@gmail.com',
    include_package_data=True,
    url='https://github.com/ohahlev/ahlev-django-categories/tree/ver-%s' % categories.__version__,
    packages=find_packages(),
    install_requires=[
          'django-fontawesome-5',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
