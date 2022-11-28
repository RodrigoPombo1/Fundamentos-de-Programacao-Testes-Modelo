def dict2list(adict, m, n):
    #create empty list
    result_list = []
    for i in range(m):
        result_list.append([])
        for _ in range(n):
            result_list[i].append(0)
    for key, value in adict.items():
        if (key[0] > m - 1) or (key[1] > n - 1):
            return None
        result_list[key[0]][key[1]] = value
    return result_list