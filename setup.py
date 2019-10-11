#!/usr/bin/env python

from glob import glob

from setuptools import find_packages

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='gsuitefy-admin',
     version='1.0.0',
     scripts=['gsuitefy-admin'],
     author="Marcos Alexandre Vidolin de Lima",
     author_email="marcosvidolin@gmail.com",
     description="Gsuite Admin client to manage users and groups",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/marcosvidolin/gsuitefy-admin",
     packages=find_packages('src'),
     package_dir={'': 'src'},
     py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )