print (“welcome to Python Calculator v. 1.0”)
print (“ accepted operations are: +, -, x, *, /“)

num1_str = input (“enter First Number: ”)
num1 = float ( num1_str )

op = input (“enter operation +, -, x, /: ”)

num2_str = input (“enter second number: “ )
num2 = float ( num2_str )

result = 0

if op == “+”:
	result = num1 +num2
elif op == “-“: 	
	result = num1 -num2
elif op in ( “x”, “X”, “*” ): 
	result = num1 * num2
elif op == “/“:
	if num2 == 0: 
		print (“ ERROR, can’t divide by zero!”)
	else:
		result = num1 / num2
else:
	print (“ERROR, invalid operation”)

if op in [ “+”, “-“, “*”, “x”, “X”, “/“ ] and not ( op == “/“ and num2 == 0):
	print (f”The result is:  {result}”)
