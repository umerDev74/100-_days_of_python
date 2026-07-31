# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is:")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} * {i} = {int(a)*i}")

# # server base error ---------
# except Exception as e:
#     print(e)

# # hand made exception for error-----
# # except:
# #     print("invalid input!")

# print("some important line of code")
# print("------------------------------")
# print("End of program......")

#  HANDLING THE SPECIFIC ERROR --------

try:
    num= int(input("Enter an integer: "))
    a=[6,3]
    print(a[num])

except ValueError:
    print("Number enter is not integer!")
except IndexError:
    print("Index error!")