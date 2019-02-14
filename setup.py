"""
Python project proto

@author chipiga86@gmail.com
"""

from setuptools import setup, find_packages

setup(
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests==2.21.0",
        "beautifulsoup4==4.7.1",
        "PyYAML==3.13",
    ],
)
