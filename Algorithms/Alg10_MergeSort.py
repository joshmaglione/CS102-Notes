# Subroutine of merge sort. 
# Given two sorted lists, we merge them and sort.
def Merge(left:list, right:list) -> list:
    lr_merge = [] 
    i = 0
    j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            lr_merge.append(left[i])
            i += 1
        else:
            lr_merge.append(right[j])
            j += 1
    lr_merge.extend(left[i:])
    lr_merge.extend(right[j:])
    return lr_merge

# Given an unsorted list, return a sorted list
def MergeSort(L:list) -> list:
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = MergeSort(L[:mid])
    right = MergeSort(L[mid:])
    return Merge(left, right)