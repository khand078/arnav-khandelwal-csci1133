#==========================================
# Purpose: Print "who needs loops" 121 times
# Input Parameter(s): funtion1 - gives the text of "who needs loops"
#                   print_121/function2 - repeats the text
# Return Value(s): none
#==========================================

#making the first function call "who needs loops" five times
def function1():
    print("who needs loops")
    print("who needs loops")
    print("who needs loops")
    print("who needs loops")
    print("who needs loops")
#making the second function call the first function six times
def function2():
    function1()
    function1()
    function1()
    function1()
    function1()
    function1()
#making the third function call the second function four times and writing "who needs loops" to get the function to print 121 times
def print_121():
    function2()
    function2()
    function2()
    function2()
    print("who needs loops")

#==========================================
# Purpose: Gives a multiple choice question for the user to answer
# Input Parameter(s): text - what the category/question of choice will be
#                   optionA, optionB, optionC - the options the user can select between 
# Return Value(s): The answer associated to the letter the user selected is what is returned
#==========================================

def choice(text,optionA,optionB,optionC):
    #display the question and answers
    print(text) 
    print("A. ", optionA)
    print("B. ", optionB)
    print("C. ", optionC)
    #making the variable choose so there can be a conditional for the selected answer
    choose = str(input("Choose A, B, or C: ")) 
    if choose == "A":
        return optionA
    elif choose == "B":
        return optionB
    elif choose == "C":
        return optionC
    else:
        print("Invalid option, returning to A")
        return optionA
    
#==========================================
# Purpose: The function sets up a path for the cycle of questions
# Input Parameter(s): Choices for answers: A, B, C, or other characters (which will default to A)
# Return Value(s): Boolean values of True and False
#==========================================

