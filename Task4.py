#Rock_Paper_Scissors_Game
import random
while True:

    print("-----Welcome To Rock_Paper_Scissors_Game")

    user_score=0
    cmp_score=0
    ties=0

    name=input("Enter your name here==")
    print("""
    Winning Rules:
    1.Paper vs Rock ---> Paper
    2.Rock vs Scissors ---> Rock
    3.Scissors vs Paper ---> Scissors
    """ )

    print("""Choice are:
    1.Rock
    2.Paper
    3.Scissors""")
    choice=int(input("Enter your choice from 1-3 ......."))
    print()

    while(choice>3 or choice<1):
        choice=int(input("Enter Invalid Input"))

    if choice==1:
        user_choice="rock"
    elif choice==2:
        user_choice="paper"
    else:
        user_choice="Scissors"

    print("\nuser choice is  ==",user_choice)
    print("\nNow it is Computer's turn")

    Computer=random.randint(1,3)

    if Computer==1:
        cmp_choice="Rock"
    elif Computer==2:
        cmp_choice="Paper"
    else:
        cmp_choice="Scissors" 

    print("\nThe computer choice is ==",cmp_choice)

    if((user_choice=="paper" and cmp_choice=="Rock")or (user_choice=="rock" and cmp_choice=="Paper")):
        print("Paper Wins")
        result="paper"
    elif((user_choice=="Scissors" and cmp_choice=="Rock")or (user_choice=="rock" and cmp_choice=="Scissors")):
        print("Rock Wins")
        result="Rock"
    elif(user_choice==cmp_choice):
        print("it is a tie")
        result="tie"
    else:
        print("Scissors Wins")
        result="Scissors"

    if result=="tie":
        ties+=1
    elif result==user_choice:
        print("User Wins")
        user_score+=1
    else:
        print("Computer Wins")
        cmp_score+=1

    print("Score are   ")
    print(name,"S score is ",user_score)
    print("Computer'S score is ",cmp_score)
    print("ties are : ",ties)

    repeat=input("Do you want to play again == ")
    if(repeat=="No" or repeat=="no"):
        break


print("Game Over!")
print("Thank")
