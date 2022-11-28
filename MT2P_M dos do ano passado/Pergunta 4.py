def moving_average(alist, n):
    if len(alist) < 3 or n < 3:
        return []
    result_list = []
    for i in range(len(alist) - (n - 1)):
        result_list.append(average_list(alist[0+i:(n+2*i)//2] + alist[(n+2*i)//2+1:n+i]))
    return result_list

def average_list(alist):
    sum = 0
    for element in alist:
        sum += element
    return round(sum / len(alist), 2)
        

print(moving_average([1, 2, 3, 4, 5], 3))
print(moving_average([2, 10, 1, 1, 7, 20, 1], 3))
print(moving_average([2, 10, 1, 1, 7, 20, 1], 5))
print(moving_average([1, 2, 3, 4, 5], 1))





#eis a solução q eu tava a fazer ao não perceber bem o enunciado, a cena é q o do meio n conta na média
#
# eu não percebi o enunciado mas faz o q eu quero q faça e na minha opinião isso é q importa
# def moving_average(alist, n):
#     if len(alist) < 3 or n < 3:
#         return []
#     result_list = []
#     for i in range(len(alist) - (n - 1)):
#         result_list.append(average_list(alist[0+i:n+i]))
#     return result_list

# def average_list(alist):
#     sum = 0
#     for element in alist:
#         sum += element
#     return round(sum / len(alist), 2)
        

# print(moving_average([1, 2, 3, 4, 5], 3))
# print(moving_average([2, 10, 1, 1, 7, 20, 1], 3))
# print(moving_average([2, 10, 1, 1, 7, 20, 1], 5))
# print(moving_average([1, 2, 3, 4, 5], 1))