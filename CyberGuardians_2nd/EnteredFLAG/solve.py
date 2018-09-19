#!/usr/bin/env python2
# coding: utf-8

import angr

def main():
    p = angr.Project("./EnteredFLAG", auto_load_libs=False)
    path_group = p.factory.path_group()
    path_group.explore(find=0x0000000000400DF9)

    print path_group.found[0]
    print path_group.found[0].state.posix.dumps(0)

if __name__ == '__main__':
    main()

"""
Result:
WARNING | 2018-09-19 12:56:04,418 | angr.factory | factory.path_group() is deprecated! Please use factory.simgr() instead.
<SimState @ 0x400df9>
Y0uUs3Angr**
J*
  JJ
    J
     J*

      J**

"""

