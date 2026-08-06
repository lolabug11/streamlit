import numpy as np
def get_factors(number,get_negative_nums = True):
  if number < 0:
    number *= -1
    factors = {}
    for posible_factor in range(int(number)):
      posible_factor += 1
      if number % posible_factor == 0:

        factors[posible_factor*-1] = number / posible_factor
        factors[posible_factor] = (number / posible_factor) * -1
    return factors
  else:
    factors = {}
    for posible_factor in range(int(number)):
      posible_factor += 1
      if number % posible_factor == 0:

        factors[posible_factor] = number / posible_factor
        if get_negative_nums:
          factors[-posible_factor] = - (number/posible_factor)

    return factors

def factor_standered_form_quadratic(a,b,c):
    print(f'{a}\n{b}\n{c}')
    if a == 0:
        return False
    a_factors = get_factors(a,False)
    b_factors = get_factors(b)
    c_factors = get_factors(c)
    print(f'{a_factors}\n{b_factors}\n{c_factors}')
    equation = False

    for a_factor in a_factors:
        for c_factor in c_factors:
            combo1 = np.array([[a_factor * c_factor,0], [a_factor , c_factor]])
            combo2 =np.array([ [a_factor * c_factors[c_factor],0], [a_factor , c_factors[c_factor]]])
            combo3 = np.array([[a_factors[a_factor] * c_factor,0], [a_factors[a_factor] , c_factor]])
            combo4 = np.array([[a_factors[a_factor] * c_factors[c_factor],0], [a_factors[a_factor] , c_factors[c_factor]]])
            if combo1[0,0] + combo2[0,0] == b :
                if combo2[1,1] >= 0:
                    sign1 = '+'
                else:
                    sign1 = '-'
                    combo2[1,1] *= -1

                if combo1[1,1] >= 0:
                    sign2 = '+'
                else:
                    sign2 = '-'
                    combo1[1,1] *= -1
                equation = f'({combo1[1,0]}x {sign1} {combo2[1,1]})({combo2[1,0]}x {sign2} {combo1[1,1]})'
                break

            elif combo1[0,0] + combo3[0,0] == b :
                if combo3[1,1] >= 0:
                    sign1 = '+'
                else:
                    sign1 = '-'
                    combo3[1,1] *= -1

                if combo1[1,1] >= 0:
                    sign2 = '+'
                else:
                    sign2 = '-'
                    combo1[1,1] *= -1
                equation = f'({combo1[1,0]}x {sign1} {combo3[1,1]})({combo3[1,0]}x {sign2} {combo1[1,1]})'
                break

            elif combo1[0,0] + combo4[0,0] == b :
                if combo4[1,1] >= 0:
                    sign1 = '+'
                else:
                    sign1 = '-'
                    combo4[1,1] *= -1

                if combo1[1,1] >= 0:
                    sign2 = '+'
                else:
                    sign2 = '-'
                    combo1[1,1] *= -1
                equation = f'({combo1[1,0]}x {sign1} {combo4[1,1]})({combo4[1,0]}x {sign2} {combo1[1,1]})'
                break

            elif combo2[0,0] + combo3[0,0] == b :
                if combo3[1,1] >= 0:
                    sign1 = '+'
                else:
                    sign1 = '-'
                    combo3[1,1] *= -1

                if combo2[1,1] >= 0:
                    sign2 = '+'
                else:
                    sign2 = '-'
                    combo2[1,1] *= -1
                equation = f'({combo2[1,0]}x {sign1} {combo3[1,1]})({combo3[1,0]}x {sign2} {combo2[1,1]})'
                break
        
            elif combo2[0,0] + combo4[0,0] == b :
                if combo4[1,1] >= 0:
                    sign1 = '+'
                else:
                    sign1 = '-'
                    combo2[1,1] *= -1

                if combo2[1,1] >= 0:
                    sign2 = '+'
                else:
                    sign2 = '-'
                    combo2[1,1] *= -1
                equation = f'({combo2[1,0]}x {sign1} {combo3[1,1]})({combo3[1,0]}x {sign2} {combo2[1,1]})'
                break

            elif combo3[0,0] + combo4[0,0] == b :
                if combo4[1,1] >= 0:
                    sign1 = '+'
                else:
                    sign1 = '-'
                    combo4[1,1] *= -1

                if combo3[1,1] >= 0:
                    sign2= '+'
                else:
                    sign2 = '-'
                    combo3[1,1] *= -1
                equation = f'({combo3[1,0]}x {sign1} {combo4[1,1]})({combo4[1,0]}x {sign2} {combo3[1,1]})'
                break
    print(equation)
    return equation

print(factor_standered_form_quadratic(1,-5,6))