# def merge_dic(d1,d2):
#     for i in d2:
#         d1[i] = d2[i]
#     return d1
# d1 = {'a':1,'b':2}
# d2 = {'b':3,'c':4}
# d3 = merge_dic(d1,d2)
# print(d3)
def merge_dic(dic1,dic2):
    final_dic = {}
    for i in dic1:
        final_dic[i] = dic1[i] + dic2.get(i,0) # if key ot mean in dic2, vea tv jea 0 ber mean vea plus
    for i in dic2:
        if i not in final_dic:
            final_dic[i] = dic2[i] # check tha ber in dic2 ot doch final yk dic2 tv final del
    return final_dic
d1 = {'a':1,'b':2}
d2 = {'b':3,'c':4}
result = merge_dic(d1,d2)
print("Final dictionary",result)