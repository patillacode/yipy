"""Packaging."""
from codecs import open
from os.path import abspath
from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup

from yipy import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='yipy',
    version=__version__,
    description='A python wraper for Yify\'s API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/patillacode/yipy',
    author='Patilla Code',
    author_email='patillacode@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='yify, api, python',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['requests'],
    extras_require={},
    entry_points={},
    cmdclass={},
)
