# # --- list in python example -------

# list1=[1,2,3,4,5,6,7,8]
# list2=['red',"green","blue"]
# print(list1)
# print(list2)

# --- Negative_Indexing ---
# marks=[10,20,30,40,50]
# print(marks[-3])
# print(marks[len(marks)-3])
# if 40 in marks:
#     print("yes")
# else:
#     print("No")

# printing in particular range ---

# marks=[10,20,30,40,50,60,70,80,90]
# print(marks)
# print(marks[1:-1])
# print(marks[1:8:2])

# ------ LIST COMPREHENSION ------
# name=["milo","sarah","bruno","anasthesia","rosa"]
# namewith_o=[i for i in name if "o" in i]
# print(namewith_o)

name=["milo","sarah","bruno","anasthesia","rosa"]
namewith_o=[i for i in name if(len(i)) > 4]
print(namewith_o)