
def compare_adjacent_elements(elements, length, descending):
    """
    Compare adjecent elements and swap them according to
    the requested order. Only runs up until length elements. 

    Arguments
    ---------
    elements:
        any iterable with comparable items

    length:
        the number of elements to consider for comparison

    descending:
        a boolean used to determine if elements should be sorted
        in descending order

    Return
    ------
    iterable:
        elements after one pass of sorting adjecent items
    """

    for i in range(0, length-1):
        comparison = elements[i] < elements[i+1] if descending else \
            elements[i] > elements[i+1]

        if comparison:
            elements[i], elements[i+1] = elements[i+1], elements[i]
    return elements


def bubble_sort(elements, descending=False):
    """
    Sort elements in the requested order

    Arguments 
    ---------
    elements:
        any iterable with comparable and swappable items 

    descending:
        a boolean used to determine the sorting order

    Return
    ------
    iterable:
         elements sorted in the requested order

    length = len(elements)

    for i in range(length):
       elements = compare_adjacent_elements(elements, length-i, descending)
    return elements
    """

    flag = False
    if (type(elements) == str):
        elements = list(elements)
        flag = True
    
    length = len(elements)

    for i in range(length):
        elements = compare_adjacent_elements(elements, length-i, descending)

    elements = "".join(elements) if flag else elements 
    return elements 
