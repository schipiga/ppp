"""
Python project proto

@author chipiga86@gmail.com
"""

from setuptools import setup, find_packages

setup(
    name='python-project-proto',
    version='0.0.1',
    description='Simple example how to build python project with good style',
    long_description=open('README.rst').read(),
    author='Sergei Chipiga',
    author_email='chipiga86@gmail.com',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/schipiga/ppp',
    install_requires=[
        'requests==2.21.0',
        'beautifulsoup4==4.7.1',
        'PyYAML==3.13',
    ],
    entry_points={
        "console_scripts": [
            "links = ppp.cli:main",
        ],
    },
)
