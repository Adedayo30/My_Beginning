#This program prints assigned digit equivalent for every word you type in
instruction = ('\nInstructions: The points of your word will be added and printed for you' '\n'
               'Note: Your word must be correct!' '\n'
               '\n1. A, E, I, L, N, O, R, S, T, U: is assigned 1 point each;' '\n'
               '2. D, G: is assigned 2 points each;' '\n'
               '3. B, C, M, P: is assigned 3 points each;' '\n'
               '4. F, H, V, W, Y: is assigned 4 points each;' '\n'
               '5. K: is assigned 5 point each;' '\n'
               '6. J, X: is assigned 8 points each;' '\n'
               '7. Q, Z: is assigned 10 points each;')

print(instruction)
while True: #for continuity 
    user_input = input(str('Enter your choice word: ')) #takes user word as string
    letter_value = {'A':1, 'E':1, 'I':1, 'L':1, 'N':1, 'O':1, 'R':1, 'S':1, 'T':1, 'U':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10}
    if user_input == 'q': #for quit
            break #In case user wants to stop
    else:
        def word_score(alphabets): #function that checks
            y= [] #I use this list to get the value of each letter.
            word = alphabets.upper() #All user's input is changed to upper case
            for k, v in letter_value.items(): #k for key, v for value; any letter can be used instead of k and v
                for i in word: #each character of input
                    if i == k: #checks for letter in letter_value dictionary
                        y.append(v) #the value of eack letter is passed to emptylist
            return sum(y) #All the items in list y are added together         
        
        print('The sum of letters of your word is: ', word_score(user_input)) #The result is printed

