
def min_index(elements):
    """
    Find the index of the smallest item in elements

    Arguments
    ----------
    elements :
        any iterable containing elements that can be compared
    
    Returns 
    -------
    int :
        the index of the smallest item in elements
    """

    min = elements[0]
    index = 0

    for i in range(len(elements)):
        if elements[i] < min:
            index = i
            min = elements[i]
    return index


def max_index(elements):
    """
    Find the index of the largest item in elements

    Arguments
    ----------
    elements :
        any iterable containing elements that can be compared
    
    Returns 
    -------
    int :
        the index of the largest item in elements
    """

    max = elements[0]
    index = 0

    for i in range(len(elements)):
        if elements[i] > max:
            index = i
            max = elements[i]
    return index


def selection_sort(elements, descending=False):
    """
    Sort elements in ascending or descending order.

    Arguments
    ----------
    elements:
        any iterable with comparable elements
        
    descending (named):
        boolean that determines whether to sort in descending order (true)
        or in ascending order (false). Default: false

    Returns
    -------
    iterable:
        elements sorted in the requested order
    """

    length = len(elements)
    find_next = max_index if descending else min_index

    for i in range(length):
        index = find_next(elements[i:])
        elements[i], elements[i + index] = elements[i + index], elements[i] 
    return elements
