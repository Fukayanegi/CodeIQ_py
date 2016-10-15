# coding: UTF-8

# from fractions import Fraction

# in1 = raw_input().split('/')
# f1 = Fraction(int(in1[0]), int(in1[1]))
# in2 = raw_input().split('/')
# f2 = Fraction(int(in2[0]), int(in2[1]))

# print(f1 + f2)

# 車輪の再発明をするなら
import time
def decomposite_prime(num):
  answer = [1]
  while num != 1:
    for i in range(2, num + 1):
      if num % i == 0:
        answer.append(i)
        num = num / i
        break
  return answer

def diff_factor(factor1, factor2):
  factor1.sort()
  factor2.sort()
  j = 0
  answer = [1]
  for i in range(0, len(factor2)):
    if j < len(factor1) and factor2[i] > factor1[j]:
      while factor2[i] > factor1[j]:
        answer.append(factor1[j])
        j += 1
        if j >= len(factor1):
          break
    elif j < len(factor1) and factor2[i] == factor1[j]:
      j += 1
  if j < len(factor1):
    answer += factor1[j:len(factor1)]
  return answer

def common_factor(factor1, factor2):
  factor1.sort()
  factor2.sort()
  j = 0
  answer = [1]
  for i in range(0, len(factor1)):
    if j < len(factor2) and factor1[i] == factor2[j]:
      answer.append(factor1[i])
      j += 1
    elif j < len(factor2) and factor1[i] > factor2[j]:
      while factor1[i] > factor2[j]:
        j += 1
        if j >= len(factor2):
          break
  return answer

in1 = raw_input().split('/')
in2 = raw_input().split('/')

n1 = int(in1[0])
d1 = decomposite_prime(int(in1[1]))
n2 = int(in2[0])
d2 = decomposite_prime(int(in2[1]))

common_multiple_factor = iter(d1 + diff_factor(d2, d1))
denominator = reduce(lambda x, y: x * y, common_multiple_factor)
# print(denominator)

if d1 != d2:
  n1 = n1 * reduce(lambda x, y: x * y, diff_factor(d2, d1))
  n2 = n2 * reduce(lambda x, y: x * y, diff_factor(d1, d2))
numerator = n1 + n2
# print(numerator)

factor_n = decomposite_prime(numerator)
factor_d = decomposite_prime(denominator)
common_factor = reduce(lambda x, y: x * y, common_factor(factor_n, factor_d))
# print(common_factor)
if denominator / common_factor == 1:
  print(numerator / common_factor)
else:
  print("%d/%d" % (numerator / common_factor, denominator / common_factor))