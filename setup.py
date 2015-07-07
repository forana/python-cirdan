#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt", 'r') as file:
    setup(name="cirdan",
        version="1.1.0",
        description="Decorator-based documentation generation for Falcon-based web applications.",
        url="https://github.com/forana/python-cirdan",
        author="Alex Foran",
        author_email="alex@alexforan.com",
        packages=find_packages(),
        install_requires=file.readlines(),
        include_package_data=True,
        package_data={
            'cirdan': ['default.jinja2'],
            'canned_environments': ['*.json']
        }
    )
