import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="encoding_dot_com-encodingapi",
    version="0.0.1",
    description=("Encoding.dom Python API"),
    license="",
    keywords="encoding.com transcoding",
    url="",
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "*.examples", "example*"]),
    long_description=read('README.md'),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: No Input/Output (Daemon)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7"
    ],
)
