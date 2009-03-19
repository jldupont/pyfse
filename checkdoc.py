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

from docutils.core import publish_parts

# adjust system path to the development environment
# =================================================
trunk   = os.path.dirname( os.path.abspath( __file__ ) )
sys.path.append( trunk )


def renderReSText(input, justBody = False):
    """ Returns a rendered ReSTructuredText string
    """
    parts = publish_parts(source=input, writer_name="html4css1",parser_name='restructuredtext')
    
    if justBody:
        rendered_page = parts["fragment"]
    else:
        rendered_page = parts["html_title"] + parts["html_subtitle"] + parts["fragment"]
    
    return rendered_page

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
    
    fileName = writeReSText(doc )
    
    webbrowser.open( fileName , moduleName )
    