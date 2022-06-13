# coding: utf8
"""
Setup script for a Python package
=================================
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
    description="This repository is a tutorial for quick Python packaging",
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