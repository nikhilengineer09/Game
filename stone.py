import random
print(" Rules: 1) Rock wins against scissors.\n 2) Scissors wins against Paper.\n 3) Paper wins against rock.")

user=input("Enter you choice(rock, paper, scissors): ")
options=['rock', 'paper', 'scissors' ]
computer=random.choice(options)
print("You chose: ") 
print(user)
print("Computer chose: ")   
print(computer)



if user=="rock":
    if computer=="scissors":
        print("Hurray! You Won")
    elif computer=="paper":
        print("Better luck next time, You lose.")
    else:
        print("It's a tie.")

        
if user=="paper":
    if computer=="scissors":
        print("Better luck next time, You lose.")
    elif computer=="Rock":
        print("Hurray! You Won")
    else:
        print("It's a tie.")
    
    
if user=="scissors":
    if computer=="rock":
        print("Better luck next time, You lose.")
    elif computer=="paper":
        print("Hurray! You Won")
    else:
        print("It's a tie.")
        

    


