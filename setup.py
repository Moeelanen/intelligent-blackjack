from setuptools import setup, find_packages

setup(
    name="intelligent-dealer",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework'
    ]
)
