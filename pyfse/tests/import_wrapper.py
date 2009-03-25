#!/usr/bin/env python
""" Import Wrapper

    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys

#============================================================================
# DO NOT TOUCH BELOW HERE
#============================================================================

def _findTrunk( path=os.path.dirname( os.path.abspath( __file__ ) ) ):
    
    trunk = path+'/trunk'
    if os.path.exists( trunk ):
        return trunk
    
    oneUp = os.path.dirname( path )
    return _findTrunk( oneUp )


trunk = _findTrunk()
sys.path.append( trunk+'/pyfse' )
