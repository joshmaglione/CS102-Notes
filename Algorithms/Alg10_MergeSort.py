# Subroutine of merge sort. 
# Given two sorted lists, we merge them and sort.
def merge(left:list, right:list) -> list:
    lr_merge = [] 
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            lr_merge.append(left[0])
            left = left[1:]
        else:
            lr_merge.append(right[0])
            right = right[1:]
    lr_merge.extend(left)
    lr_merge.extend(right)
    return lr_merge

# Given an unsorted list, return a sorted list
def merge_sort(L:list) -> list:
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)