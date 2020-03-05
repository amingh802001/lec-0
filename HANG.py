import random
import string

WORDLIST_FILENAME = "words.txt"

class save (object):
    guess_remained = 6
    worning_remained = 3
    seret = []
    guessed = []
    hint = []
def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

worldlist = load_words()
def is_word_guessed(secret_word, letters_guessed):
    secret_word = list(secret_word)
    copy_s = secret_word[:]
    for i in letters_guessed:
        for j in copy_s:
            if i == j:
                if j in secret_word:
                    secret_word.remove(j)
    if len(secret_word) == 0:
        return True
    else:
        return

def get_guessed_word(secret_word, letters_guessed):
    secret_word = list(secret_word)
    hang = []
    for i in range(len(secret_word)):
        hang.append('_ ')
    for i in letters_guessed:
        for j in range(len(secret_word)):
            if i == secret_word[j]:
                hang[j] = secret_word[j]

    return hang

def get_available_letters(letters_guessed):
    maintained = list(string.ascii_lowercase)
    for i in letters_guessed:
        for j in maintained:
            if j == i:
                maintained.remove(j)
    return ''.join(maintained)

def choose_word(worldlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(worldlist)

def remove_space(my_word):
    copy_w = []
    for i in range(len(my_word)):
        if my_word[i] != ' ':
            copy_w.append(my_word[i])
    w = ''.join(copy_w)
    return w

def match_with_gaps(my_word, other_word):
    word = remove_space(my_word)
    if len(word) != len(other_word):
        return False
    for i in range(len(word)):
        if word[i]!= '_':
            if word[i] != other_word[i]:
                return False
    return True

def show_possible_matches():
    w = ''.join(get_guessed_word(save.seret, save.guessed))
    if len(save.hint) == 0:
      for world in worldlist:
         if match_with_gaps(w,world)== True:
            save.hint.append(world)
    else:
        chint = save.hint[:]
        for word in chint:
          if match_with_gaps(w,word) == False:
                 save.hint.remove(word)
    if len(save.hint) <= 5 :
        print('you lose one guess , wanna continue ? y/n')
        ans = input ()
        if ans == 'y' :
            print (save.hint)
            save.guess_remained -=1

            return 0
        else:
            
            return 0
    else:
     print(save.hint)

def hangman():
 save.seret = choose_word(worldlist)
 for i in range(len(save.seret)):
    save.guessed.append('_ ')
 print('____________________________________' + 'game started ')
 print ('the lenght =' , len(save.seret))
 while(save.guess_remained >= 0):
    print('_____________________________________________________________')
    if is_word_guessed (save.seret , save.guessed) == True:
        print('you won :)')
        break
    if save.guess_remained == 0:
        print('lost '+'\n'+' game over')
        break
    print('you can guess from :' , get_available_letters(save.guessed))
    print('guesses remained = ' , save.guess_remained)
    print('worning remaid =' , save.worning_remained)
    w = ''.join(get_guessed_word(save.seret, save.guessed))
    print(w)
    guess = input('guess:')
    if guess == '*':
        show_possible_matches()
        continue
    elif (len(guess) == len(save.seret)):
        if (str.isalpha(guess) == False):
            print('invalid!')
            if (save.worning_remained == 0):
                save.guess_remained -=1
            else:
                save.worning_remained -=1
        elif(save.seret == guess):
            print('you won! :)')
            break
        else:
            save.guess_remained -=1
            continue
    elif(len(guess) > 1 or str.isalpha(guess) == False or guess in save.guessed ):
        print('invalid!')
        if (save.worning_remained == 0):
            save.guess_remained -= 1
        else:
            save.worning_remained -= 1
    else:
     save.guessed.append(guess)
     if guess in save.seret :
        print ('it is there!')
     else:
        print ('not there')
        save.guess_remained -=1

hangman()








