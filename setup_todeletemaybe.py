import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="project",
    version="0.0.1",
    description="Project description",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/maximlt/project",
    author="Maxime Liquet",
    author_email="maximeliquet@free.fr",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["project"],
    include_package_data=True,
    install_requires=[],
)
