from random import randint

from game_data import data
from art import logo, vs, game_over



# choose a first person to compare
def choose_from_list():
    '''
    Chooses one value randomly from a list then removes the value from the list
    '''
    #choses a random integer from 0 to the number equal to the length of the data
    random_number = randint(0, len(data) - 1)
    chosen_data = data[random_number]
    return chosen_data
    
def choose_A_and_B():
    '''
    Create an array of two values by calling the choose_from_list function to make sure the two chosen are always unique
    '''
    chosen_data_list = []
    for _ in range(2):
        chosen_data_list.append(choose_from_list())
    if chosen_data_list[0] == chosen_data_list[1]:
        choose_A_and_B()
    return chosen_data_list
    

    
def play_game():
    '''
    Void function
    Has the game logic and plays the game
    '''
    score = 0
    play = True
    game_lost = False
    # deconstructs the array to pick two values from the list to compare
    a,b = choose_A_and_B()
    while play:
        # moves what was b to a then chooses a new random dictionary for b
        a = b
        b = choose_from_list()
        
        if not game_lost:
            print(logo)
        if score > 0:            
            print(f"You're right! Current score: {score}")
        if game_lost:
            print(logo)
            print(f"Sorry that's wrong. Final Score: {score}")
            break
        print(f"Compare A: {a['name']} {a['description']} from {a['country']} ")
        print(vs)
        print(f"Against B: {b['name']} {b['description']} from {b['country']} ")
        
        follower_count_A = a['follower_count']
        follower_count_B = b['follower_count']
        if follower_count_A > follower_count_B:
            correct_answer = 'A'
        else:
            correct_answer = 'B'
        
        
        print('This is the correct answer',correct_answer)
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if user_guess == correct_answer:
            score += 1
        else:            
            game_lost = True




def play_again():
    '''
        Void Function
        Asks the user if the user wants to keep playing
    '''
    keep_playing = True
    play_game()
    while keep_playing:
        play_again_input = input("Would you like to play again y/n \n")
        if play_again_input == 'y':
            play_game()
        else:
            print(game_over)
            keep_playing = False

play_again()