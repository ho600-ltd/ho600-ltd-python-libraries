#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ho600-ltd-python-libraries",
    version="0.0.1",
    author="ho600 Ltd.",
    author_email="libraries@ho600.com",
    description="Utils and Libraries collection from ho600 Ltd.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ho600-ltd/ho600-ltd-python-libraries",
    packages=setuptools.find_packages(),
    platforms=['any'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
