# # # # print("hey i am a \"good boy\" \n and this viewer is also a good boy/girl")
# # # # print("hey",5,6, sep="~")

# # # a=50
# # # b=40
# # # print("The Value of",a,'+',b,'=',a+b)
# # # print("The Value of",a,'-',b,'=',a-b)
# # # print("The value of",a,'*',b,'=',a*b)
# # # print("The value of",a,'/',b,'=',a/b)

# # a=input("Enter your name:")
# # print("My name is:",a)

# # x=input("Enter 1st number:")
# # y=input("Enter 2nd number:")
# # # print(x+y)
# # print(int(x)+ int(y))


# name = 'umer nawaz'
# string='''he said,
# hi harry
# hello
# "i want to eat apple"
# are you want anything
# '''
# # print('Hello '+name)
# # print(string)
# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])

# print("lets use a for loop\n")
# for character in name:
#     print(character)

# fruit = "Mango"
# mangolen = len(fruit)
# print(mangolen)

# print(fruit[0:4])
# print(fruit[1:4])

# print(fruit[:5])
# print(fruit[0:-3])
# #print(fruit[-1:-3])
# print(fruit[-3:-1])
# -------QUIZ-----------
# nm="Harry"
# print(nm[-4:-2])


# --- String Methods --- #

a="Umer!!!! nawaz Umer hello umer"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Umer","Jhon"))
print(a.split(" "))
heading="introduction oF pYthon"
print(heading.capitalize())
str1="Welcome to a Pakistan##"
print(str1.center(30))
print(a.count("Umer"))
print(str1.endswith("#"))
print(str1.endswith("a",10,15))
str2="he's name is Dan, He is a good man"
print(str2.find("Dans"))
print(str2.index("Dan"))
str3="welcomtopakistan"
print(str3.isalnum())
print(str3.isalpha())
str4="welcom to pakistan\n"
print(str4.islower())
str5="WELCOME"
print(str5.isupper())
print(str4.isprintable())
str6="    "
print(str6.isspace())
str7="Hello World"
print(str7.istitle())
str7="Hello world my name is khan"
print(str7.istitle())
print(str7.title())