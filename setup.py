# Jordan Cazamias
# CFDG Optimizer
# July 2014

from setuptools import setup
from setuptools import find_packages

setup(
    name='cfdg-optimizer',
    version='1.0',
    author='Jordan Cazamias',
    author_email='jacazamias@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pillow',
        'numpy',
        'scipy',
        'pyssim',
        'python-Levenshtein'
    ],
    entry_points={
        'console_scripts':
            [
                'cfdgo = cfdg_optimizer.cli:main'
            ]
    }
)