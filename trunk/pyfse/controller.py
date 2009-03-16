#!/usr/bin/env python
""" pyfse.Controller

    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from types import *




class pyfseException(Exception):
    """ pyfse Exception base class 
    """
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.params = params
        



class Controller(object):
    """ Base class
    
        Transition Table
        ================
        
        List consisting of:
            [current_state, event, next_state]
            
        Upon leaving the current_state, the method 'leave_STATE'
        will be called. Upon entering the next_state, the method
        'enter_STATE' will be called.
        
        The format of the parameter 'event': 
            (unique_string, ...)
    """
    
    _enter_prefix = "enter_"
    _leave_prefix = "leave_"
    
    def __init__(self, transition_table, start_state):
        self.transition_table = transition_table
        self.current_state = start_state
    
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
        raise AttributeError("pyfse.Controller.__getattr__: name[%s]" % name)
        
    def __call__(self, event, *pargs):
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
        next_state = self._lookup(event)
        
        #3
        enter_method = "%s%s" % (self._enter_prefix, next_state)
        result = getattr(self, enter_method)(event, pargs)
        
        #4#
        self.current_state = next_state
        
        #5
        return result

    def _lookup(self, event):
        """ Look up the next_state based on [current_state;event]
        
            @return: next_state
        """
        #direct match
        tuple_dm = (self.current_state, event)        
        dm = self.transition_table.get( tuple_dm, None )
        if dm is not None:
            return dm
        
        #wildcard match
        tuple_wm = (self.current_state, None)
        wm = self.transition_table.get(tuple_wm, None)
        if wm is not None:
            return wm
        
        self._raiseException('error_transition_missing', event)

    def _raiseException(self, msg, event = None):
        """ Raises an exception.
            Convenience method.
        """
        params = {'current_state':self.current_state, 'event':event}
        raise pyfseException(msg, params)

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    table = {   ('state_a', 'event_a'): 'state_b',
                ('state_b', 'event_b'): 'state_c',
                ('state_c', None): 'state_a'
             }
    
    class ExampleController(Controller):
        """
        """
        def __init__(self, table, start_state):
            Controller.__init__(self, table, start_state)
            
        def enter_state_a(self, event, *pargs):
            print "Enter StateA"
            
        def leave_state_a(self):
            print "Leave StateA"
    
        def enter_state_b(self, event, *pargs):
            print "Enter StateB"
            
        def leave_state_b(self):
            print "Leave StateB"

        def enter_state_c(self, event, *pargs):
            print "Enter StateC"
            
        def leave_state_c(self):
            print "Leave StateC"

    def tests(self):
        """
        >>> c = ExampleController(table, 'state_a')
        >>> c('event_a')
        >>> c('event_b')
        >>> c('whatever')
        """

# ==============================================
# ==============================================

    import doctest
    doctest.testmod()

