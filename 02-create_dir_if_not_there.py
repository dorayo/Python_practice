#!/usr/bin/python

import os
try:
    home = os.path.expanduser('~')
    print(home)

    if not os.path.exists(os.path.join(home, 'testdir')):
        os.makedir(os.path.join(home, 'testdir'))
except Exception as e:
    print(e)
