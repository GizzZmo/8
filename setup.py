#!/usr/bin/env python3
"""Setup script for OSI Blockchain Simulation."""

from setuptools import setup, find_packages
import os

# Read the README file
def read_file(filename):
    """Read file contents."""
    with open(filename, encoding='utf-8') as f:
        return f.read()

# Get version from git or use default
def get_version():
    """Get version from git tags or use default."""
    try:
        import subprocess
        version = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0'], 
                                         stderr=subprocess.DEVNULL).decode().strip()
        return version.lstrip('v')
    except Exception:
        return '0.1.0'

setup(
    name='osi-blockchain-simulation',
    version=get_version(),
    description='OSI Model Blockchain Simulation with all 7 layers',
    long_description=read_file('readme.md') if os.path.exists('readme.md') else '',
    long_description_content_type='text/markdown',
    author='GizzZmo',
    url='https://github.com/GizzZmo/8',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=[
        # No external dependencies - uses Python standard library only
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'flake8>=6.1.0',
            'pylint>=3.0.0',
            'black>=23.0.0',
        ],
        'docs': [
            'sphinx>=7.2.0',
            'sphinx-rtd-theme>=1.3.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'osi-simulate=osi_blockchain_simulation.main_simulation:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
    keywords='osi-model blockchain simulation networking education',
    project_urls={
        'Bug Reports': 'https://github.com/GizzZmo/8/issues',
        'Source': 'https://github.com/GizzZmo/8',
    },
)
