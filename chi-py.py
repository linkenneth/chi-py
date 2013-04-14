# -*- coding: utf-8 -*-
import subprocess, re, sys, io
from collections import OrderedDict

python = subprocess.Popen(["python"],
                          stdin = subprocess.PIPE,
                          stdout = subprocess.PIPE)

dictionary = OrderedDict([
    [ ur'否则如果', 'elif' ],
    [ ur'如果', 'if' ],
    [ ur'否则', 'else' ],
    [ ur'当', 'while' ],
    [ ur'用', 'with' ],
    [ ur'返回', 'return' ],
    [ ur'为', 'as' ],
    [ ur'总和', 'sum' ],
    [ ur'和', 'and' ],
    [ ur'或', 'or' ],
    [ ur'循环', 'for' ],
    [ ur'是', 'is' ],
    [ ur'真', 'True' ],
    [ ur'假', 'False' ],
    [ ur'加入', 'import' ],
    [ ur'定义', 'def' ],
    [ ur'类', 'class' ],
    [ ur'不', 'not' ],
    [ ur'于', 'in' ],
    [ ur'在', 'in' ],
    [ ur'打印', 'print' ],
    [ ur'时间', 'time' ],
    [ ur'范围', 'range' ],
    [ ur'一箭双雕\((.*?),\s*(.*?)\)',
      "__chi_py_p = __chi_py_Pool(5); __chi_py_p.map(\\1, \\2)" ]
])

dictionary = { re.compile(k, flags = re.UNICODE) : v \
                   for k, v in dictionary.items() }

CHINESE_REGEX = re.compile(u'[\u4e00-\u9fff\u3400-\u4dff]')
chi_idents = {}

v = 0

SETUP = [ "# -*- coding: utf-8 -*-",
          "from multiprocessing import Pool as __chi_py_Pool" ]

for line in SETUP:
    print >>python.stdin, line

while True:
    line = sys.stdin.readline().decode("utf-8")
    print line,
    if not line:
        break
    for chinese, english in dictionary.items():
        line = re.sub(chinese, english, line)
    idents = re.findall(CHINESE_REGEX, line)
    for ident in idents:
        if ident not in chi_idents:
            chi_idents[ident] = "__chi_py_v" + str(v)
            v += 1
        line = line.replace(ident, chi_idents[ident])
    print line,
    print >>python.stdin, line.encode('utf-8')

python.stdin.close()
print python.stdout.read(),