def adventure():
    #This will be the first choice
    text = "Do you want whole grain, no bread, or wheat? "
    optionA = "Whole grain"
    optionB = "No bread"
    optionC = "Wheat"
    print(text) 
    print("A. ", optionA)
    print("B. ", optionB)
    print("C. ", optionC)
    choose = str(input("Choose A, B, or C: "))

    #This option A will bring you to the second question
    if choose == "A":
        text = "Do you want american cheese, pepperjack cheese, or cheddar cheese? "
        optionA = "American cheese"
        optionB = "Pepperjack cheese"
        optionC = "Cheddar cheese"
        print(text) 
        print("A. ", optionA)
        print("B. ", optionB)
        print("C. ", optionC)
        choose = str(input("Choose A, B, or C: "))

        #This option A will end the adventure with a True statement
        if choose == "A":
            print("Ayy that's a good burger")
            return True

        #This option B will bring you to the fourth question
        elif choose == "B":
            text = "Do you want it toasted, grilled, or cooked? "
            optionA = "Toasted"
            optionB = "Grilled"
            optionC = "Cooked"
            print(text) 
            print("A. ", optionA)
            print("B. ", optionB)
            print("C. ", optionC)
            choose = str(input("Choose A, B, or C: "))

            #This option A and B will end the adventure with a True statement
            if choose == "A":
                print("This is going to be one good burger")
                return True

            elif choose == "B":
                print("This is going to be one good burger")
                return True

            #This option C will end the adventure with a False statement
            elif choose == "C":
                print("Well that's just a gross burger")
                return False

            #This else will return the output to be option A
            else:
                print("Invalid option, returning to A")
                print("This is going to be one good burger")
                return True

        #This option C will bring you to the third question
        elif choose == "C":
            text = "Do you want turkey, bacon, or ham? "
            optionA = "Turkey"
            optionB = "Bacon"
            optionC = "Ham"
            print(text) 
            print("A. ", optionA)
            print("B. ", optionB)
            print("C. ", optionC)
            choose = str(input("Choose A, B, or C: "))

            #This option A will be False and will end the adventure here
            if choose == "A":
                print("Gross! Turkey will make it taste bad.")
                return False

            #This option B will bring you to fourth question 
            elif choose == "B":
                text = "Do you want it toasted, grilled, or cooked? "
                optionA = "Toasted"
                optionB = "Grilled"
                optionC = "Cooked"
                print(text) 
                print("A. ", optionA)
                print("B. ", optionB)
                print("C. ", optionC)
                choose = str(input("Choose A, B, or C: "))

                #This option A and B will end the adventure with a True statement
                if choose == "A":
                    print("This is going to be one good burger")
                    return True

                elif choose == "B":
                    print("This is going to be one good burger")
                    return True

                #This option C will end the adventure with a False statement
                elif choose == "C":
                    print("Well that's just a gross burger")
                    return False

                #This else will return the output to be option A
                else:
                    print("Invalid option, returning to A")
                    print("This is going to be one good burger")
                    return True


            #This option C will end the adventure with a True statement
            elif choose == "C":
                print("Oo ham is a good choice")
                return True

            #This else option will return the output to be option A
            else:
                print("Invalid option, returning to A")
                print("Gross! Turkey will make it taste bad.")
                return False

        #This else option will return the output to be option A   
        else:
            print("Invalid option, returning to A")
            print("Ayy that's a good burger")
            return True
            
    #This option B will be False and will end the adventure here
    elif choose == "B":
        print("How can you have a bruger with no bread?")
        return False

    #This option C will bring you to the third question
    elif choose == "C":
        text = "Do you want turkey, bacon, or ham? "
        optionA = "Turkey"
        optionB = "Bacon"
        optionC = "Ham"
        print(text) 
        print("A. ", optionA)
        print("B. ", optionB)
        print("C. ", optionC)
        choose = str(input("Choose A, B, or C: "))

        #This option A will be False and will end the adventure here
        if choose == "A":
            print("Gross! Turkey will make it taste bad.")
            return False

        #This option B will bring you to fourth question 
        elif choose == "B":
            text = "Do you want it toasted, grilled, or cooked? "
            optionA = "Toasted"
            optionB = "Grilled"
            optionC = "Cooked"
            print(text) 
            print("A. ", optionA)
            print("B. ", optionB)
            print("C. ", optionC)
            choose = str(input("Choose A, B, or C: "))

            #This option A and B will end the adventure with a True statement
            if choose == "A":
                print("This is going to be one good burger")
                return True

            elif choose == "B":
                print("This is going to be one good burger")
                return True

            #This option C will end the adventure with a False statement
            elif choose == "C":
                print("Well that's just a gross burger")
                return False

            #This else will return the output to be option A
            else:
                print("Invalid option, returning to A")
                print("This is going to be one good burger")
                return True


        #This option C will end the adventure with a True statement 
        elif choose == "C":
            print("This is going to be a good burger")
            return True

        #This else will return the adventure with a False statement
        else:
            print("Invalid option, returning to A")
            print("This will be a gross burger")
            return False

    #This else will return the adventure with a False statement
    else:
        print("Invalid option, returning to A")

        #This option A will bring you to the second question 
        text = "Do you want american cheese, pepperjack cheese, or cheddar cheese? "
        optionA = "American cheese"
        optionB = "Pepperjack cheese"
        optionC = "Cheddar cheese"
        print(text) 
        print("A. ", optionA)
        print("B. ", optionB)
        print("C. ", optionC)
        choose = str(input("Choose A, B, or C: "))

        #This option A will end the adventure with a True statement
        if choose == "A":
            print("Ayy that's a good burger")
            return True

        #This option B will bring you to the fourth question
        elif choose == "B":
            text = "Do you want it toasted, grilled, or cooked? "
            optionA = "Toasted"
            optionB = "Grilled"
            optionC = "Cooked"
            print(text) 
            print("A. ", optionA)
            print("B. ", optionB)
            print("C. ", optionC)
            choose = str(input("Choose A, B, or C: "))

            #This option A and B will end the adventure with a True statement
            if choose == "A":
                print("This is going to be one good burger")
                return True

            elif choose == "B":
                print("This is going to be one good burger")
                return True

            #This option C will end the adventure with a False statement
            elif choose == "C":
                print("Well that's just a gross burger")
                return False

            #This else will return the output to be option A
            else:
                print("Invalid option, returning to A")
                print("This is going to be one good burger")
                return True

        #This option C will bring you to the third question
        elif choose == "C":
            text = "Do you want turkey, bacon, or ham? "
            optionA = "Turkey"
            optionB = "Bacon"
            optionC = "Ham"
            print(text) 
            print("A. ", optionA)
            print("B. ", optionB)
            print("C. ", optionC)
            choose = str(input("Choose A, B, or C: "))

            #This option A will be False and will end the adventure here
            if choose == "A":
                print("Gross! Turkey will make it taste bad.")
                return False

            #This option B will bring you to fourth question 
            elif choose == "B":
                text = "Do you want it toasted, grilled, or cooked? "
                optionA = "Toasted"
                optionB = "Grilled"
                optionC = "Cooked"
                print(text) 
                print("A. ", optionA)
                print("B. ", optionB)
                print("C. ", optionC)
                choose = str(input("Choose A, B, or C: "))

                #This option A and B will end the adventure with a True statement
                if choose == "A":
                    print("This is going to be one good burger")
                    return True

                elif choose == "B":
                    print("This is going to be one good burger")
                    return True

                #This option C will end the adventure with a False statement
                elif choose == "C":
                    print("Well that's just a gross burger")
                    return False

                #This else will return the output to be option A
                else:
                    print("Invalid option, returning to A")
                    print("This is going to be one good burger")
                    return True


            #This option C will end the adventure with a True statement
            elif choose == "C":
                print("Oo ham is a good choice")
                return True

            #This else option will return the output to be option A
            else:
                print("Invalid option, returning to A")
                print("Gross! Turkey will make it taste bad.")
                return False

        #This else option will return the output to be option A   
        else:
            print("Invalid option, returning to A")
            print("Ayy that's a good burger")
            return True
        

