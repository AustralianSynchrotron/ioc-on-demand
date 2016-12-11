from setuptools import setup
import re

with open('ioc_launcher/__init__.py') as file:
    version = re.search(r"__version__ = '(.*)'", file.read()).group(1)

setup(
    name='ioc-launcher',
    version=version,
    license='MIT',
    author='Robbie Clarken',
    packages=['ioc_launcher'],
    install_requires=[
        'aiohttp',
        'docker-py',
    ],
    entry_points={
        'console_scripts': [
            'ioc-launcher=ioc_launcher.app:main',
        ],
    },
)
