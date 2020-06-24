#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
#############################################
# File Name: setup.py
# Author: ffxw0720
# Mail: feifanxiaowang@163.com
# Created Time: 2020-6-24 17:30:00
#############################################
 
 
from setuptools import setup, find_packages
 
setup(
  name = "musen",
  version = "1.0.0",
  keywords = ("pip", "musen", "ffxw0720"),
  description = "musen file processing library produced by musen team",
  long_description = "musen file processing library produced by musen team",
  license = "MIT Licence",
 
  url = "https://github.com/fengmm521/pipProject",
  author = "mage",
  author_email = "mage@woodcol.com",
 
  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = []
)