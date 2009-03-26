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
            ('state_a', 'to_d'):    ('state_d', None),
            ('state_b', 'event_b'): ('state_c', None),
            ('state_c', None):      ('state_a', None),
            ('state_d', 'to_e'):    ('state_e', None),
         }

class ExampleController(Controller):
    """
    """
    def __init__(self, table, actions = None):
        Controller.__init__(self, table, actions)
        self._debug = True
        
    def enter_state_a(self, event, *pargs, **kargs):
        print "Enter StateA"
        
    def leave_state_a(self):
        print "Leave StateA"

    def enter_state_b(self, event, *pargs, **kargs):
        print "Enter StateB"
        
    def leave_state_b(self):
        print "Leave StateB"

    def enter_state_c(self, event, *pargs, **kargs):
        print "Enter StateC: type pargs[%s]" % type(pargs)
        
    def leave_state_c(self):
        print "Leave StateC"
        
    def enter_state_d(self, event, *pargs, **kargs):
        print "Enter StateD: type pargs[%s] pargs[%s]" % (type(pargs), pargs)
        
    def leave_state_d(self):
        print "Leave StateD"

    def enter_state_e(self, event, *pargs, **kargs):
        print "Enter StateE: pargs[%s] kargs[%s]" % (str(pargs), str(kargs))
                
    def enter_state_v(self, event, *pargs, **kargs):
        print "Enter StateV"
    
        
    def enter_TRAP(self, event, *pargs, **kargs):
        print "enter TRAP"
        
    def action_START(self, event, *pargs, **kargs):
        print "action_START"
        

def tests():
    """
    Normal testing + unknown transition exception testing
    
    >>> c = ExampleController(table)
    >>> c('start')
    default_leave
    Enter StateA
    >>> c('event_a')
    Leave StateA
    Enter StateB
    >>> c('event_b','param1', 'param2') # test with parameter
    Leave StateB
    Enter StateC: type pargs[<type 'tuple'>]
    >>> c('whatever')
    Leave StateC
    Enter StateA
    >>> c('unknown')
    Traceback (most recent call last):
    ...
    pyfseException: msg[error_transition_missing] params[{'current_state': 'state_a', 'event': 'unknown'}]
    >>> c('to_d', 'param1', 'param2')
    Leave StateA
    Enter StateD: type pargs[<type 'tuple'>] pargs[('param1', 'param2')]
    >>> c('to_e', param1='value1')
    Leave StateD
    Enter StateE: pargs[()] kargs[{'param1': 'value1'}]
    """

def Trap(event):
    print "Trap event[%s]" % event


table2 = {   ('', None):            ('state_a', 'action_START'),
            ('state_a', 'event_a'): ('state_b', None),
            ('state_b', 'event_b'): ('state_c', None),
            ('state_c', None):      ('state_a', None),
            (None, 'event_trap'):   ('TRAP',    Trap)
         }

def tests2():
    """
    Attractor Match testing
    
    >>> c = ExampleController(table2)
    >>> c('start')
    default_leave
    Enter StateA
    action_START
    >>> c('event_trap')
    Leave StateA
    enter TRAP
    Trap event[event_trap]
    """

class Actions(object):
    
    def A(self, event, *pargs, **kargs):
        print "action_A: event[%s] pargs[%s]" % (event, pargs)
        
    def V(self, event, *pargs, **kargs):
        print "action_V: event[%s] pargs[%s]" % (event, pargs)
        
    def W(self, event, *pargs, **kargs):
        print "action_W: event[%s] pargs[%s] kargs[%s]" % (event, pargs, kargs)
        

table3 = {  ('', None):             ('state_a', 'A'),
            ('state_a', 'to_v'):    ('state_v', 'V'),
            ('state_v', None):      ('state_y', 'Y'),
            ('state_v', 'to_w'):    ('state_w', 'W'),
         }


def test3():
    """
    >>> a = Actions()
    >>> c = ExampleController(table3, a)
    >>> c('start')
    default_leave
    Enter StateA
    action_A: event[start] pargs[()]
    >>> c('to_v', 'param1', 'param2')  # testing with actions & pargs
    Leave StateA
    Enter StateV
    action_V: event[to_v] pargs[('param1', 'param2')]
    >>> c('whatever')
    Traceback (most recent call last):
    ...
    pyfseException: msg[error_action_method_not_found] params[{'current_state': 'state_v', 'event': 'whatever'}]
    >>> c('to_w', param1='value1')
    default_leave
    default_enter
    action_W: event[to_w] pargs[()] kargs[{'param1': 'value1'}]
    """


# ==============================================
# ==============================================

import doctest
doctest.testmod(report=True)
   
