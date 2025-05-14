
# Function to get player1 name
def get_player1_name():
    player1 = input(f"What is your name player1?: ")
    return player1

# Function to get player2 names
def get_player2_name():
    player2 = input(f"What is your name player2?: ")
    return player2

# Function to get number of rounds
def get_rounds():
    while True:
        try:
            rounds = int(input("Enter number of rounds: "))
            if rounds > 0:
                return rounds
            print("\nPlease enter a positive number.😀")
        except ValueError:
            print("\nPlease enter a valid number.😀")

# Function to get user input
def get_choice(player):
    # Mapping user input to string values
    # 1 == rock, 2 == paper, 3 == scissors
    choice_map = {1: 'rock', 2: 'paper', 3: 'scissors'}
    while True:
        try:
            choice = int(input(f"{player}, enter your choice (1, 2, 3): "))
            if choice  in choice_map:
                return choice_map[choice]  # Return the mapped string value
            else:
                print("\nWrong Input❌ \nChoice must be 1, 2, or 3")
        except ValueError:
            print("\nPlease enter a valid number.⛔")

# Function to randomly choose between rock, paper, and scissors
def random_choice():
    import random
    return random.choice(['rock', 'paper', 'scissors'])

# Function to check the winner
def check_winner(choice1, choice2, player1, player2):
    
    #'rock' == 1 
    #'paper' == 2 
    #'scissors' == 3

    # Define winning combinations
    if choice1 == choice2:
        print("It's a tie!")
        return "Its a tie"
    
    
    while choice1 == 'rock':
        # rock vs scissors
        if choice2 == 'scissors':
            print("rock crushes scissors")
            print(f"{player1} wins!")
            return f"{player1} wins!"
        
        # rock vs paper
        elif choice2 == 'paper':
           print("paper covers rock")
           print(f"{player2} wins!")
           return f"{player2} wins!"

    while choice1 == 'scissors':
        # scissors vs paper
        if choice2 == 'paper':
            print("scissors cuts paper")
            print(f"{player1} wins!")
            return f"{player1} wins!"
        
        # scissors vs rock
        elif choice2 == 'rock':
            print("rock crushes scissors")
            print(f"{player2} wins!")
            return f"{player2} wins!"
        
    while choice1 == 'paper':
        # paper vs rock
        if choice2 == 'rock':
            print("paper covers rock")
            print(f"{player1} wins!")
            return f"{player1} wins!"
        
        ## paper vs scissors
        elif choice2 == 'scissors':
            print("scissors cuts paper")
            print(f"{player2} wins!")
            return f"{player2} wins!"

# Update scores based on the result
def score(result, player1, player2):
    p1_score = 0
    p2_score = 0
    if f"{player1} wins!" in result:
        p1_score += 1
    elif f"{player2} wins!" in result:
        p2_score += 1

    #print(f"Scores: {p1} - {p2}")
    return p1_score, p2_score

# Final score
def final_score(player1, player2, p1_score, p2_score):
    print()
    print("-"* 30)
    print('End of Game results📌')
    print(f'{player1}: {p1_score} \n{player2}: {p2_score}')
    if p1_score > p2_score:
        print(f"{player1} wins the Game🏆")
    elif p2_score > p1_score:
        print(f"{player2} wins the Game🏆")
    else:
        print("It's a tie!😊")

# Function to simulate a game between two human players
def human_vs_human():
    print("\nPlayer 1 vs Player 2")
    print("-" * 30)
    print()
    
    # Getting player names
    player1 = get_player1_name()
    player2 = get_player2_name()

    # Get number of rounds
    rounds = get_rounds()

    # Initialize scores
    p1_score = 0
    p2_score = 0

    # Loop through number of rounds
    for i in range(rounds):
        print(f"\nRound {i + 1}:")
        print("Choices \n1. Rock \n2. Paper \n3. Scissors")
        choice1 = get_choice(player1)
        choice2 = get_choice(player2)
        print(f"\n{player1} choses: {choice1}")
        print(f"{player2} choses: {choice2}")

        # Check result
        result = check_winner(choice1, choice2, player1, player2)

        # Adding scores for each round
        p1, p2 = score(result, player1, player2)
        p1_score += p1 
        p2_score += p2
        
    final_score(player1, player2, p1_score, p2_score)

# Function to simulate a game between a human and the computer
def human_vs_computer():
    print("\nPlayer vs Computer")
    print("-" * 30)
    print()
    # Getting player names
    player1 = get_player1_name()
    player2 = "Computer"
    
    # Get number of rounds
    rounds = get_rounds()

    # Initialize scores
    p1_score = 0
    p2_score = 0

    # Loop through number of rounds
    for i in range(rounds):
        print(f"\nRound {i + 1}:")
        print("Choices \n1. Rock \n2. Paper \n3. Scissors")
        choice1 = get_choice(player1)
        choice2 = random_choice()
        print(f"\n{player1} choses: {choice1}")
        print(f"{player2} choses: {choice2}")
        
        result = check_winner(choice1, choice2, player1, player2)
    
        # Adding scores for each round
        p1, p2 = score(result, player1, player2)

        p1_score += p1
        p2_score += p2

    final_score(player1, player2, p1_score, p2_score)

# Function to simulate a game between two computers
def computer_vs_computer():
    print("\nComputer 1 vs Computer 2")
    print("-" * 30)
    print()
    # Getting player names
    player1 = "Computer 1"
    player2 = "Computer 2"

    # Get number of rounds
    rounds = get_rounds()

    # Initialize scores
    p1_score = 0
    p2_score = 0

    # Loop through number of rounds
    for i in range(rounds):
        print(f"\nRound {i + 1}:")
        choice1 = random_choice()
        choice2 = random_choice()
        print(f"{player1} choses: {choice1}")
        print(f"{player2} choses: {choice2}")
                
        result = check_winner(choice1, choice2, player1, player2)
    
        # Adding scores for each round
        p1, p2 = score(result, player1, player2)

        p1_score += p1
        p2_score += p2

    final_score(player1, player2, p1_score, p2_score)

# Function to display the main menu and handle user input
def main_menu():
    
    print("\nMain Menu:")
    print("1. Human vs Human")
    print("2. Human vs Computer")
    print("3. Computer vs Computer")
    choice = input("Select game mode (1-3): ")

    # Validate user input
    if choice == '1':
        human_vs_human()
    elif choice == '2':
        human_vs_computer()
    elif choice == '3':
        computer_vs_computer()
    else:
        print("Invalid choice. Please try again⛔.")
        main_menu()

# Main function to run the game
def main():
    print("-" * 30)
    print("Rock Paper Scissors Game👾")
    print("-" * 30)

    while True:
        main_menu()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
if __name__ == '__main__':
    main()