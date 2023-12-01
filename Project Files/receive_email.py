import imaplib
import email

email_sender = "theceresapp@gmail.com"
email_pword = "fxfh hyeo oell jedw"
email_reciever = "adamsprojects412@gmail.com"

imap_url = 'imap.gmail.com' #connect to imap

my_mail = imaplib.IMAP4_SSL(imap_url) #connection with gmail using ssl
my_mail.login(email_sender,email_pword) #log in using our creds
my_mail.select('Inbox') #select the inbox to fetch messages

#--------------- SET FILTERS ---------------
#define key and value for email search

def Ascii_Menu():
    print(" ----------------")
    print("|1. from         |")
    print("|2. subject      |")
    print("|3. body contains|")
    print("|4. no filters?  |")
    print("|                |")
    print(" ---------------")
    userinput = input("\n> ")
    userinput = int(userinput)
    print(f"{userinput} with a type of {type(userinput)}")
    if (userinput == 1):
        ScanEmail('FROM', 'adamsprojects412@gmail.com') #could make this custom but i am lazy
    elif(userinput == 2):
        ScanEmail('subject', 'test subject!')
    elif(userinput == 3):
        ScanEmail('text/plain', 'lets keep looking')
    elif(userinput == 4):
        ScanEmail('all', 'all')
    else:
        print(f"{userinput} is not an applicable option...")
        Ascii_Menu()
    

def ScanEmail(key, value):
    #key = 'FROM'
    #value = 'adamsprojects412@gmail.com'
    _, data = my_mail.search(None, key, value)

    mail_id_list = data[0].split() #search for emails with a specific key
    msgs = []#empty list to capture all the messages

    #iterate through messages and extraact data into the msgs list
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)') #(RFC822) returns whole message
        msgs.append(data)

    #all messages with all details
    #extract the text we want

    MessageContents = []
    for msg in msgs[::-1]:
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg = email.message_from_bytes((response_part[1])) #message contents are in bytes. my_msg is an object
                f = open("Most_Recent_Email_Search.txt", "w")
                #print("--------------------------------------------")
                f.write(str(my_msg))
                #print("subj:", my_msg['subject'])
                MessageContents.append(my_msg['subject'])
                #print("from:", my_msg['from'])
                MessageContents.append(my_msg['from'])
                print("body: ")
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/plain':
                        #print(part.get_payload())
                        MessageContents.append(part.get_payload())
                return MessageContents



