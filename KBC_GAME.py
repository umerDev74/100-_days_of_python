# 1. Questions ki list (Har element me: Question, Charo Options, aur Correct Option Number hai)

questions = [
    [
    "which programing language is known as the language of AI?",
    ["python","java","c++","c#"],
    1
    ],
    [
    "Who developed Python Programming Language?",
    ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
    2
    ],
    [
    "Which data type is used to store multiple items in a single variable?",
    ["Integer", "String", "List", "Float"],
    3
    ],
    [
    "What is the correct extension of a Python file?",
    [".py", ".python", ".pyt", ".pt"],
    1
    ],
    [
        "Which keyword is used to create a function in Python?",
        ["func", "define", "def", "function"],
        3 # 'def' sahi jawab hai
    ],
    [
        "What is the output of print(2 ** 3) in Python?",
        ["6", "8", "9", "5"],
        2 # 2 ki power 3 = 8 hota hai
    ],
    [
        "Which of the following is NOT a core data type in Python?",
        ["List", "Dictionary", "Tuple", "Class"],
        4 # Class data type nahi hai
    ],
    [
        "How do you start a loop in Python?",
        ["for", "while", "both for and while", "loop"],
        3 # Dono loops hote hain
    ]
]

# 2. Har level ke prize money ki list

levels = [500, 1000, 2000, 5000, 10000, 20000, 40000, 80000]
money = 0

print("\n========WELCOME TO KBC GAME========\n")

# 3. Loop jo har question ko baari baari chalayega

for i in range(len(questions)):
    current_question = questions[i][0]
    options = questions[i][1]
    correct_answer = questions[i][2]


 # Question aur uski prize money display karna

    print(f"Question for Rs. {levels[i]}:")
    print(f" {current_question}")

    # option display karna
    print(f"1. {options[0]}         2. {options[1]}")
    print(f"3. {options[2]}         4. {options[3]}")

    # User se input lena

    user_replay = int(input("\nEnter your choice (1-4) or press 0 to Quit:"))

    # Agar user Quit karna chahta hai

    if user_replay == 0:
        print("\nYou chose to quit the game.")
        break

    # Jawab check karna 

    if user_replay == correct_answer:
        print(f"SAhi Jawab! App jeet chuke hain Rs. {levels[i]}\n")
        money += levels[i]  # Money update kardi
        print("----------------------------------------------")
    else:
        print("Ghalat Jawab! Afsoos, is sawal ke paise nahi milenge. Agla sawal dekhein:")
        print("----------------------------------------------")
        continue  # agar jawab ghalat ho gaya hai tu agle par jao 

# Final Take-Home Amount Display karna

print("----------------------------------------------")
print(f" GAme Over! Total Amount you are taking home: Rs. {money}")
print("----------------------------------------------")