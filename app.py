#!/usr/bin/python
import time
import sys
import requests
import os

def sendText(botMessage):
    botToken = '1173827382:AAGd13RVAbBRcVWNpcXAZHni-uEc7rdAS6E'
    botChatId = '842357098' #meu id
    #botChatId = '-300263333' #group id
    sendTxt = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatId + '&parse_mode=Markdown&text=' + botMessage
    response = requests.get(sendTxt)

    return response.json()

def latestFile(file1,file2):
    infoFile1 = os.stat(file1)[9] # [9] acesses the st_mtime from the object
    infoFile2 = os.stat(file2)[9] # which is the timestamp for file modification
    if infoFile1 > infoFile2: #higher means most recently modified
        return lines1[0]
    else:
        return lines2[0]

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

counter = 0
while True:
    print(50*'=')
    print('Run number: {}'.format(counter))
    print(50*'=')
    f1= open("content.txt","r")
    f2= open("contentaux.txt","r")
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    sendNotification = False

    try:
        if lines1[0]==lines2[0]:
            print("Nenhuma mudança por aqui!")
        else:
            sendNotification = True
            print("[+] Text Sent!!")
            print("content.txt: {}".format(lines1[0]))
            print("contentaux.txt: {}".format(lines2[0]))
    except:
        print("Oopsie! Probably writing file...")
            

    if sendNotification == True:
        sendText('Olha só, o seguinte chamado foi aberto agora! \n {}'.format(latestFile('content.txt','contentaux.txt')))   

    counter += 1
    for i in progressbar(range(10), "Waiting: ", 13):
        time.sleep(1) # any calculation you need
    f1.close()
    f2.close()

