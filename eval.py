#!/usr/bin/env python
from __future__ import print_function
import sys, os
import math

SINGLE_QUOTE="'"
DOUBLE_QUOTE='"'

arg_to_eval = os.environ["PARAMETER_EXPR"]

arg_to_eval = arg_to_eval.strip(SINGLE_QUOTE+DOUBLE_QUOTE)

log_file = sys.stdout  if not sys.argv[1:] \
           else open(sys.argv[1],'a')

print('eval({!r}) -> {!r}'.format(arg_to_eval, eval(arg_to_eval)), file = log_file)
