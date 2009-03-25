#!/usr/bin/env python
""" Test for pyfse

    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import import_wrapper
from pyfse import *
    
table = {   ('', None):             ('state_a', None),
            ('state_a', 'event_a'): ('state_b', None),
            ('state_b', 'event_b'): ('state_c', None),
            ('state_c', None):      ('state_a', None)
         }

class ExampleController(Controller):
    """
    """
    def __init__(self, table):
        Controller.__init__(self, table)
        
    def enter_state_a(self, event, *pargs):
        print "Enter StateA"
        
    def leave_state_a(self):
        print "Leave StateA"

    def enter_state_b(self, event, *pargs):
        print "Enter StateB"
        
    def leave_state_b(self):
        print "Leave StateB"

    def enter_state_c(self, event, *pargs):
        print "Enter StateC %s" % pargs
        
    def leave_state_c(self):
        print "Leave StateC"
        
    def enter_TRAP(self, event, *pargs):
        print "enter TRAP"
        
    def action_START(self, event, *pargs):
        print "action_START"
        

def tests(self):
    """
    Normal testing + unknown transition exception testing
    
    >>> c = ExampleController(table)
    >>> c('start')
    Enter StateA
    >>> c('event_a')
    Leave StateA
    Enter StateB
    >>> c('event_b','test')
    Leave StateB
    Enter StateC ('test',)
    >>> c('whatever')
    Leave StateC
    Enter StateA
    >>> c('unknown')
    Traceback (most recent call last):
    ...
    pyfseException: msg[error_transition_missing] params[{'current_state': 'state_a', 'event': 'unknown'}]
    """

def Trap(event):
    print "Trap event[%s]" % event


table2 = {   ('', None):            ('state_a', 'action_START'),
            ('state_a', 'event_a'): ('state_b', None),
            ('state_b', 'event_b'): ('state_c', None),
            ('state_c', None):      ('state_a', None),
            (None, 'event_trap'):   ('TRAP',    Trap)
         }

def tests2(self):
    """
    Attractor Match testing
    
    >>> c = ExampleController(table2)
    >>> c('start')
    Enter StateA
    action_START
    >>> c('event_trap')
    Leave StateA
    enter TRAP
    Trap event[event_trap]
    """

# ==============================================
# ==============================================

import doctest
doctest.testmod()
   
