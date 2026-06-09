import random
def loadstats(): 
 try:
    
     with open("stats.txt", "r") as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
     score, rounds, streak, best_streak = map(int, line1.split(","))
     history = line2.split()
     return  score, rounds, streak, best_streak, history
 except:
    score = 0
    rounds = 0
    streak = 0
    best_streak = 0
    history = []
    return score, rounds, streak, best_streak, history
score, rounds, streak, best_streak, history = loadstats()
def savestats():
     with open("stats.txt", "w") as f:
      f.write(f"{score},{rounds},{streak},{best_streak}\n")
      f.write(" ".join(history))
def stats():
     win_rate=(score/rounds)*100
     print("="*30)
     print("STATS")
     print("="*30)
     print(f"Score:{score}/{rounds}")
     print(f"Streak:{streak}")
     print(f"Win Rate:{win_rate:.2f}%")
     print(f"History:"," ".join(history))
     print(f"Best Streak:{best_streak}")
     print("="*30 + "\n")
def playgame():

    a = 0
    
    print("Choose your difficulty..")
    print("Level 1. 1-50, 10 attempts[EASY]")
    print("Level 2. 1-100, 7 attempts[MEDIUM]")
    print("Level 3. 1-200, 5 attempts[HARD]")
    d=input("Choose your difficulty(1/2/3):")
    if d=="1":
        max_a=10
        max_n=50
    elif d=="2":
        max_a=7
        max_n=100
    elif d=="3":
        max_a=5
        max_n=200
    else:
        print("Returning to default level 2")
        max_a=7
        max_n=100
    n = random.randint(1, max_n)
    print(f"Total attempts:{max_a}")

    while a < max_a:

        try:
            guess = int(input(f"Enter your guess between 1-{max_n}: "))

        except:
            print(f"Enter a valid number between 1-{max_n}")
            continue

        a += 1

        if guess == n:
            print("CONGRATULATIONS! YOU HAVE GUESSED THE NUMBER")
            return True

        elif abs(guess - n) <= 2:
            print("Very Close")
        elif abs(guess-n)<=5:
            print("Close")
        elif abs(guess-n)>=20:
            print("Way too far")

        if guess < n:
            print("Too small")

        else:
            print("Too big")


        if a < max_a:
            print(f"Attempts left: {max_a-a}")

    print("Game Over! The number was",n)
    return False
    
print("="*30)
print("NUMBER GUESSING GAME")
print("="*30)
while True:
 print("Hello User! what do you wish to do today")
 print("1. Play Game")
 print("2. Load Stats")
 print("3. Reset Stats")
 print("4. Exit")
 choice2=input("What do you choose(1/2/3/4): ")
 if choice2 =="1":  
  while True:
      rounds+=1
      result = playgame()

      if result:
        print("You won!")
        score+=1
        streak+=1
        best_streak=max(best_streak,streak)
        history.append("W")
        


      else:
        print("You lost!")
        streak=0
        history.append("L")

      print("\n")
    
      if len(history)>10:
            history.pop(0)   
    
      stats()
      play = input("Do you want to play again (yes/no): ").lower()

      if play == "yes" or play == "y":
        print("Restarting Game...\n")
        continue

      else:
        print("Goodbye!")
      savestats()
      break

 elif choice2 == "2":
     if rounds == 0:
      print("\n")
      print("You have to play 1 round first to calcultate Stats")
      print("Current STATS 0")
      print("\n")
     else:
      print("\n")
      stats()
      print("\n")
      
 elif choice2=="3":
     score = 0
     rounds = 0
     streak = 0
     best_streak = 0
     history = []
     savestats() 
     print("\n")
     print("Successfully reset all stats")
     print("\n")
      
 elif choice2=="4":
    print("\n")
    print("Goodbye")
    print("\n")
    break
 else:
    print("\n")
    print("Invalid Choice")
    print("\n")