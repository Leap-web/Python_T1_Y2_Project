a ={1: 10,2: 20,3: 30,4: 40}
new_a= {k: (lambda x: x * 2)(v)for k,v in  a.items()} # items mean 1:10 like key+value=item
print(new_a)
# k take a key of a and V take a value of a
# x and v are the value of a
# (lambda x: x * 2)(v) it means that v pass the value to x to perform the condition