def algo(a,b):
  q = a // b
  r = a % b
  print(f'{a} {q} {b} {r}')
  if r == 0:
    return b
  return algo(b,r)

print('Greatest Common Divisor algo')
a = int(input('enter 1st number: '))
b = int(input('enter 2nd number: '))

print('a  q  b  r')

gcd = algo(a, b)

print(f'Greatest Common Divisor = {gcd}') 