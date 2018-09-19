"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gsuite-exporter',
    version='0.0.1',
    description='GSuite Admin API Exporter',
    long_description=long_description,
    author='Google Inc.',
    author_email='ocervello@google.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='gsuite exporter stackdriver',
    install_requires=[
        'google-api-python-client',
        'python-dateutil',
        'oauth2client'
    ],
    entry_points={
        'console_scripts': [
            'gsuite-exporter=gsuite_exporter.cli:main',
        ],
    },
)