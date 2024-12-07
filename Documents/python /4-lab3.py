dic = {"alice":30,"Bob":25,"Charlie":35}
print(dic)
dic ["Dara"] = 40
print(dic)
del dic ["alice"]
print(dic)
for i,e in dic.items(): # i = key, e = value
    print(f"{i}:{e}")
