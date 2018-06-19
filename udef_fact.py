#!usr/bin/python2

def factorial(num) :
	if num==1 :
		return num
	else :
		return num*factorial(num-1)

num=input("enter number ")
if num<0 :
	print("factorial cant be a negative number")
elif num==0 :
	print("factorial is 1")
else :
	print("factorial of given number is ", factorial(num))


