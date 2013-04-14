# -*- coding: utf-8 -*-
import subprocess, re, sys, io

python = subprocess.Popen(["python"],
                          stdin = subprocess.PIPE,
                          stdout = subprocess.PIPE,
                          bufsize=1,
                          close_fds = True)

dictionary = {
    '如果' : 'if',
    '否则' : 'else'
    }

while True:
    line = sys.stdin.readline()
    if not line:
        break
    for chinese, english in dictionary.items():
        line = re.sub(chinese, english, line)
    print >>python.stdin, line

python.stdin.close()
print python.stdout.read(),
