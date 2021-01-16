# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in stpl_2/__init__.py
from stpl_2 import __version__ as version

setup(
	name='stpl_2',
	version=version,
	description='v13 app test',
	author='stpl',
	author_email='info@sprics.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
