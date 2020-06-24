
#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="tf-eager-fasterrcnn",
	version="0.1",
	description="Test for pip install git+",
	url="https://github.com/ryotaro-aoyama/tf-eager-fasterrcnn/new/master",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	test_a_f = 
tf-eager-fasterrcnn.tf-eager-fasterrcnn:main
	""",
	)
