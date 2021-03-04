#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='BaOIA',
      version='0.1',
      url='https://github.com/baoia/scripts',
      description='Boîte à outils d\'Intelligence artificielle',
      packages=find_packages(exclude=['exps*']),
      project_urls={
          'Paper': 'https://arxiv.org/abs/1804.10371',
          'Source Code': 'https://github.com/dhlab-epfl/dhSegment'
      },
      scripts=['recup_genre.py'],
      install_requires=[
        'wptools==0.1.6',
        'simplejson==3.17.2'
      ],
      zip_safe=False)
