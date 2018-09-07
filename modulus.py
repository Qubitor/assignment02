
with open("primes1.txt") as f:
    content = f.readlines()
    primes=content[0].split()

var=2648264727
l=len(str(var))/2
print l
modulus=[]
for i in primes:
	if(len(i)<=l):
		if(var%int(i)==0):
			modulus.append(i)

print modulus