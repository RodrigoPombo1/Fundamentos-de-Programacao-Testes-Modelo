def is_the_same_number_in_reverse(number_one, number_two):
    string_number1 = str(number_one)
    string_number2 = str(number_two)
    length1 = len(string_number1)
    if length1 == len(string_number2):
        for position, char in enumerate(string_number1):
            if char != string_number2[-(position + 1)]:
                return False
        return True
    return False
    

def is_pair_of_square(number_one, number_two):
    if number_one != number_two:
        if is_the_same_number_in_reverse(number_one, number_two) and is_the_same_number_in_reverse(number_one**2, number_two**2):
            return True
    return False