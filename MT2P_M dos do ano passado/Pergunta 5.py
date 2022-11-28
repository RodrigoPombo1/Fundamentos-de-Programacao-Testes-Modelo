from math import gcd

def calculator(expr):
    length = len(expr)
    if length == 2:
        return expr
    if type(expr[0]) == tuple:
        aux_tuple_0 = calculator(expr[0])
    else:
        aux_tuple_0 = expr[0]
    if type(expr[2]) == tuple:
        aux_tuple_2 = calculator(expr[2])
    else:
        aux_tuple_2 = expr[2]
    if expr[1] == '*':
        result_tuple = (aux_tuple_0[0]*aux_tuple_2[0], aux_tuple_0[1]*aux_tuple_2[1])
    else: # <=> (if expr[1] == '/':)
        result_tuple = (aux_tuple_0[0]*aux_tuple_2[1], aux_tuple_0[1]*aux_tuple_2[0])
    common_divisor = gcd(int(result_tuple[0]), int(result_tuple[1]))
    return (int(result_tuple[0] / common_divisor), int(result_tuple[1] / common_divisor))


print(calculator((1, 3)))
print(calculator(((1, 3), '*', (2, 5))))
print(calculator((((1, 3), '/', (4, 5)), '*', (2, 5))))
print(calculator((((1, 3), '/', (4, 5)), '*', ((2, 5), '*', ((10, 2), '/', (1, 1))))))