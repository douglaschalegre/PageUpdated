#!/usr/bin/python
import time
import requests

def sendText(botMessage):
    botToken = ''
    botChatId = ''
    sendTxt = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatId + '&parse_mode=Markdown&text=' + botMessage
    response = requests.get(sendTxt)

    return response.json()

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
        sendText('Ei! Algo mudou... Fica de olho!')   

    counter += 1
    time.sleep(10)
    f1.close()
    f2.close()

