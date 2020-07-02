print("Welcome to this Calculator")
print("")

firstnmbr = input("Your first number: ")
secondnmbr = input("Your second number: ")
print("")

print("[1]+")
print("[2]-")
print("[3]/")
print("[4]*")

operator = input("Choose your operator: ")
float_operator = float(operator)	
float_first = float(firstnmbr)
float_second = float(secondnmbr)

if float_operator == 1:
	result = float_first + float_second
	print(firstnmbr, "+", secondnmbr, "=", result)

if float_operator == 2:
	result = float_first - float_second
	print(firstnmbr, "-", secondnmbr, "=", result)

if float_operator == 3:
	result = float_first / float_second
	print(firstnmbr, "/", secondnmbr, "=", result)

if float_operator == 4:
	result = float_first * float_second
	print(firstnmbr, "*", secondnmbr, "=", result)