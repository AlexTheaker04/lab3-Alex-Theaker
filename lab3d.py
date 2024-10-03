#!/usr/bin/env python3
'''Lab 3 part D '''
# Author ID: theakera

import subprocess
import os


def free_space():
    p = subprocess.Popen([" df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    disk_space = p.communicate()

    stdout = disk_space[0].decode('utf-8').strip()
    return(stdout)

print(free_space())