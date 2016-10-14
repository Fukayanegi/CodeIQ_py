from fractions import Fraction

in1 = raw_input().split('/')
f1 = Fraction(int(in1[0]), int(in1[1]))
in2 = raw_input().split('/')
f2 = Fraction(int(in2[0]), int(in2[1]))

print(f1 + f2)
