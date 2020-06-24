
#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="detection",
	version="0.1",
	description="Test for pip install git+",
	url="https://github.com/ryotaro-aoyama/tf-eager-fasterrcnn",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	test_a_f = 
detection.detection:main
	""",
	)
