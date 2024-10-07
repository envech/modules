def find_two_smallest(list_input):
    if len(list_input) < 2:
        raise ValueError("List must contain at least two elements.")
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for number in list_input:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif smallest < number < second_smallest:
            second_smallest = number
    
    return smallest, second_smallest