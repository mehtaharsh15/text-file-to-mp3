#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0', 'gTTS'
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(shridarpatil): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='text_file_to_audio',
    version='0.1.0',
    description="Converts a text file to mp3",
    long_description=readme + '\n\n' + history,
    author="Shridhar Patil",
    author_email='shridharpatil2792@gmail.com',
    url='https://github.com/shridarpatil/text_file_to_audio',
    packages=find_packages(include=['text_file_to_audio']),
    entry_points={
        'console_scripts': [
            'text_to_audio=text_file_to_audio.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='text_file_to_audio',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
