# dic = {"Name":"Umer Nawaz", 35:"Roll No", "Male": True}
# # print(dic["Name"])
# # print(dic.get('Male2'))
# # print(dic[35])

# # print(dic.keys())
# # print(dic.values())

# # # for value find with the help of keys
# # for key in dic.keys():
# #     print(dic[key])


# # for key in dic.keys():
# #     print(f"The corresponding to the key {key} is {dic[key]}")


# print(dic.items())
# for key, value in dic.items():
#     print(f"The corresponding to the key {key} is {value}")

# ------------------ DICTIONARY_METHODS IN PYTHON ---------------------------

emp1 = {11:25,12:35,13:45}
emp2 = {21:55,22:65}
#emp1.update(emp2)
#emp1.clear()
#emp1.pop(12)
#emp1.popitem()
#del emp1
del emp1[11]
print(emp1)