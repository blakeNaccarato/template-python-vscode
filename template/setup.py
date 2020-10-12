"""
Package description.
"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path().resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="package",
    version="0.0.0",
    description=("Package description."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/<user>/<repo>",
    author="<user>",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
)
