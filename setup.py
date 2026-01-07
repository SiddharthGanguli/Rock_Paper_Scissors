from setuptools import setup, find_packages

setup(
    name="Rock_Paper_Scissors",
    version="1.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
