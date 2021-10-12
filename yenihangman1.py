import random
words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
guesses= ' '
mode=True
can=5
def changeMod(mode):
    if mode==True:
        mode=False
    else:
        mode=False


while can>0:
    guess=input("\nBir harf giriniz: ")
    if guess in word:
        print(f"Guessed word: {guess}   And you are in {mode} MOD")
    else:
        print(f"Guessed word: {guess}   And you are in {mode} MOD")
        can-=1
    print(f"You have {can} guesses left")
    
    guesses= guesses + guess
    failed=0
    for letter in word:
        if letter in guesses:
            print(f"{letter}", end=" ")
        else:
            print(f"-", end=" ")
            failed+=1
    if failed==0:
        print("\nYou won the game")
        break
    if mode==True:
        if guess not in word:
            can=can
    else:
        if guess not in word:
            can-=1

else:
    print("\nUnfortunately you didn't find secret word")



