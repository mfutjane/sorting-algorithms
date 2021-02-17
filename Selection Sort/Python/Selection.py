
def find_index(elements, descending):
    """
    Find the index of the smallest/largest item in elements
    depending on the requested order.

    Arguments
    ----------
    elements :
        any iterable containing elements that can be compared
    
    descending :
        boolean describing the order elements will be sorted in.
        true = descending order, false = ascending order

    Returns 
    -------
    int :
        the index of the appropriate item in elements depending on order
    """

    candidate = elements[0]
    index = 0

    for i in range(len(elements)):
        comparison = elements[i] > candidate if descending else \
            elements[i] < candidate 
        
        if comparison == True:
            index = i
            candidate = elements[i]
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
    flag = False
    if (type(elements) == str):
        elements = list(elements)
        flag = True

    length = len(elements)

    for i in range(length):
        index = find_index(elements[i:], descending)
        elements[i], elements[i + index] = elements[i + index], elements[i] 
    
    elements = "".join(elements) if flag else elements
    return elements
