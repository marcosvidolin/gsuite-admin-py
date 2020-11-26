#!/usr/bin/env python

from glob import glob

from setuptools import find_packages

import setuptools

install_requires = [
    'google-api-python-client==1.12.8',
    'google-auth-httplib2==0.0.3',
    'google-auth-oauthlib==0.4.1',
    'oauth2client==4.1.3'
]

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='gsuitefy',
     version='1.1.1',
     scripts=['gsuitefy'],
     author="Marcos Alexandre Vidolin de Lima",
     author_email="marcosvidolin@gmail.com",
     description="Gsuite Admin client to manage users and groups",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/marcosvidolin/gsuitefy",
     install_requires=install_requires,
     packages=find_packages('src'),
     package_dir={'': 'src'},
     py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3.4",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )