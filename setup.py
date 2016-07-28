from setuptools import setup

name = 'prettytraceback'

import imp
_version = imp.load_source('%s._version' % name, '%s/_version.py' % name)

setup(
    name=name,
    version=_version.version,
    author='Tom Flanagan',
    author_email='tom@zkpq.ca',
    license='MIT',
    # url='https://github.com/Knio/pynmea2',

    description='Python plugin for enabling pretty tracebacks',
    packages=[name],
    keywords='python traceback cgitb color colors pretty shel tool ipython ultratb',

    install_requires=[
          'IPython',
    ],

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
