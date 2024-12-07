def add(a,b):
    return a+b
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(add(num1,num2))

# def sum(a,b):
#     result = a+b
#     print(result)
# sum(4,5)

def greet():
    print('Hello, World!')
greet()

x = lambda num:num**2
print(x(5))