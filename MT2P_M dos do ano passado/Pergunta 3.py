def rec_count(alist, dict = {}):
    for element in alist:
        if type(element) == list:
            rec_count(element)
        elif element in dict.keys():
            dict[element] += 1
        else:
            dict[element] = 1
    return dict
    

#têm de se passar os testes 1 a 1
print(rec_count([6, "9j", [], [[0, [2, [2, [3, [4, "9j", [5, 6]]]]]]]])) # o 9j n era uma string mas pronto tem de ser assim senão vai dar erro
print(rec_count([[-1, 0, 0, []], [0, -1, 0], [0, 0, -1]]))
print(rec_count([[[2.0], []], [6, [2.0]], 1, [6, 6]]))
print(rec_count([[],[],[]]))