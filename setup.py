import os
from setuptools import setup, find_packages


setup(
    name=os.getenv('APP_NAME', 'app'),
    version=os.getenv('APP_VERSION', '1.0.0'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
    ],
)
