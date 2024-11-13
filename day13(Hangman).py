import random

hangmanpics = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']



word_list = ["apple","beans","egg","yoghurt","aardvark"]

random_word = random.choice(word_list)
life = 6
# placeholder = "_" * len(chosen_word)
placeholder = []
for i in range(len(random_word)):
    placeholder.append("_")

game_over = False
while not game_over:
    # print(f"chars spy: {chars}")
    print(f"{life}/6")
    print(f"{"".join(placeholder)}\n")
    guess = input(f"Guess a letter(Above is the {len(random_word)} letter word) : ").lower()
    if guess in placeholder:
        print("Already given!")
    else:
        for i in range(len(random_word)):
            if guess == random_word[i]:
                placeholder[i]=guess
            
        # else:
    final = "".join(placeholder)
    if final == random_word:
            print(f"Well done! Your word is: {final}")
            break
    if guess not in random_word:
        life = life - 1
        print("Wrong!")
        print(hangmanpics[6-life])
         
    if life == 0:
         print(f"Game Over!, Life = {life}/6")
         print(hangmanpics[6])
         game_over = not game_over
