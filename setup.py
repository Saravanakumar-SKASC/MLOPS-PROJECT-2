from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mlops-project-2",
    version="0.0.1",
    description="MLOps Project 2",
    author="SAR",
    author_email="ofysar@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
)