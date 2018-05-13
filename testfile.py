print ('WELCOME TO THE MULTIPLE CHOICE TEST ON THE PERIOTIC TABLE\n')
name = input('WHAT IS YOUR NAME? ')
print ('\nHI THERE ' + name + '! LET''S PLAY A GAME!\n')
print ('I will ask you 40 questions and give you three choices for each question.\n\nYou select which choice is the correct answer. E.g. A, B or C\n')
print ('Important : Please keep your CAPS LOCK on')
print ('\n-----------------------------------------------------------\n')

keep_going = ""
if keep_going != "":
  print("stop")
else:
  while keep_going == "":

    ###########################################################################
    #                          SET THE SCORE TO ZERO                          #
    ###########################################################################

    score = 0
    score = int(score)  #Convert the 0 into a number so we can add scores


    ###########################################################################
    #                           QUESTION 1                                    #
    ###########################################################################

    print ('QUESTION 1: What is the symbol for Hydrogen?\n')
    print ('A. H')
    print ('B. Y')
    print ('C. G')
    print ('')

    Q1answer = "A"
    Q1response= input('Your answer : ')

    if (Q1response != Q1answer):
        print ('Sorry, that is incorrect!')
    else:
        print ('Well done! ' + Q1response + ' is correct!')
        score = score + 1

    print ('Your current score is ' + str(score) + ' out of 40')
    print ('\n-----------------------------------------------------------\n')

    keep_going = input("press any key to continue or press <enter> to retry: ")

    ###########################################################################
    #                           QUESTION 2                                    #
    ###########################################################################

    print ('QUESTION 2: What is the element for the symbol He ...\n')
    print ('A. Helium')
    print ('B. Neon')
    print ('C. Hydroxide')
    print ('')

    Q2answer = "A"
    Q2response = input('Your answer : ')

    if (Q2response != Q2answer):
      print ('Sorry, that is incorrect!')
    else:
        print ('Well done! ' + Q1response + ' is correct!')
        score = score + 1

    print ('Your current score is ' + str(score) + ' out of 40')
    print ('\n-----------------------------------------------------------\n')

    keep_going = input("press any key to continue or press <enter> to retry: ")

    ###########################################################################
    #                           QUESTION 3                                    #
    ###########################################################################

    print ('QUESTION 2: What is the symbol for Lithium ...\n')
    print ('A. Helium')
    print ('B. Neon')
    print ('C. Hydroxide')
    print ('')

    Q2answer = "A"
    Q2response = input('Your answer : ')

    if (Q2response != Q2answer):
      print ('Sorry, that is incorrect!')
    else:

        print ('Well done! ' + Q1response + ' is correct!')
        score = score + 1

    print ('Your current score is ' + str(score) + ' out of 40')
    print ('\n-----------------------------------------------------------\n')

    keep_going = input("press any key to continue or press <enter> to retry: ")

