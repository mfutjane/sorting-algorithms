# Find the smallest/largest element and move it ahead

def min_index(iterable_elements):
    min_element = min(iterable_elements)
    return iterable_elements.index(min_element)


def max_index(iterable_elements):
    max_element = max(iterable_elements)
    return iterable_elements.index(max_element)

def selection_sort(iterable_elements, descending=False):
    find_next = max_index if descending else min_index

    for i in range(len(iterable_elements)):
        next_element = find_next(iterable_elements[i:])
        iterable_elements[i], iterable_elements[i + next_element] = iterable_elements[i + next_element], iterable_elements[i] 
    return iterable_elements

if __name__ == "__main__":
    res = selection_sort(open("testfile.txt", "r").readlines(), descending=True)
    for line in res:
        print(line)