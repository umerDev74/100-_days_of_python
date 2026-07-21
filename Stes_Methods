# for union and update()
s1 = {1, 2, 3, 4, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))  # union() method

s1.update(s2)  # update() method
print(s1,s2)

# INTERSECTION METHODS
print(s1.intersection(s2))  # intersection() method

# SYMMETRIC DIFFERNCE--------
city1 = {"khutti","zandani","sheru","saggu"}
city2 = {"khutti","gandi","saggu","zafar"}
city3 = city1.symmetric_difference(city2)
print(city3)

# DIFFERNCE-----
city1 = {"khutti","zandani","sheru","saggu"}
city2 = {"khutti","gandi","saggu","zafar"}
city3 = city1.difference(city2)
print(city3)

# Is disjoint Method-----

# agar dono sets me intersection nhi hai tu true warna ye false hoga
city1 = {"khutti","zandani","sheru","saggu"}
city2 = {"khutti2","gandi","saggu2","zafar"}
print(city1.isdisjoint(city2))

# ISSuperset

# ye is disjoint ka ulat hai yahan par agar intersection ho tu ye true ho ga warna false ho ga
city1 = {"khutti","zandani","sheru","saggu"}
city2 = {"khutti","gandi","saggu","zafar"}
print(city1.issuperset(city2))

# issubset_Method

# is me agar set2 ke sare elements hai set1 me tu ye true hoga warna false
city1 = {"khutti","zandani","sheru","saggu"}
city2 = {"khutti","saggu"}
print(city2.issubset(city1))

# Add_Method-------
num = {"n1","n2","n3"}
num.add("n4")
print(num)

"""agar remove method me koi aisi chese remove karna jo set me hai hi nahi tu ye error de ga
leikn agar ham dicard method use kare tu ye error nahi de ga aur agar wo number set me hoga
tu delete warna error nahi hoga"""
 
# Remove Method

# num.remove("n2")
# print(num)

# discard_method-----
num.discard("n1")
print(num)