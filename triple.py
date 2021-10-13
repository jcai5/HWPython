def tripler(func):
	"""
	tripler decorator repeats the same function 3 times.
	Parameters
	----------
	func: the function to be repeated
	"""
	def triple():
		func()
		func()
		func()
	return triple()
