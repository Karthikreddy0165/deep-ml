def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	for i in range(len(a)):
		a[i] += b[i]
	return a if len(a) == len(b) else -1
