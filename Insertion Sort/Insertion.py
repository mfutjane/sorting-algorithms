
def swap_at_index(elements, i, descending):
    """
    Swap the element at i into the sorted array, 
    considering descending order

    Arguments
    ---------
    elements:
        any iterable with comparable elements
    
    i:
        the index where the unsorted part of elements begins
    
    descending:
        the order elements should be sorted in
    
    Returns
    -------
    iterable:
        elements with the item at i placed in the correct position
    """

    while True:
        comparison = elements[i] <= elements[i-1] if descending else \
            elements[i] >= elements[i-1]

        if i == 0:
            return elements
        if comparison == True:
            return elements

        elements[i], elements[i-1] = elements[i-1], elements[i]
        i -= 1


def insertion_sort(elements, descending=False):
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

    for i in range(length):
        if i == 0:
            continue
        elements = swap_at_index(elements, i, descending)
    return elements
