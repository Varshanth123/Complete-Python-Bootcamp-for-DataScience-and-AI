# Logical operators
a=int(input("Enter A value "))
b=int(input("Enter B value "))

# Logical "and" operator
print("Is A is greater than B and Divisible by 5 ?",a>b and a%5==0)

# Logical "or" operator
print("Is A is greater than B or Divisible by 5 ?",a>b or a%5==0)

# Logical "not" operator
print("Is A is not greater than B and not Divisible by 5 ?",not(a>b and a%5==0))
