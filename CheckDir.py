#!usr/bin/env python3

import os


def check_dir(xyz):
    if os.path.isdir(xyz):
        return True
    else:
        os.mkdir(xyz)
        return False
