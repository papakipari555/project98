def intro():
    fileName=input(" ENTER THE FILE NAME :")
    numberofwords=0
    file=open(fileName,'r')
    for line in file:
        words= line.split()
        numberofwords=numberofwords+len(words)
        
    print("number of words are :", numberofwords)

intro()    