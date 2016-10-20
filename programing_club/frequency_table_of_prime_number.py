# coding: UTF-8

# 素数配列作成
def make_primes(limit):
  primes = []
  for num in range(2, limit + 1):
    is_prime = True
    quotient = limit
    for prime in primes:
      # 判定対象が前回判定時の商を超える素数だった場合、
      # 以降の商は前回の素数を下回る（既に存在しないことが判定済）ため打ち切り
      if prime > quotient:
        break
      quotient = num / prime
      if num % prime == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num) 
  return primes

input = map(int, raw_input().split(' '))
digit = len(str(input[0]))
f_str = "%0" + str(digit) + "d-%0" + str(digit) + "d:"

primes = make_primes(input[0])
ps = enumerate(primes)
i, target = ps.next()

for base in range(1, input[0], input[1]):
  section_limit = base + input[1] - 1
  frequency = 0
  while target <= section_limit:
    frequency += 1
    try:
      i, target = ps.next()
    except StopIteration:
      break
  print(f_str % (base, section_limit) + "*"*frequency)