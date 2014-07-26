# Jordan Cazamias
# CFDG Optimizer
# July 2014

from setuptools import setup

setup(
    name='cfdg-optimizer',
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cfdgo=cli:cli
    '''
)