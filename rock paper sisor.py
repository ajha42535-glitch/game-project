score=0
while True:
    print("=============================")
    print("1)start the game\n")
    print("2) see the score\n")
    print("3) seee leaderboard rank\n")
    print("4) EXIT\n")
    print("===============================")
    choice=int(input("enter a choice"))
    if choice==1:
        while True:
             computer="rock"
             player=input("enter a your time")
             if computer=="rock" and player=="paper":
                print("you won")
                score+=5
             elif computer=="rock" and player=="scisor":
                    print("you loss")
                    score-=1
             elif computer=="rock"and player=="rock":
                    print("tied")
                  
        
            
             
             else:
                   input("press enter to exit")
                   break
    elif choice==2:
         total_score=score
         print("Your Total score is :\n",total_score)
    elif choice==3:
         if score>=20:
              print("1ST Rank")
         elif score>=10:
              print("2ND Rank")
         else:
              print("no Rank")
    elif choice==4:
         print("Have a nice day")
         break
    else:
         print("Invalid")
    




