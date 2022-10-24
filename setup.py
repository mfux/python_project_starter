"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="wsboyt",
    version="0.1",
    packages=["wsboyt"],
    package_dir={"": "src"},
    install_requires=["pytest==7.1.3", "black==22.10.0"],
)
