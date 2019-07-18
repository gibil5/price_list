# -*- coding: utf-8 -*-

import sys, os


# ----------------------------------------------- Test Funcs -------------------------------------

# Disable
#def blockPrint():
def disablePrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

