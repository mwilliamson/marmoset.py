#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='marmoset',
    version='0.1.0',
    description='Convert Python values, such as lists and dicts, into human-friendly strings',
    long_description=read("README"),
    author='Michael Williamson',
    author_email='mike@zwobble.org',
    url='http://github.com/mwilliamson/marmoset.py',
    packages=['marmoset'],
)
