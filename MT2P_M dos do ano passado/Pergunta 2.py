def reverse_subtuples(alist):
    for counter, atuple in enumerate(alist):
        result_tuple = ()
        result_list = []
        for i in range(len(atuple)):
            result_list.append(atuple[-(i + 1)])
            result_tuple = tuple(result_list)
        alist[counter] = result_tuple
    return alist
    
print(reverse_subtuples([(1,2,3), (4,5,6)]))
print(reverse_subtuples([('Afonso', 'João'), ('Ricardo', 'Nuno', 'Rui')]))
print(reverse_subtuples([(6, 1), ()]))
print(reverse_subtuples([(3, 1, ()), (2,1,'?','a'), (5,1), (7,)]))