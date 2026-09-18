# x=10 #global variable

# def my_function():
#     global x
#     x=20 #modifying global variable

#     y=5
#     print(y) #local variable

# my_function()

# print(x)

# ------------------------------------------------------

# 1. Global Variable (Ye function ke bahar hai)
x = "Main Global Variable hoon"


def my_function():
    # 2. Local Variable (Ye function ke andar hai)
    y = "Main Local Variable hoon"

    # Function ke andar dono ko print karte hain
    print("--- Function ke andar ---")
    print(x)  # Accessible (Global variable andar bhi milta hai)
    print(y)  # Accessible (Local variable function ke andar kaam karega)


# Function ko call karte hain
my_function()

# Function ke bahar dono ko print karne ki koshish karte hain
print("\n--- Function ke bahar ---")
print(x)  # Accessible (Global variable bahar bhi chalega)

# print(y)  <-- Agar aap is line se '#' hata kar run karoge, toh ERROR aayega!
# Kyun ke 'y' sirf 'my_function' ke andar tak hi zinda tha.