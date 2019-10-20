import sys, requests
from setuptools import setup, find_packages
import shutil, os

setup(
    name='pystickynote',
    version='1.1.1',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='Easy Sticky Note Widgets',
    long_description="""\
# PyStickynote

### Easily give yourself a sticky note to write to and load using PySimpleGUI. Customization options for background_color, text_color, and alpha!""",
    long_description_content_type='text/markdown',
    url='https://github.com/M4cs/pystickynote',
    packages=['pystickynote'],
    install_requires=[
        'PySimpleGUIQt',
        'PyQt5',
        'PySide2'
    ],
    project_urls={
        'Discord Server': 'https://discordapp.com/invite/7VN9VZe'
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'pystickynote = pystickynote.__main__:main',
        ],
    },
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)