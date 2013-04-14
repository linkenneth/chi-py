# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import subprocess, re, sys, io

python = subprocess.Popen(["python"],
                          stdin = subprocess.PIPE,
                          stdout = subprocess.PIPE)

dictionary = {
    u'如果' : 'if',
    u'否则' : 'else',
    u'直到' : 'while',
    u'用' : 'with',
    u'是' : 'is',
    u'加入' : 'import',
    u'不' : 'not',
    u'于' : 'in',
    u'在' : 'in',
    u'范围' : 'range'
    }

dictionary = { re.compile(r'\b%s\b' % k, flags = re.UNICODE) : v \
                   for k, v in dictionary.items() }

while True:
    line = sys.stdin.readline().decode("utf-8")
    if not line:
        break
    for chinese, english in dictionary.items():
        line = re.sub(chinese, english, line)
    print >>python.stdin, line.encode('utf-8')

python.stdin.close()
print python.stdout.read(),
