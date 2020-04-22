#!/usr/bin/python
import time

counter = 0

while True:
    f1=open("content.txt","r")
    f2=open("contentaux.txt","r")
    for line1 in f1:
        for line2 in f2:
            if line1==line2:
                print("SAME")
            else:
                print("NOT SAME")
            break
    counter += 1
    print(50*'=')
    print('Run number: {}'.format(counter))
    print(50*'=')
    time.sleep(1)
    f1.close()
    f2.close()