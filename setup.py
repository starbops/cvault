"""A setuptools based setup module
"""
from setuptools import setup, find_packages
from codecs import open

import os
import sys

version = '0.1.2'

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    os.system('python3 setup.py bdist_wheel upload')
    os.system("git tag -s {} -m 'version {}'".format(version, version))
    os.system('git push --tags')
    sys.exit()

here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='cvault',
        version=version,
        description='Credential Vault',
        long_description = long_description,
        url='https://github.com/starbops/cvault',
        author='Zespre Schmidt',
        author_email='starbops@zespre.com',
        license='MIT',
        platforms='any',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: End Users/Desktop',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
        keywords='credential memo',
        packages=find_packages(exclude=['tests']),
        install_requires=['docopt'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        #test_suite='tests',
        entry_points={
            'console_scripts': [
                'cvault=cvault:main',
            ],
        },
)
