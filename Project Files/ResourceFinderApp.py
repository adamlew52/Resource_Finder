import os
import TestingFramework as TF
import Search as S
import time
import schedule
import receive_email as RE


keywords = ["resourcelist", "resource_list", "resource list","topics"]
target = "\\topics"

def FindResourceList(): #use the 
    cwd = os.getcwd()
    sortedFileList = []
    #print(f"finding resources from current directory [[{cwd}]]")
    FileTitle = str(cwd)+str(target)
    FileList = os.listdir(FileTitle)
    for file in FileList:
        for keyword in keywords:
            if keyword in file.lower() :
                sortedFileList.append(file)
            else:
                pass
    return sortedFileList

def SplitResourceListsinFiles(fileLocation):
    f = open(fileLocation, "r") #opens the file
    count = 0
    lineCount = len(f.readlines())
    
    resourceList = []

    while count < (lineCount + 1):
        f = open(fileLocation, "r")

        # Get next line from file

        #new try
        lines = f.readlines()
        #print(lines[count-1])
        #print(lines[count])
        try:
            resourceList.append(lines[count])
        except:
            print("")
        ##resourceList.append(lines.split(","))
        #print(lines)
        count += 1

    #print(f"final list:\n{resourceList}")
    return resourceList

def SplitTextResourceList(body):
    bodySplit = body.split(",")
    resourceList = []
    for item in bodySplit:
        resourceList.append(item)
    return resourceList 

#START SEARCH/WEBSCRAPE TOOLS
def SearchMaterials(query):
    resource = []
    resultsNum = 1
    resource.append(S.Search(query, resultsNum))
    print(resource)
#END SEARCH/WEBSCRAPE TOOLS

#START EMAIL TOOLS
def Email_In():
    keywords = ["Resources", ]#"ResourceFinder","NeedResources"]
    for keyword in keywords:
        keyword = keyword.lower()
        emailContents = RE.ScanEmail("all", "all")
        emailSender = emailContents[1]
        emailBody = emailContents[2]
    return emailBody, emailSender
#main()

def Email_Out():
    print("This is a placeholder for now, but once we have the resource finder set up we'll use the script in /send_email.py")
#END EMAIL TOOLS

def AutomateSendReceive(emailContents, emailAddress):
    print(f"emailContents: {emailContents}")
    print(f"emailAddress: {emailAddress}")
    Formatting.text(emailContents)
    

class Formatting:
    def text(emailContents): #if the user only sent text in the email, process it here
        emailTopics = SplitTextResourceList(emailContents)
        SearchMaterials(emailContents)


def UnitTest(): #use the appropriate functions here   
    cwd = os.getcwd()

    ResourceList = FindResourceList()
    for resource in ResourceList: #goes through all the resources that meet the criterion (resources are the lists of topics)
        FileTitle = str(cwd)+str(target)+"\\"+str(resource)
        currentItems = SplitResourceListsinFiles(FileTitle)
        print(f"Topic: {resource}\n\t\t-----Resources-----")
        count = 1 
        for item in currentItems:
            print(f"\t{count}. {item}")
            MaterialSearchOutcome = SearchMaterials(item)
            print(f"\t\t{MaterialSearchOutcome}")
            count += 1
        
        #SearchMaterials(item)

emailContents = Email_In()
AutomateSendReceive(emailContents[0], emailContents[1])


#server scheduling 
#schedule.every(1).hours.do()  
#while 1:
#    schedule.run_pending()
#    time.sleep(1)