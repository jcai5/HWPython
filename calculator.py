def calculator(number1, number2, operator):
	"""
	calculator function computes +, -, *, /, //, and ** using the inputs number1, number2, and the operator.
	Parameters
	----------
	number1 : float
	number2 : float
	operator : string

	Returns
	-------
	float depending on the operator or false if the operator is not found
	
	"""
	if operator == '+':
		return number1+number2
	if operator == '-':
		return number1-number2
	if operator == '*':
		return number1*number2
	if operator == '/':
		return number1/number2
	if operator == '//':
		return number1//number2
	if operator == '**':
		return number1**number2
	else:
		return False

def parse_input():
	"""
	parse_input takes the input of the user, parses the input and passes it to the calculator.
	"""
	str = (raw_input("Enter equation: "))
	x = str.split()
	num1 = float(x[0])
	num2 = float(x[-1])
	op = (x[1])
	print (calculator(num1, num2, op))

