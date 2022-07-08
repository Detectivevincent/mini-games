import random 
def game():  
    num = random.randint(1, 100) 
    total = 0 
    n = 0
    while True: 
        n = int(input("Guess the number")) 
        total += 1 
        if n < num: 
            print("No, too low") 
        elif n > num: 
            print("No, too much") 
        else: 
            print(f' Yes! You win with {total} gueses') 
            break 
game()
