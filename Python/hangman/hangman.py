import random
words = []
# get the words
w = open("words", 'r')
for lines in w:
    words.append(lines)
w.close()
rng_yn = input("Do want a word to be generated for you? ").lower()
if rng_yn == "yes":
    Word = words[random.randint(0, 3000)]
elif rng_yn == "no":
    Word = input("PLease enter your word ")
else:
    print("yes or no are the only valid responses!")
    exit()
def guess(guesses):
    if guesses > 0:
        imp = str(input("please enter your guess? "))
        if len(imp) > 1:
            print("Your guess must only be one letter!")
        else:
            wordList = list(Word)
            del wordList[-1]
        if imp in wordList:
                value = wordList.index(imp)
                wordList.remove(imp)
                print("you have guessed correctly!")
                print(imp + " was correct")
                print(imp + " was the " + str(value + 1) + " letter" )
                if len(wordList) == 0:
                    print("You have won the word is " + Word)
                else:
                    guess(guesses)
        elif imp not in wordList:
            print("you have guessed incorrectly!")
            print(imp + " was not correct")
            guesses -=1
            print("you have " + str(guesses) + " guesses remaining")
            guess(guesses)
    else:
        print("You have run out of guesses. The word is " + Word)
        exit()
g_num = (len(Word) - 1) * 2
guess(g_num)
