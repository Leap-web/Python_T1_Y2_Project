num = int(input("Enter the number:"))
fac =1
if num >=1:
    for i in range(1,num+1):
        fac = fac*i
    print(f"Factorial of {num} is {fac}")
else:
    print(f"Factorial of {num} is {fac}")