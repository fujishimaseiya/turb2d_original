# -*- coding: utf-8 -*-
import numpy as np
from Cython.Build import cythonize
from setuptools import setup, Extension, find_packages

with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

ext_neighbors_at_link = Extension(
    "_neighbors_at_link",
    sources=["turb2d/_neighbors_at_link.pyx"],
    include_dirs=[np.get_include()],
)

setup(
    name="turb2d",
    version="0.3.0",
    description="2D shallow water model for turbidity currents",
    long_description=readme,
    author="Hajime Naruse",
    author_email="naruse@kueps.kyoto-u.ac.jp",
    url="https://github.com/narusehajime/turb2d.git",
    license=license,
    install_requires=[
        "cython",
        "numpy",
        "scipy",
        "landlab==2.4.1",
        "matplotlib",
        "gdal==3.6.4",
        "tqdm",
    ],
    ext_modules=cythonize([ext_neighbors_at_link]),
    packages=find_packages(exclude=("tests", "docs")),
)
