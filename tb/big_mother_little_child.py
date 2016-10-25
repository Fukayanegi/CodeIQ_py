# coding: UTF-8

lines = []
try:
  while True:
    line = raw_input()
    lines.append(line)
except EOFError:
  pass

import re
pattern = re.compile('[aiueoAIUEO]')
for line in lines:
  if pattern.search(line):
    print(line.upper())
  else:
    print(line.lower())