def magic_square(n, matrix = [], current_number = 0, last_position=()):
    if matrix == []:
        for i in range(n):
            matrix.append([])
            for _ in range(n):
                matrix[i].append('')
        matrix[0][n//2] = 1
        matrix[n - 1][n//2] = n ** 2
        current_number = 1
        last_position = (0, n//2)
        
    if current_number + 1 == n**2:
        return matrix        
    next_position = (last_position[0] - 1, last_position[1] + 1)
    
    if (next_position[1] > n - 1) and (next_position[0] < 0):
        next_position = (next_position[0] + 2, next_position[1] - 1)
        last_position = next_position
        current_number += 1
        matrix[next_position[0]][next_position[1]] = current_number
        return magic_square(n, matrix, current_number, last_position)
    
    if next_position[0] < 0:
        next_position = (n - 1, next_position[1])
        
        if matrix[next_position[0]][next_position[1]] != '':
            next_position = (next_position[0] + 2, next_position[1] - 1)
            
        last_position = next_position
        current_number += 1
        matrix[next_position[0]][next_position[1]] = current_number
        return magic_square(n, matrix, current_number, last_position)
    
    if next_position[1] > n - 1:
        next_position = (next_position[0], 0)
        
        if matrix[next_position[0]][next_position[1]] != '':
            next_position = (next_position[0] + 2, next_position[1] - 1)
            
        last_position = next_position
        current_number += 1
        matrix[next_position[0]][next_position[1]] = current_number
        return magic_square(n, matrix, current_number, last_position)
    
    if matrix[next_position[0]][next_position[1]] != '':
        next_position = (next_position[0] + 2, next_position[1] - 1)
        
    last_position = next_position
    current_number += 1
    matrix[next_position[0]][next_position[1]] = current_number
    return magic_square(n, matrix, current_number, last_position)