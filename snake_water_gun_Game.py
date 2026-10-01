import random
def check_win_matrix(computer,player):
    matrix = [
        [0,1,-1], # player = snake (0)
        [-1,0,1],# player = water (1)
        [1,-1,0]# player = gun (2)
    ]

    return matrix[player][computer]

# main execution ..........

def main():
    player_score = 0
    computer_score = 0
    outcomes = {0: "Round Draw ...", 1: "You Win", -1: "You Lose!"}

    print("=================================================")
    print("=== Snake, Water, Gun Game (Total 10 rounds)===")
    print("=================================================")

    for round_num in range(1,11):
        print(f"\n--- Round {round_num} of 10 ---")
        while True:

            try:
                player = int(input("Enter your choice (0: Snake, 1: Water, 2: Gun): "))
                if player in [0, 1, 2]:
                    break
                else:
                    print("Invalid input! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        computer = random.randint(0, 2)


        print(f"computer chose: {computer}")
        print(f"You chose     : {player}")

        # Result from Matrix >>>>>>>>>>

        result = check_win_matrix(computer,player)
        print(f"Round result  :{outcomes[result]}")

        # Score Updation -------------

        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

# Final Result Summary >>>>>>>>>>

    print("\n" + "=" * 35)
    print(" ---------------- Final Result --------------")
    print("=" * 35)
    print(f"Your Total Score is  : {player_score}")
    print(f"Computer Total Score is  : {computer_score}")
        
    if player_score > computer_score:
        print("\nCongratulation! You Win The Game")
    elif computer_score > player_score:
        print("\nYou Lose! The Game")
    else:
        print("Overall Series Draw!")

if __name__ == "__main__":
    main()