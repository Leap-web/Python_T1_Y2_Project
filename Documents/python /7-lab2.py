def test_str(lst):
    list={}
    for i in lst.lower(): # want Hello to become all small letters
        if i in list:
            list[i] +=1
        else:
            list[i] =1
    return list
print(test_str("Hello"))

# from typing import Dict


# char_dict = {} #type: Dict[str, int]


# def char_count(string: str) -> dict:
#     new_string = string.lower()
#     for c in new_string:
#         if c in char_dict:
#             char_dict[c] += 1
#         else:
#             char_dict[c] = 1
#     return char_dict


# if name == "main":
#     UserString = input("Enter Input String: ")
#     CharCount = char_count(UserString)
#     print("Characters Count: ", CharCount)