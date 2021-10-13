import time
def calculate_time(func):
	"""
	Decorator to calculate the amount of time a function takes to execute.
	"""
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		result = end-start
		print("Total time ", result)
	return wrapper
