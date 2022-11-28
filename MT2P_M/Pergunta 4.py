#não passa nos testes privados
def unique_ntree(tree, result_list=[]):
    if len(tree) == 0:
        return []
    if len(tree) == 1:
        result_list.append(tree[0])
    # if len(tree) == 3:
    if type(tree[0]) == int:
        result_list.append(tree[0])
    unique_ntree(tree[1], result_list)
    unique_ntree(tree[2], result_list)
    return sorted(list(set(result_list)))