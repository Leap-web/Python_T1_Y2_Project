def rev_lst(lst):
    new_lst=lst[::-1]
    return new_lst
list=[] # create an empty list
n = int(input("Enter the number in list:")) # ask user to input
for i in range(0,n):
    element = int(input()) #user input the element
    list.append(element) # add element that user input to the list
print(list)
print(rev_lst(list))
# def rev_lst(lst):
#     new_lst=lst[::-1]
#     return new_lst
# list=[1,2,3,4,5]
# print(rev_lst(list))