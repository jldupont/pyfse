#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

TO_RENDER = [('pyfse.controller','Controller'),]

import os
import sys
import tempfile
import webbrowser

from docutils.core import publish_string

# adjust system path to the development environment
# =================================================
trunk   = os.path.dirname( os.path.abspath( __file__ ) )
sys.path.append( trunk )


def renderReSText(input, justBody = False):
    """ Returns a rendered ReSTructuredText string
    """
    parts = publish_string(source=input, writer_name="html")
       
    return parts

def writeReSText( text ):
    ""
    uniqueName = os.tempnam() + ".html"
    file = open(uniqueName, "w+b")
    name = file.name
    file.write( text )
    file.close()
    return name
    

for item in TO_RENDER:
    moduleName, objectName = item
    
    module = __import__( moduleName )
    
    obj = getattr( module, objectName )
    doc = obj.__doc__
    
    rendered = renderReSText( doc )
    
    fileName = writeReSText(rendered )
    
    webbrowser.open( fileName , moduleName )
    