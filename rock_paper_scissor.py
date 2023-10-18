import random
l=["rock","paper","scissor"]
while True:
    player_count=0
    computer_count=0
    p=int(input('''
For Start The Game Press 1 or for stop the Game press 2 : 
1 Yes
2 No  
     '''))
    if p==1:
        for b in range(5):
            player=int(input('''
1 Rock
2 Scissor
3 Paper              
        '''))
            if player==1:
                player_choice="rock"
            elif player==2:
                player_choice="scissor"
            elif player==3:
                player_choice="paper"
            else:
                print("Invalid Option \n ")    
                break

            computer_choice=random.choice(l)

            if computer_choice==player_choice:
                print("Player Choice : ",player_choice)
                print("computer Choice : ",computer_choice) 
                print("Game Draw")
                player_count=player_count+1
                computer_count=computer_count+1 
            elif (computer_choice=="scissor" and player_choice=="rock") or (computer_choice=="rock" and player_choice=="paper") or (computer_choice=="paper" and player_choice=="scissor"):
                print("Player Choice : ",player_choice)
                print("computer Choice : ",computer_choice) 
                print("You win")
                player_count=player_count+1
            else:
                print("Player Choice : ",player_choice)
                print("computer Choice : ",computer_choice) 
                print("You Loss")
                computer_count=computer_count+1
        print("\n")        
        if computer_count==player_count:
            print("Game draw")
            print("Computer Score : ",computer_count)
            print("Player Score : ",player_count)   
        elif computer_count < player_count:
            print("You Win The Game")
            print("Computer Score : ",computer_count)
            print("Player Score : ",player_count)
        elif computer_count > player_count:
            print("You Loss The Game")
            print("Computer Score : ",computer_count)
            print("Player Score : ",player_count)             
    else:
        print("***Bye Bye***")
        break