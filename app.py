#!/usr/bin/python
import time, sys, os
import datetime
import requests

def sendText(botMessage):
    botToken = ''
    botChatId = '' #meu id
    #botChatId = '' #group id
    sendTxt = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatId + '&parse_mode=Markdown&text=' + botMessage
    response = requests.get(sendTxt)

    return response.json()

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

def makeDatetime(line):
    splitedWebPage = line[8]
    splitedWebPage = splitedWebPage.split(">")
    splitedWebPage = splitedWebPage[1][0:-4]
    splitedWebPage = splitedWebPage.split(" ")
    splitedWebPage = [splitedWebPage[0].split("-"), splitedWebPage[1].split(":")]
    # datetime(year, month, day, hour, minute, second) 
    year = int(splitedWebPage[0][2])
    month = int(splitedWebPage[0][1])
    day = int(splitedWebPage[0][0])
    hour = int(splitedWebPage[1][0])
    minute = int(splitedWebPage[1][1])    
    return datetime.datetime(year,month,day,hour,minute,0)

def getTime(line1,line2):
    a = makeDatetime(line1)
    b = makeDatetime(line2)
    if a>b:
        return [a,line1]
    elif b>a:
        return [b,line2]

def getTicket():
    mostRecent = getTime(lines1,lines2)[1]
    splitedWebPage = mostRecent[1].split("'")
    return splitedWebPage[3]

def getTitleAndDesc():
    mostRecent = getTime(lines1,lines2)[1]
    splitedWebPage = mostRecent[1].split(">")
    title = splitedWebPage[2][0:-3]
    desc = splitedWebPage[4][0:-5]
    return [title,desc]

def getCategory():
    mostRecent = getTime(lines1,lines2)[1]
    splitedWebPage = mostRecent[5].split("'>")
    category = splitedWebPage[1][0:-6]
    return category

def getTec():
    mostRecent = getTime(lines1,lines2)[1]
    splitedWebPage = mostRecent[3].split("'>")
    tech = splitedWebPage[1][0:-7]
    return tech

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
            datef1 = makeDatetime(line1)
            datef2 = makeDatetime(line2)
            infoFile1 = os.stat('content.txt')[9] # [9] acesses the st_mtime from the object
            infoFile2 = os.stat('contentaux.txt')[9] # which is the timestamp for file modification

            if infoFile1 > infoFile2: #higher means most recently modified
                if a > b: # Se o arquivo content.txt foi editado por ultimo e possui uma data mais recente então, um novo chamado foi aberto
                    sendNotification = True
                    print("[+] Text Sent!!")
                    print("content.txt: {}".format(lines1[0]))
                    print("contentaux.txt: {}".format(lines2[0]))
            elif infoFile2 > infoFile1:
                if b > a: # Se o arquivo contentaux.txt foi editado por ultimo e possui uma data mais recente então, um novo chamado foi aberto
                    sendNotification = True
                    print("[+] Text Sent!!")
                    print("content.txt: {}".format(lines1[0]))
                    print("contentaux.txt: {}".format(lines2[0]))     
    except:
        print("Oopsie! Probably writing file...")
            

    if sendNotification == True:
        ticket = getTicket()
        lastAtt = getTime(lines1,lines2)[0]
        cat = getCategory()
        title  = getTitleAndDesc()[0]
        description = getTitleAndDesc()[1]
        tec = getTec()
        
        sendText('**Atenção!** o {} foi atualizado agora as {} \n\nCategoria: {}\n\nTitulo: {}\n\nDescrição: {}\n\nAtribuído para: {}'.format(ticket, lastAtt, cat, title, description, tec))   

    counter += 1
    for i in progressbar(range(30), "Waiting: ", 30):
        time.sleep(1)

    f1.close()
    f2.close()

