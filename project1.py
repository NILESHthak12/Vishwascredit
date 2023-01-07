candidate1 = input("Enter 1st candidate name:")
candidate2 = input("Enter 2st candidate name:")

candidate1_votes = 0
candidate2_votes = 0

voters_id = [1,2,3,4]
number_of_voters = len(voters_id)
print("number of voters:",number_of_voters)
voted = []
while True:
    if voters_id ==[]:
        print("voting is over")
        if candidate1_votes > candidate2_votes:
            print(f"{candidate1} won the election with {candidate1_votes}")
        elif candidate2_votes > candidate1_votes:
            print(f"{candidate2} won the election with {candidate2_votes}")
        elif candidate1_votes == candidate2_votes:
            print("tied.......")
        break
            
            
    else:
        voter = int(input("Enter your id:"))
        if voter in voted:
            print("You already voted:")
        else:
            if voter in voters_id:
                print(f"1.{candidate1} \n2.{candidate2}")
                choice=int(input("enter your choice"))
                if choice==1:
                    candidate1_votes += 1
                    print(f"you voted {candidate1}")
                
                elif choice==2:
                    candidate2_votes += 2
                    print(f"you voted {candidate2}")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("yor are not allowed to vote:")