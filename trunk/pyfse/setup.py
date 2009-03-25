""" pyfse: python finite state engine (machine)
"""
__author__  = "Jean-Lou Dupont"
__version__ = "0.0.5"
__email__   = "python (at) jldupont.com"

__desc__    = """
This project consists in helper classes used to design FSM (Finite State Machines) from pure python classes. 

Example usage is included in /tests. Additional documentation can be found in doc_.

Changelog
---------

**0.0.6**

Added 


**0.0.5**

Added support for more `action_method`


**0.0.4**

* Backward compatibility breakage
  
 * Added `action_method` support to `transition table`

**0.0.3**

* Added the 'attractor' transition

**0.0.2**

* Removed unnecessary imports 

**0.0.1** 

Initial alpha release

.. _SVN: http://pyfse.googlecode.com/
.. _doc: http://pyfse.googlecode.com/svn/trunk/pyfse/docs/html/index.html
"""

__doc_url__ = """http://pyfse.googlecode.com/"""

import sys
import os.path
from setuptools import setup, find_packages

__classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    ]

__dependencies = []

setup(
    name = "pyfse",
    description      = __doc__,
    author_email     = __email__,
    author           = __author__,
    url              = __doc_url__,
    long_description = __desc__,
    version          = __version__,
    package_data     = {'':['*.*']},
    packages         = find_packages(),
    classifiers      = __classifiers,
    install_requires = __dependencies,
    zip_safe         = True,
)
