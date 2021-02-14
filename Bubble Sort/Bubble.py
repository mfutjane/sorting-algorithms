
def compare_adjacent_elements(elements, length, descending):
    for i in range(0, length-1):
        comparison = elements[i] < elements[i+1] if descending else \
            elements[i] > elements[i+1]

        if comparison:
            elements[i], elements[i+1] = elements[i+1], elements[i]
    return elements


def bubble_sort(elements, descending=False):
    length = len(elements)

    for i in range(length):
       elements = compare_adjacent_elements(elements, length, descending)
    return elements