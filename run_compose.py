#/usr/bin/env python3

import os
import sys
import compose.cli.command

config = compose.cli.command.get_project(os.path.dirname(sys.argv[0]))

config.build()
containers = config.up()

# print('up() ->', containers, file=sys.stderr)

for x in containers:
    exitcode = x.wait()
    print (x, 'exited with status:', exitcode, file=sys.stderr)
