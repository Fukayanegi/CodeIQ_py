# coding: UTF-8

lines = []
try:
  while True:
    line = raw_input()
    lines.append(line)
except EOFError:
  pass

# 閉じるタグがないタグ名
NOT_CLOSE = ["INPUT"]
# 閉じるタグは任意のタグ名
NOT_REQUIRED_CLOSE = ["LI"]

import re
# 属性以降は無視
pattern = re.compile('<(/*)(\w*) ?([\w=\.\s"]*)>')
syntax_tree = []
error_line = -1
for i, l in enumerate(lines):
  matches = pattern.finditer(l)
  for m in matches:
    # print(m.group())
    # print(m.group(1))
    # print(m.group(2))
    if m.group(1) != "/":
      # 閉じるタグがないタグでなければスタックにpush
      tag = m.group(2).upper()
      if tag not in NOT_CLOSE:
        # print("append %s" % tag)
        syntax_tree.append(tag)
    else:
      # /で始まるタグだった場合、直近のタグと比較
      previous = syntax_tree.pop().upper()
      close_tag = m.group(2).upper()
      # print("pop %s" % previous)
      # print("compare %s" % close_tag)
      # 同一でなくても直近のタグが、閉じるのが任意のタグだった場合はさらに一つ前のタグと比較
      while previous != close_tag and previous in NOT_REQUIRED_CLOSE:
        previous = syntax_tree.pop().upper()
      if previous != close_tag:
        error_line = i
        # print("no match! %s %s" % (previous, close_tag))
  if error_line >= 0:
    break

print(error_line+1)