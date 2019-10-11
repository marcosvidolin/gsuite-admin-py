# Steps to publish

## Setup

- Install the required packages

```shell
sudo python -m pip install --upgrade pip setuptools wheel
sudo python -m pip install tqdm
sudo python -m pip install --user --upgrade twine
```

- Create the Pypirc file (~/.pypirc) to stores the PyPi repository information

```shell
[distutils] 
index-servers=pypi
[pypi] 
repository=https://upload.pypi.org/legacy/ 
username=[MY-USER-NAME]
```

## Compiling the Package
  
```shell
python setup.py bdist_wheel
```

## Install on Your Local Machine (to test)

```shell
python -m pip install dist/gsuitefy-1.0.0-py2-none-any.whl
```

## Upload on pip

```shell
python -m twine upload dist/*
```

## Thanks to

[Build Your First pip Package](https://dzone.com/articles/executable-package-pip-install)
