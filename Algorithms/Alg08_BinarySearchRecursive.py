def binary_search_recursive(L:list, x) -> bool:
	if len(L) == 0:
		return False
	mid = len(L)//2
	if L[mid] == x:
		return True
	if x < L[mid]:
		return binary_search_recursive(L[:mid], x)
	return binary_search_recursive(L[mid + 1:], x)