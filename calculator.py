def calculator(number1, number2, operator):
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
	str = (raw_input("Enter equation: "))
	x = str.split()
	num1 = float(x[0])
	num2 = float(x[-1])
	op = (x[1])
	print (calculator(num1, num2, op))

parse_input()
