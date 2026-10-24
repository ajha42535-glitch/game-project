name=input("enter your name player").lower()
mobile_no=(input("enter your mobile no"))
if len(mobile_no)>10:
    print("enter a valid mobile no")
age=int(input("enter your age"))
if age>=18:
    print("you are valid for game")
else:
    print("you can play this game")
origin=input("enter your country origin")
input("press enter you are not robot")
while True:
    print("q1 what is value of 2+2?")
    user=int(input("enter a proper ans of each question"))
    if user==4:
        print("right")
        break
    else:
        print("wrong")
        
input("press enter so continue to menu.......")

while True:
    print("===========================")
    
    print("1) start the game\n")
    print("2)View the score\n")
    print("3) see leaderboard\n")
    print("4)EXIT\n")
    print("5) Move Level 2\n")
    print("6) view user login info:\n")
    print("=============================")
    
    choice=int(input("enter your choice"))
    if choice==1:
        input("press enter to play game")
        print("welcome to number guessing game")
        score=0
        health=10
        while True:
                import random
                num=random.randint(1,20)
                try:
                    player=int(input("enter a number any from 1 to 20\n"))
                except ValueError:
                    print("enter a correct num not a alphabet")
                if player==11:
                   print("near but not right")
                
                
                elif player==num:
                    print("you won")
                    score+=20
                
                
                else:
                    print("lose")
                    score-=1
                    health-=1
                    if health==0:
                        print("you cant play more game your health goes to end")
                        break

    elif choice==2:
        with open("vf.txt","a") as file:
            file.write("your score of 1st game is:"+str(score))
            file.write("your score of 2nd game is:"+str(score))
        with open("vf.txt","r") as file:
            b=file.readline()
            
            print(b)
            
    elif choice==3:
        if score>=20:
            print("1st Rank")
        elif score>=10:
            print("2nd Rank")
        elif score>=5:
            print("3rd Rank")
        else:
            print("No Rank")
    elif choice==4:
        input("press enter to quit game")
        break
    elif choice==5:
        score=0
        health=15
        while True:
            import random
            num2=random.randint(100,150)
            try:
                user=int(input("enter a number from 100 to 150:::::\n"))
            except ValueError:
                print("you cant insert alphabets  ")
            except:
                print("only numbers")
            if user==num2:
                print("you won")
                score+=6
                health+=5
            elif user>=151:
                print("please enter a num between 100 to 150")
            elif user<=99:
                print("enter a valid no from 100 to 150")
            else:
                print("you lose")
                score-=1
                health-=1
                if health==0:
                    print("empty health")
                    break
    elif choice==6:
        print("===============================\n")
        print("your name is",name)
        print("your Mobile No:",mobile_no)
        print("country:",origin)
        print("age:",age)
        print("==================================")

    else:
        print("Invalid choice")
