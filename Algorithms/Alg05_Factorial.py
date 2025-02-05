# We assume that n is a positive integer throughout

# Definition 1: non-recursive
def factorial1(n:int) -> int:
	f = 1
	for i in range(1, n + 1):
		f *= i
	return f


# Definition 2: recursive
def factorial2(n:int) -> int:
	if n == 1:						# base case
		return 1
	return n * factorial2(n - 1)	# recursion