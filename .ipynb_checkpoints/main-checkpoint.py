from smallest import find_two_smallest
from list import list1, list2, list3, list4

lists = [list1, list2, list3, list4]
results = []

for list_input in lists:
    try:
        smallest_pair = find_two_smallest(list_input)
        results.append(smallest_pair)
    except ValueError as e:
        results.append(str(e))

with open("result.txt", "w") as f:
    for result in results:
        f.write(f"{result}\n")