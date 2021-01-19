import random
import bisect
import math

def populate_numbers_list(list_size):
    numbers = []
    for i in range(0,list_size):
        n = random.randint(1,100)
        while n in numbers:
            n = random.randint(1,100)
        bisect.insort(numbers, n)
    return numbers

def binary_search_recursive(numbers, to_find, begin, end):
    if (begin > end):
        return -1

    current = math.floor((begin + end) / 2)
    if numbers[current] == to_find:
        return current
    elif numbers[current] < to_find:
        return binary_search_recursive(numbers, to_find, current + 1, end)
    else:
        return binary_search_recursive(numbers, to_find, begin, current - 1)

def binary_search_iterative(numbers, to_find):
    begin = 0
    end = len(numbers)-1

    while(begin <= end):
        current = math.floor((begin + end) / 2)
        if numbers[current] == to_find:
            return current
        elif numbers[current] < to_find:
            begin = current + 1
        else:
            end = current - 1

    return -1


numbers = populate_numbers_list(25)
to_find = random.randint(1,100)
#found = binary_search_recursive(numbers, to_find, 0, len(numbers) - 1)
found = binary_search_iterative(numbers, to_find)

print("Numbers: " + str(numbers))
print("To find: " + str(to_find))
print("Found at: " + str(found))


        


    
