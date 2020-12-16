#Program to find out the total marks recieved in a subject and its Percentage

subjects=["Science","Social","Maths","English","Hindi","Sanskrit"]
marks=[0,0,0,0,0,0]
totalmarks=0
i=0

choice=input ('NEW!! Now calclate the entire marks of the exam. Warning. No Decimals will work. Please type in Integers. If an error occurs, stop the execution and try again.  Are you interested in this, or do you want subject-by-subject calculation? Please type YES or NO.')

choice=choice.upper()
if choice=="YES":
    print("OK")
    for subject in subjects:
        marks[i]=int(input('Enter the marks recieved for {0}.'.format(subject)))
        totalmarks+=marks[i]
        i+=1

    possiblemarks=int(input('Enter the total marks for the exams.'))
    percentagemarks=(totalmarks/possiblemarks)*100
    print("Total Marks obtained is {0}, percentage is {1}".format(totalmarks, percentagemarks))
    
