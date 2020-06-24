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
  version = "1.0.7",
  keywords = ("pip", "musen", "ffxw0720"),
  description = "musen file processing library produced by musen team.",
  long_description = "musen file processing library produced by musen team.Welcome to the http://musendocs.musen.teamview usage documents!© 2020 musen",
  license = "GPL-3.0 License",
 
  url = "https://github.com/FFXW0720/musen",
  author = "ffxw0720",
  author_email = "feifanxiaowang@163.com",
 
  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = [],

  classifiers=[   # 只适用于python3，若构建python2包，请移除
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)