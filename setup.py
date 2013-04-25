#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='pl-py2deb',
      version='0.5.0',
      description='A tool to convert python packages to debian packages.',
      author='Arjan Verwer',
      author_email='arjan.verwer@paylogic.eu',
      url='https://wiki.paylogic.eu/',
      packages=find_packages(),
      package_data={'py2deb': ['config/*.ini']},
      install_requires=['python-debian', 'stdeb'],
      entry_points={'console_scripts': ['py2deb = py2deb:main']})