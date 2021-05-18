from sys import maxsize
from copy import deepcopy

def get_input():
    number_standard_lengths = int(input("Enter the number of standard lengths: "))
    standard_lengths = []
    while len(standard_lengths) < number_standard_lengths:
        length = int(input("Enter a standard length: "))
        if(length not in standard_lengths):
            standard_lengths.append(length)

    total_length = int(input("Enter the total length of material available: "))
    
    return standard_lengths, total_length
        
def minimize_waste(total_length, standard_lengths, counts):
    #Calculate remaining length
    length_so_far = 0
    for key, value in counts.items():
        length_so_far += key * value
    remaining_length = total_length - length_so_far

    #Remaining length is all waste
    if remaining_length < min(standard_lengths):
        return deepcopy(counts), remaining_length

    lowest_waste = maxsize
    best_counts = {}

    for i in standard_lengths:
        counts_deepcopy = deepcopy(counts)
        
        #Remaining length is divisible by a standard length
        if remaining_length % i == 0:
            counts_deepcopy[i] += remaining_length/i
            return counts_deepcopy, 0
        elif (remaining_length - i) > 0:
            counts_deepcopy[i] += 1
            updated_counts, waste = minimize_waste(total_length, standard_lengths, counts_deepcopy)
            if(waste < lowest_waste):
                best_counts, lowest_waste = updated_counts, waste 

    return best_counts, lowest_waste

if __name__ == "__main__":
    standard_lengths, total_length = get_input()
    counts = {}
    for i in standard_lengths:
        counts[i] = 0
    
    result_counts, result_waste = minimize_waste(total_length, standard_lengths, counts)
    print(result_counts)
    print(result_waste)