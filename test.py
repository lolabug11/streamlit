def get_factors(number):
  factors = {}
  for posible_factor in range(int(number)):
    posible_factor += 1
    if number % posible_factor == 0:
      if  posible_factor not in factors.values():
        factors[posible_factor] = number / posible_factor
  return factors

a = float(input('a'))
b = float(input('b')) 
c = float(input('c'))
a_factors = get_factors(a)
b_factors = get_factors(b)
c_factors = get_factors(c)

if len(a_factors) == 1:
  print('A is prime')
if len(b_factors) == 1:
  print('B is prime')
if len(c_factors) == 1:
  print('C is prime')
