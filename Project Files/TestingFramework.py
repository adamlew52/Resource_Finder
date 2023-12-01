import os
import random
import pandas as pd
import receive_email as RE


#f = open("positive_words.txt", "r")
target = "\\topics"

def GenerateFileData(dataNum, testFileQuantity):
    topicsdir = "topics"
    print(f"finding {dataNum} different resources for {testFileQuantity} files...")
    f = open("positive_words.txt", "r")
    noOfLines = len(f.readlines())
    fileCount = 1
    wordCount = 0

    #creating files for the number requested, then getting the number of random test words requested 
    while (fileCount < (testFileQuantity+1)):
        print(fileCount)
        FileGen(fileCount)
        wordCount = 0
        while (wordCount < dataNum):
            cwd = os.getcwd()
            wordlist = CreateTestWordList(dataNum, noOfLines)
            FileTitle = str(cwd)+ target +"\ResourceList"+str(fileCount)+".txt"
            print(f"\t{wordCount}")
            g = open(FileTitle, "w")
            for word in wordlist:
                g.write(word)
            wordCount+=1

        fileCount+=1

    MakeMisleadingItem()

def CreateTestWordList(goalamount, noOfLines):
    testwordlist = []
    wordsinlist = 0
    while wordsinlist < goalamount:
        testwordlist.append(pickrandwords(noOfLines))
        wordsinlist +=1
    return testwordlist

def pickrandwords(noOfLines):
    randNum = random.randint(1, int(noOfLines)-1) #random line number from our test-word txt
    #print(randNum)
    randomWord = f.readline(randNum) #use the random line number to get the word from that number
    #print(GetSpecLine(randNum))
    #testWords.append(randomWord)
    return GetSpecLine(randNum)

def GetSpecLine(line):
    f=open("positive_words.txt", "r")
    lines=f.readlines()
    try:
        word = lines[line]
        return word
    except:
        print("-------------------------- random number out of range, skip --------------------------")
        pass

def MakeMisleadingItem():
    cwd = os.getcwd()
    FileGen("_Misleading_File")
    FileTitle = str(cwd)+ target +"\ResourceList"+"_Misleading_File"+".txt"
    j = open(FileTitle, "w")
    j.write("this is misleading data and if you see this you done messed up boy...------------------------------------------------")             

def FileGen(number):
    cwd = os.getcwd()
    #FileTitle = "C:\Users\house\OneDrive\Desktop\Resource_Finder\Project Files\\topics"+"\TestFile"+str(number)+".txt"
    FileTitle = str(cwd)+ target +"\ResourceList"+str(number)+".txt"
    g = open(FileTitle,"w")
    g.close
    return FileTitle

dataNum = 5
testFileQuantity = 5
#GenerateFileData(dataNum, testFileQuantity) #5 words, on 5 documents