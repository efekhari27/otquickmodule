# Easy Python Packaging *(7 steps to publish on PyPI)*


This document aims at giving a quick tutorial for structuring, packaging, and publishing your Python package on https://pypi.org/.

To illustrate this tutorial, let's work on ditribution of a full Python package called ```otquickmodule``` example, based on the following tutorial https://github.com/judy2k/publishing_python_packages_talk.  

Our illustrative package, ```otquickmodule```, includes two classes: 

- ```KernelHerding```
- ```BayesianQuadratureWeighting```

## **0. Create a new environment**
Before strating, creating a new environment for this occasion is highly recomanded to properly manage dependencies (we decided to name ours ```otqm_env```). For more information, check-out the conda environnments documentation https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html. 

```python
~$ conda create -n otqm_env python=3.9
~$ conda activate otqm_env
```

Do not forget to activate this environment for all the following steps.

## **1. Write ```__init__.py``` file**

This file will allow the auto-completion your methods when using the package. Note that the version defined here will be the package version (including on pypi).

```python
"""otquickmodule module"""

from .KernelHerding import KernelHerding
from .BayesianQuadratureWeighting import BayesianQuadratureWeighting

__all__ = [
    "KernelHerding",
    "BayesianQuadratureWeighting",
]
__version__ = "0.0.1"
```

## **2. Create the package structure**

Before creating the package structure, we recommand to follow a few good practices in Python: 

- Avoid unecessary dependancies to simplify package maintenancy
- Follow the PEP 8 coding standards and use the package ```black``` to format your code according to PEP 8.
- Write explicit docstrings on each method using the numpydoc syntax. This formalism will allow you to easily create a beautiful documentation in the future (e.g., https://efekhari27.github.io/otkerneldesign/master/) 

Here is the recommended Python package structure, do not foget to place the ```__init__.py``` file in the by the two classes.

```
PACKAGE STRUCTURE (step 2)
==========================
├── otquickmodule
|    ├── example
|    ├── test
|    ├── otquickmodule
|    |   ├── __init__.py
|    |   ├── BayesianQuadratureWeighting.py
|    |   └── KernelHerding.py
```

## **3. Add license, readme and gitignore files**

- The ```README.md``` file should describe the package and will appear on your github repository and your pypi page.  

- To help you choosing a license: https://choosealicense.com/. In our case, we chose a GPL license in the form of the file ```LICENSE```.

- To create a .gitignore file (to make sure git doesn't follow auxillary files): copy ours or check out https://www.toptal.com/developers/gitignore/

```
PACKAGE STRUCTURE (step 3)
==========================
├── otquickmodule
|    ├── example
|    ├── test
|    ├── otquickmodule
|    |   ├── __init__.py
|    |   ├── BayesianQuadratureWeighting.py
|    |   └── KernelHerding.py
|    ├── LICENSE
|    ├── README.md
|    └── .gitignore
```

## **4. Write a ```setup.py``` file**

The ```setup.py``` is the most important file for installing your package. Note that the ```name``` defined here will be the name published on pypi. 

```python
# coding: utf8
"""
Setup script for a Python package
"""
import os
import re
from setuptools import setup

# Get the version from __init__.py
path = os.path.join(os.path.dirname(__file__), 'otquickmodule', '__init__.py')
with open(path) as f:
    version_file = f.read()

version = re.search(r"^\s*__version__\s*=\s*['\"]([^'\"]+)['\"]",
                    version_file, re.M)
if version:
    version = version.group(1)
else:
    raise RuntimeError("Unable to find version string.")

# Long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="otquickmodule",
    version=version,
    author="Elias Fekhari",
    author_email="elias.fekhari@edf.fr",
    description="This repository is a turorial for easy Python packaging",
    license='GPLv3+',
    keywords=['OpenTURNS', 'KernelHerding'],
    url="https://github.com/efekhari27/otquickmodule",
    packages=['otquickmodule', 'test'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=[
          "numpy",
          "scipy", 
          "openturns>=1.17"
      ],
)
```

At this step, you should be able to run the following commands without error. It will first create a ```build``` repertory with the sources of your package. Then, you can try to install the package locally (the option ```-e``` imposes a local install). 

```bash 
~/otquickmodule$ pyton setup.py bdist_wheel
~/otquickmodule$ pip install -e .
```

You can now import the module from anywhere with the Python interpreter of the ```otqm_env``` conda environment: 

``` python
~$ conda activate otqm_env
~$ python 
>>> import otquickmodule as otqm
>>>
```

## **5. Write tests and examples**

Each class should have a corresponding test file. Tests can either be writen using the ```unittest``` or ```pytest``` package. ```pytest``` is very popular and present various practical features but requires to be added to the package requirements. For our needs, we chose to use the native Python module ```unnitest```.

Additionally, users appreciate to get started with a simple usage example which can be a ipython notebook file.

```
PACKAGE STRUCTURE (step 5)
==========================
├── otquickmodule
|    ├── build
|    |   ├── ...
|    |   └── ...
|    ├── example
|    |   └── kernel_herding_example.ipynb
|    ├── test
|    |   ├── TestBayesianQuadratureWeighting.py
|    |   └── TestKernelHerding.py
|    ├── otquickmodule
|    |   ├── __init__.py
|    |   ├── BayesianQuadratureWeighting.py
|    |   └── KernelHerding.py
|    ├── LICENSE
|    ├── README.md
|    ├── setup.py
|    └── .gitignore
```

At this step you can repeat the build and install commands from the previous step.

## **6. Build, distribute and publish**

Create the source distribution of the package: (creates a tar gz archive and the hosting ```dist``` repertory)

```bash
~/otquickmodule$ pyton setup.py bdist_wheel sdist
```

Check if it worked: (you should see the content of the archive) 

```bash
~/otquickmodule$ tar tzf dist/otquickmodule-0.0.1.tar.gz 
```

Create a PyPI account online and remember your username and password. 

Install the package ```twine```:

```bash
~/otquickmodule$ conda install twine
```

Publish the package on PyPI: 
```bash
~/otquickmodule$ twine upload dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: YOUR_USER_NAME
Enter your password: YOUR_PASSWORD
Uploading otquickmodule-0.0.1.tar.gz
100%|██████████████████████████████████████████████████████████████| 3.49k/3.49k [00:01<00:00, 2.17kB/s]

View at:
https://pypi.org/project/otquickmodule/0.0.1/
```

Your package is available online!

## **7. Try your package**

Create or switch to a different conda environment and install your package from pypi: 
```bash
~$ conda activate other_env
~$ pip install otquickmodule
```