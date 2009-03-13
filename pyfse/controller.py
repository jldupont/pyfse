#!/usr/bin/env python
""" pyfse.Controller

    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from types import *

class Controller(object):
    """ Base class
    """
    #__metaclass__ = MetaController
    
    _enter_prefix = "enter_"
    _leave_prefix = "leave_"
    
    def __init__(self, transition_table = None):
        self.transition_table = transition_table
        self.current_state = None
    
    def __getattr__(self, name):
        """ Trap for the special methods
            e.g. enter_X  leave_X
            
            If we get here, that surely means the called method 
            is not found; if it is one of enter_ or leave_ then 
            return without raising an exception.
        """
        if name.startswith(self._enter_prefix):
            return None
        if name.startswith(self._leave_prefix):
            return None
        raise AttributeError("Controller.__getattr__: name[%s]" % name)
        
    def __call__(self, input):
        """ Event Handler entry point
        
            1. Call the leave_X method where X is the current_state
            2. Look-up next_state based on [current_state;input]            
            3. Call the enter_Y method where Y is the next_state
            4. current_state <- next_state
            5. Return the result
        """
        #1
        leave_method = "%s%s" % (self._leave_prefix, self.current_state)
        getattr(self, leave_method)()
        
        #2
        next_state = self._lookup(input)
        
        #3
        enter_method = "%s%s" % (self._enter_prefix, next_state)
        result = getattr(self, enter_method)(input)
        
        #4#
        self.current_state = next_state
        
        #5
        return result

    def _lookup(self, input):
        """
        """

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    class ExampleController(Controller):
        """
        """
        def __init__(self):
            Controller.__init__(self)
            print "ExampleController.__init__"
            
        def enter_StateA(self):
            print "Enter StateA"
            
        def leave_StateA(self):
            print "Leave StateA"
    
        def enter_StateB(self):
            print "Enter StateB"
            
        def leave_StateB(self):
            print "Leave StateB"


    def tests(self):
        """
        >>> c = ExampleController()
        >>> ExampleController.dump()
        """

# ==============================================
# ==============================================

    import doctest
    doctest.testmod()

