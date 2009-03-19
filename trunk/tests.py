#!/usr/bin/env python
""" Automated unittest runner
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys
import unittest
import doctest
from types import *

# ONLY CHANGE THE FOLLOWING:
_thislib_name = 'pyfse'

#============================================================================
# DO NOT TOUCH BELOW HERE
#============================================================================

try:
    thislib = __import__(_thislib_name)
except:
    #for the development environment
    trunk   = os.path.dirname( os.path.abspath( __file__ ) )
    sys.path.append( trunk )
    
    try:
        thislib = __import__(_thislib_name)
    except:
        raise RuntimeError("Cannot locate %s package" % _thislib_name)
        sys.exit(0)

modules = filter(lambda X: type(thislib.__getattribute__(X)) is ModuleType, thislib.__dict__)
modules = map(lambda X: "%s.%s" % (_thislib_name, X), modules)

print "Modules under test: %s" % modules

suite = unittest.TestSuite()
for mod in modules:
    suite.addTest(doctest.DocTestSuite(mod))
runner = unittest.TextTestRunner()
runner.run(suite)