if user_choice == comp_choice:
        print("It's a tie! 🤝🏻")
    elif(user_choice == 'rock' and comp_choice == 'scissors'):
        print("Congratulations! You Won!! 🎉")
        u_points += 1
    elif(user_choice == 'scissors' and comp_choice == 'paper'):
        print("Congratulations! You Won!! 🎉")
        u_points += 1
    elif(user_choice == 'paper' and comp_choice == 'rock'):
        print("Congratulations! You Won!! 🎉") 
        u_points += 1
    else:
        print("Oops! You Lose 😔")
        c_points += 1
    
    print(f"Score - You: {u_points}, Computer: {c_points}\n")