# Python program to print odd Numbers in given range

m, n = 4, 19

# iterating each number in list
for num in range(m, n + 1):
	
	# checking condition
	if num % 2 != 0:
		print(num, end = " ")
