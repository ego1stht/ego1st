#!/usr/bin/emv python
# -*- coding:utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet nmap islemleri")

print("""
\33[31m
1-) hızlı tarama(1)
2-) servis ve versiyon bilgisi
3-) işletim sistemi bilgisi
4-) geniş tarama(2)
5-) normal tarama(3)
6-) açık port bulma
7-) hızlı port tarama

""")

islemnumarasi = raw_input("işlem gir: ")

if(islemnumarasi == "1"):
                    hedefip = raw_input("hedef IP numarası girin: ")
                    os.system("nmap " + hedefip)

elif(islemnumarasi == "2"):
                      hedefip = raw_input("hedef IP numarası girin: ")
                      os.system("nmap -sS -sV " + hedefip)

elif(islemnumarasi == "3"):
                      hedefip = raw_input("hedef IP numarası girin: ")
                      os.system("nmap -O " + hedefip)

elif(islemnumarasi == "4"):
		      hedefip = raw_input("hedef IP numarası girin: ")
                      os.system("nmap -v " + hedefip)

elif(islemnumarasi == "5"):
		      hedefip = raw_input("hedef IP numarası girin: ")
                      os.system("nmap -vv " + hedefip)

elif(islemnumarasi == "6"):
                      hedefip = raw_input("hedef IP numarası girin: ")
                      os.system("nmap -sT " + hedefip)

elif(islemnumarasi == "7"):
                    hedefip = raw_input("hedef IP numarası girin: ")
                    os.system("nmap -F " + hedefip)


else:
    print("""
girilen değer yanlış.
""")


print("\33[36myeniden işlem yapmak ister misiniz?")

sec = raw_input("Y/N: ")

if(sec == "Y"):
	os.system("python NMAP\ İşlemleri.py")

else:
	print("program kapanıyor.")
