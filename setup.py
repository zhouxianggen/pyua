#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pyua',
        version = '1.0',
        install_requires = ['psutil'], 
        description = 'user agency',
        url = 'https://github.com/zhouxianggen/pyua', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['pyua'],
        data_files = [ ],  
        entry_points = { }   
        )
