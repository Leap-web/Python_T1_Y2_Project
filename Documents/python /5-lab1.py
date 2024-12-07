c = input("Enter a string:")
length = len(c)
c = c.lower()
mid = length//2
cr =-1
for i in range(mid):
    if c[i] == c[cr]:
        cr-=1
    else:
        print(c,"is not a palindrome")
print(c,"is a palindrome")
