# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in logistic/__init__.py
from logistic import __version__ as version

setup(
	name='logistic',
	version=version,
	description='Shipment Management',
	author='Yasser Elbana',
	author_email='yasserelbana@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
