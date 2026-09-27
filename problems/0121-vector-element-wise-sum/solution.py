def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	len_a = len(a)
	len_b = len(b)

	if len_a == len_b:
		return [sum(i) for i in zip(a,b)]

	else:
		return -1