import random
l=["rock","paper","scissors"]
s=str(random.choice(l))
print("Welcome to ROCK, PAPER, SCISSORS game")
print("The computer has chosen its choice, it is your turn to choose now")
b=str(input("Enter your choice: "))
c=b.lower()
if(s=="rock" and c=="paper"):
    print(f"You win, your choice was {c}, computer's choice was {s}")
elif(s=="paper" and c=="scissors"):
    print(f"You win, your choice was {c}, computer's choice was {s}")
elif(s=="scissors" and c=="rock"):
    print(f"You win, your choice was {c}, computer's choice was {s}")
elif(s=="rock" and c=="scissors"):
    print(f"Computer wins, your choice was {c}, computer's choice was {s}")
elif(s=="paper" and c=="rock"):
    print(f"Computer wins, your choice was {c}, computer's choice was {s}")
elif(s=="scissors" and c=="paper"):
    print(f"Computer wins, your choice was {c}, computer's choice was {s}")
else:
    print("It is a tie")
  