#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
from twisted.python import log

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def start(where=sys.stdout):
    """
    Starts logging  
    
    Args:
        where: where to log (default=sys.stdout)
    """
    log.startLogging(where)
    
def debug(message):
    """
    Publish a message to the global log publisher.
    
    Args:
        message: the log message
    """
    log.msg(message)
    
def error(message, excpection=Exception):
    """
    Publish an error to the global log publisher.
    
    Args:
        message: the error message
        exception: the exception type (default=Exception)
    """
    log.err(exception, message)