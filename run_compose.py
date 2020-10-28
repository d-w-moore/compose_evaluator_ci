#/usr/bin/env python3

import os, sys
import compose.cli.command

config = compose.cli.command.get_project('.')

config.build()
containers = config.up()

print ('up() ->', containers)

for x in containers:
  exitcode = x.wait()
  print (x, 'exited with status:', exitcode, file=sys.stderr)
