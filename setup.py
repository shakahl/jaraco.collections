#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import io
import sys

import setuptools

with io.open('README.txt', encoding='utf-8') as readme:
	long_description = readme.read()
with io.open('CHANGES.txt', encoding='utf-8') as changes:
	long_description += '\n\n' + changes.read()

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []

setup_params = dict(
	name='jaraco.collections',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="jaraco.collections",
	long_description=long_description,
	url="https://bitbucket.org/jaraco/jaraco.collections",
	packages=setuptools.find_packages(),
	install_requires=[
		'jaraco.text',
		'jaraco.classes',
		'six',
	],
	setup_requires=[
		'hgtools',
		'sphinx',
	] + pytest_runner,
	tests_require=[
		'pytest',
	],
	license='MIT',
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)