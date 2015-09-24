#!/usr/bin/python

import sys

import os

import re

import subprocess

def checkValid():
    cmd = "git diff-index --name-only HEAD"

    names = [f[:-1] for f in subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, cwd=os.getcwd()).stdout.readlines() ]

    for n in names:
        lines = open(n).readlines()
        for l in lines:
            if (len(l) > 80):
                print "Unacceptable file!"
                exit(1)
    
    exit(0)

if __name__ == "__main__":
    checkValid()
