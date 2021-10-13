def tripler(func):
	"""
	"""
	def triple():
		func()
		func()
		func()
	return triple()
