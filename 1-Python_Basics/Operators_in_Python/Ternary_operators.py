# Ternary operators
# syn: [on_true] if [expression] else [on_false]

a=int(input("Enter A value "))
b=int(input("Enter B value "))

min=a if a<b else b 
print("Min value is",min)

print ("Both a and b are equal" if a == b else "a is greater than b"if a > b else "b is greater than a")

#Python Ternary Operator using Tuples
print( (b, a) [a < b] )

#Python Ternary Operator using Dictionary
print({True: a, False: b} [a < b])

#Python Ternary Operator using Lambda
print((lambda: b, lambda: a)[a < b]())

#Print in if Ternary Operator
print(a,"is greater") if (a>b) else print(b,"is Greater")