# def merge_list(lst1,lst2):
#     list=[]
#     for i in range(len(lst1)):
#         for j in range(i+1,len(lst2)):
#             if lst1[i] == lst2[j]:
#                 continue
# print(merge_list([1,2,3],[2,3,4,5]))

def merge_list(lst1,lst2):
    return lst1 + [i for i in lst2 if i not in lst1]
print(merge_list([1,2,3],[2,3,4,5]))