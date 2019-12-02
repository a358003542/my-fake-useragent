#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
from setuptools import setup, find_packages
import my_fake_useragent

REQUIREMENTS = []

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='my_fake_useragent',
    version=my_fake_useragent.__version__,
    description='create a fake useragent',
    url='https://github.com/a358003542/my-fake-useragent',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer='wanze',
    maintainer_email='a358003542@gmail.com',
    license='MIT',
    keywords=['useragent', 'python'],
    classifiers=['Development Status :: 4 - Beta',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX :: Linux',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3', ],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    setup_requires=REQUIREMENTS,
    install_requires=REQUIREMENTS,
)
