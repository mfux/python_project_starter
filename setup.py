"""Package configuration."""
from setuptools import setup

setup(
    name="pythonprojectstarter",
    version="0.1",
    packages=["pythonprojectstarter"],
    package_dir={"": "src"},
    install_requires=["pytest==7.1.3", "black==22.10.0"],
)
