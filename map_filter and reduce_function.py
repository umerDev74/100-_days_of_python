
# REDUCE_FUNCTION >>>>>>>>>>

from functools import reduce

numbers = [1,2,3,4,5,6]

sum = reduce(lambda x,y: x+y, numbers)

print(sum)


# #   MAP_FUNCTION ----------
# #  without map function >>>>>
# def cube(x):
#     return x*x*x
# print(cube(2))

# l=[1,2,3,4,6,5]
# newl=[]

# for item in l:
#     newl.append(cube(item))
# print(newl)

# # now by using map_function and also by lambda function >>>>>>>

# l=[1,2,3,4,6,5]
# newl = list(map(lambda x:x*x*x, l))

# print(newl)

# # FILTER_FUNCTION >>>>>>>>>>>>>

# l=[1,2,3,4,6,5]
# myfile = list(filter(lambda x: x>3, l))

# print(myfile)
