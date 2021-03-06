#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import shutil
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

# this package
from __pkginfo__ import *  # pylint: disable=wildcard-import

setup(
		description="Backport of pprint from Python 3.9 to Python 3.6-3.8",
		extras_require=extras_require,
		install_requires=install_requires,
		py_modules=[],
		version=__version__,
		)

shutil.rmtree("pprint36.egg-info", ignore_errors=True)
