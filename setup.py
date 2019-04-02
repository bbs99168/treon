# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('treon/treon.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "treon",
    packages = ["treon"],
    entry_points = {
        "console_scripts": ['treon = treon.treon:main']
    },
    version = version,
    description = "Testing framework for Jupyter Notebooks",
    long_description = long_descr,
    author = "Amit Rathi",
    author_email = "amit@reviewnb.com",
    url = "https://reviewnb.com",
    install_requires=[
        'nbconvert',
        'jupyter_client',
        'jupyter',
        'docopt'
    ]
    )
