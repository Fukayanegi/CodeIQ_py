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

in1 = raw_input().split('/')
in2 = raw_input().split('/')

n1 = int(in1[0])
d1 = set(decomposite_prime(int(in1[1])))
n2 = int(in2[0])
d2 = set(decomposite_prime(int(in2[1])))

common_multiple_factor = iter(d1 | (d1 ^ d2))
denominator = reduce(lambda x, y: x * y, common_multiple_factor)

if d1 != d2:
  n1 = n1 * reduce(lambda x, y: x * y, (d2 - d1))
  n2 = n2 * reduce(lambda x, y: x * y, (d1 - d2))
numerator = n1 + n2

factor_n = set(decomposite_prime(numerator))
factor_d = set(decomposite_prime(denominator))
common_factor = reduce(lambda x, y: x * y, factor_n & factor_d)
if denominator / common_factor == 1:
  print(numerator / common_factor)
else:
  print("%d/%d" % (numerator / common_factor, denominator / common_factor))



