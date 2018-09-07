#importing regular expression library
import re
#opening a file in read mode
file = open('primes1.txt', 'r')
#reading a file
file = file.read()[1:]
numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file) 
#this is same as given above
numbers = re.findall(r"[-+]?[0-9]*\.[0-9]+|[0-9]+", file)
#prompt you to enter the index of the prime number which you realy needed
index=input("enter the index of an prime which you needed:")
#selecting and displaying the prime number of an given index
print numbers[index]

