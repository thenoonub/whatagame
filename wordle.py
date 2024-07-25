word = 'hello'
v, w, x, y, z = word

i = 1
while i != 0:
    guess = input("guess the 5 letter word \n")

    a, b, c, d, e = guess

    if guess == word:
        print('Correct, you win!')
        i = 0
        break
    else:
        if a == v:
            print(a, "is in the right position")
        else:
            if a in word: 
                print(a, 'is in the word')

        if b == w:
            print(b, "is in the right position")
        else:
            if b in word: 
                print (b, 'is in the word')

        if c == x:
            print(c, "is in the right position")
        else:
            if c in word: 
                print (c, 'is in the word')
        
        if d == y:
            print(c, "is in the right position")
        else:
            if d in word: 
                print (d, 'is in the word')

        if e == z:
            print(c, "is in the right position")
        else:
            if e in word: 
                print (e, 'is in the word')