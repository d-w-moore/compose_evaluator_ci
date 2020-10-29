#!/usr/bin/env python
from __future__ import print_function
import sys, os
import math

arg_to_eval = sys.argv[1]

if arg_to_eval.startswith("EXPR"): arg_to_eval = os.environ.get(arg_to_eval,'1234')

arg_to_eval = arg_to_eval.strip("'" '"')

log_file = sys.stdout \
                      if not sys.argv[2:] \
           else open(sys.argv[2],'w')

print('eval({!r}) -> {!r}'.format(arg_to_eval, eval(arg_to_eval)), file = log_file)
