#!/usr/bin/python
def recur_fibo(n):
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))

#nterms = 10

def my_function(nterms):
	if nterms <= 0:
		print("Please enter a positive integer")
	else:
		print("Fibonacci sequence:")
		for x in range(nterms):
			print(recur_fibo(x))

nterm = int(input("Enter amount of terms: "))
print(nterm)
