from setuptools import setup
import re

with open('ioc_relay/__init__.py') as file:
    version = re.search(r"__version__ = '(.*)'", file.read()).group(1)

setup(
    name='ioc-relay',
    version=version,
    license='MIT',
    author='Robbie Clarken',
    author_email='robbie.clarken@gmail.com',
    packages=['ioc_relay'],
    install_requires=[
        'websockets',
        'pyepics',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'ioc-relay=ioc_relay.ws_server:main',
        ],
    },
)
