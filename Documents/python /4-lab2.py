def max(tups):
    maxx = tups[0]
    for i in range(0,len(tups)):
        if tups[i] > maxx:
            maxx = tups[i]
    return maxx
def mini(tups):
    minii = tups[0]
    for i in range(0,len(tups)):
        if tups[i] < minii:
            minii = tups[i]
    return minii
tup = (10,5,8,12,3)
print(max(tup))
print(mini(tup))

# def max_min(tuple):
#     return max(tuple), min(tuple)
# max_min_tuple = (10, 5, 8, 12, 3)
# print(max_min(max_min_tuple))
