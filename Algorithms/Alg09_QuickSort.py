def QuickSort(L:list) -> list:
    if len(L) <= 1:
        return L
    pivot = L[0]
    left = []
    middle = []
    right = []
    for x in L:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return QuickSort(left) + middle + QuickSort(right)