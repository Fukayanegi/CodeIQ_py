# coding: UTF-8

lines = []
try:
  while True:
    line = raw_input()
    lines.append(line)
except EOFError:
  pass

for line in lines:
  print(line)