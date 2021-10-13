def swap_last_item(myList):
	"""
	Swaps the last element in a list with the first element.
	
	Parameters
	----------
	myList:list of integers
	Returns
	-------
	list: myList with first and last element swapped

	"""
	temp = myList[-1]
	myList[-1] = myList[0]
	myList[0] = temp
	return myList
