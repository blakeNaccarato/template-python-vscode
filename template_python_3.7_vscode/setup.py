"""
Package description.
"""

from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="package_name",
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
