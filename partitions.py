def count_paritions(n, m):
	if m  == 1:
		return 1
	return count_paritions(n - m, m) + count_partitions(n, m-1)
