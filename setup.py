from setuptools import setup
import re

with open('ttmltosrt/__init__.py') as file:
    version = re.search(r"__version__ = '(.*)'", file.read()).group(1)

setup(
    name='ttmltosrt',
    version=version,
    description='Convert Timed Text Markup Language to SRT',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Robbie Clarken',
    author_email='robbie.clarken@gmail.com',
    url='https://github.com/RobbieClarken/ttmltosrt',
    packages=['ttmltosrt'],
    install_requires=[
        'beautifulsoup4>=4.4.1',
        'click>=6.2',
    ],
    entry_points={
        'console_scripts': ['ttmltosrt=ttmltosrt.ttmltosrt:convert_file']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
)
