"""Pretty much useless code to 'compute' Graham's number. https://en.wikipedia.org/wiki/Graham%27s_number"""
def arrow(a, b, n):
	if n == 1:
		return a ** b
	elif b == 0:
		return 1
	return arrow(a, arrow(a, b-1, n), n-1)

def graham(n):
	if n == 1:
		return arrow(3, 3, 3)
	assert type(n) == int, "graham function only defined on integers."
	return arrow(3, 3, g(n-1))
