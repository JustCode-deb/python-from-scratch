#Print the value of the data from the user and switch it
 
a = input("A: ")
b = input("B: ")

#Using a bridge variable to switch the input value

c=a
a=b
b=c

print("A= " + a)
print("B= " + b)