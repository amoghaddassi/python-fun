"""Code to calculate the chance of ruin in a gambler's ruin type game.
TODO: ruin doesn't work, need to redefine the recursive formula.
"""
def memo(f):
	cache = {}
	def memoized(*args):
		if args not in cache:
			result = f(*args)
			cache[args] = result
		return cache[args]
	return memoized

@memo
def ruin(start, end):
	assert start < end, 'Invalid inputs.'
	if start == 0:
		return 0
	elif start == end:
		return 1
	return .5 * ruin(start - 1, end) + .5 * ruin(start + 1, end)