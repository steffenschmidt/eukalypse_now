#!/usr/bin/env python
"""
eukalypse_now

:copyright: (c) 2012 Dennis Schwertel, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages


tests_require = [
]

dependency_links = [
    'http://github.com/kinkerl/eukalypse/tarball/master#egg=eukalypse'
]


install_requires = [
    'south',
    'sphinx',
    'pil',
    'raven',
    'logan',
    'gunicorn',
    'eukalypse'

]

setup(
    name='eukalypse_now',
    version='0.1',
    author='Dennis Schwertel',
    author_email='s@digitalkultur.net',
    description='eukalypse web server',
    long_description=__doc__,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links = dependency_links,
    license='BSD',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'eukalypse_now = eukalypse_now.utils.runner:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)