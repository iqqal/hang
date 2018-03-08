print "WELCOME TO HANGMAN GAME"
print "one word, adjective, 5 letters ... good luck"
word = "short"
guess = ["*","*","*","*","*"]
mistakes = 0
word_length = len(word)
starter = 0
while starter < word_length:
    first_letter = raw_input("enter letter : ")
    if first_letter in word:
        print "true"
        fl_location = word.find(first_letter) #inserted letter location
        fl_locationnew = fl_location + 1
        print "this letter is the " +str(fl_locationnew)
        guess[fl_location] = first_letter
        if first_letter == guess[fl_location]:
            print "you already guess that letter ... "

        print guess
        print ""
        print "__________________________________"
        starter+= 1
    else:
        print "this is mistake"
        mistakes += 1
        if mistakes == 6:
            starter = len(word)
            print "GAME OVER"
        else:
            print "try next letter"
            print ""
            print "__________________________________"








if guess == ["s", "h", "o", "r", "t"]:
    print "GAAAAAAAMEEEEEE OVVVVVVVERRRRR ,,, YOUUUUU WIIINNNNNNNNN"
else:
    print "YOOOOOUUUUUUUUUUU LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOSE!!!!!!!!!!"
exit = raw_input("press enter to exit")
