#!/usr/bin/env python

from setuptools import setup
from join import __version__

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
with open('requirements.txt') as f:
    requirements = f.read().split('\n')

setup(
    name='join command',
    version=__version__,
    description='join command in O(1) memory',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Michał Dobranowski',
    author_email='mdbrnowski@gmail.com',
    packages=['join', 'join.utils'],
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts': ['join=join.main:main']},
)
