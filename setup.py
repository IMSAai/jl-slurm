#!/usr/bin/env python3
# -*- encoding: utf-8 -

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "jl-slurm",
    version = "1.0.0",
    author = "EpochML",
    author_email = "webmaster@epochml.org",
    maintainer = "EpochML",
    maintainer_email = "webmaster@epochml.org",
    description = ("Scheduler for Jupyter Notebook on SLURM clusters where compute nodes are hidden behind head/login nodes"),
    license = "BSD",
    platforms=['Linux'],
    project_urls={
        "Bug Tracker": "https://github.com/epochml/jup_sched/issues",
        "Documentation": "https://github.com/epochml/jup_sched/blob/master/README.md",
        "Source Code": "https://github.com/epochml/jup_sched/",
    },
    keywords = "slurm python development jupyterlab",
    url = "https://github.com/epochml/jup_sched",
    scripts=['jl-slurm'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)