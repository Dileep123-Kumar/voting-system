
#Simple voting program for 3 candidates using a while loop.........
#Candidates: DILEEP, MANOJ, PARKASH


#starts with vote counters for each candidate........
can1=0
can2=0
can3=0
# Showing Candidates making easy for voters so, they can vote easily according to thier choice
print("1) DILEEP \n2) MANOJ \n3) PARKASH \n4)Show votes  \n5) winner")
#starts infinite loop because we dont know how many voters come for voting
while True:
    # taking choice in numbers by user because voter can vote appropriate candidate......
    choice=int(input("Enter the Number for voting candidate/Result/Winner: "))
    # stop the programme if user enter the 0
    if choice == 0:
        break
    elif choice == 1:
        can1+=1 # adding vote of Dileep if user enter 1........
        print("The vote of dileep:",can1)
    elif choice == 2:
        can2+=1 # adding vote of Manoj if user enter 2........
        print("The vote of Manoj: ",can2)
    elif choice == 3:
        can3+=1 # adding vote of Parkash if user enter 3......
        print("The vote of parkash: ",can3)
        
    elif choice == 4: #showing votes if user entere 4........
        print(f"Votes:\nDILEEP: {can1}\nMANOJ: {can2}\nPARKASH: {can3}")

    elif choice == 5: 
        # checking the votes for Dileep if he achive more votes than other candidates
        if can1 > can2 and can1 > can3:
            print(f"Winner is: Congratulations! The election is Won by  DILEEP by the leading of {can1} votes")
        # checking the votes for Manoj if he achive more votes than other candidates
        elif can2 > can1 and can2 > can3:
            print(f"Congratulations! The election is Won by  MANOJ by the leading of {can2} votes")
        # checking the votes for Parkash if he achive more votes than other candidates
        elif can3 > can1 and can3 > can2:
            print(f"Congratulations! The election is Won by  PARKASH by the leading of {can3} votes")
        else:
            print(f"Election has tied because the votes of Two Candidates are Equal")   #if two candidates more votes than third then showing this message
    else:
        print("Invalid Entry")





