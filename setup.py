#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='blockmarket',
    version='1.0',
    description='Basic Blockheads Blockmarket Library',
    author='Wingysam',
    url='https://github.com/Wingysam/blockmarket',
    packages=['blockmarket'],
    requires=['requests', 'json', 'html.parser']
)
