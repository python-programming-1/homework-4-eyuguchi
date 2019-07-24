import random

playerScore = 0
computerScore = 0 


request = ['sc']    
plays = ['r', 's', 'p']
answers = ['y','n']

letsplay = True

while True: 
    your_move = input('Make your move (r/s/p or sc for score):')
    computer_move = random.choice(plays)

    print('robot played ' + computer_move)

    if your_move == computer_move:
        print('Draw!')
    
    elif your_move == 'p':
        if computer_move == 's':
            print ('You lose. >:)')
            computerScore += 1
        else:
            print ('You win. :(')
            playerScore += 1
        
    elif your_move == 's':
        if computer_move == 'r':
            print ('You lose. >:)')
            computerScore += 1
        else:
            print ('You win. :(')
            playerScore += 1

    elif your_move == 'r':
        if computer_move == 'p':
            print ('You lose. >:)')
            computerScore += 1
        else:
            print ('You win. :(')
            playerScore += 1
    
                    
            
    play_again = input ('Would you like to play again? (y/n):')
    if play_again == 'y':
        continue
    else:
        break


    

    
    
        

    





