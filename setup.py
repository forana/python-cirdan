#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="cirdan",
    version="1.1.1",
    description="Decorator-based documentation generation for Falcon-based web applications.",
    url="https://github.com/forana/python-cirdan",
    author="Alex Foran",
    author_email="alex@alexforan.com",
    packages=find_packages(),
    install_requires=[
        "Jinja2==2.7.3",
        "falcon==0.3.0"
    ],
    include_package_data=True,
    package_data={
        'cirdan': ['default.jinja2'],
        'canned_environments': ['*.json']
    }
)
