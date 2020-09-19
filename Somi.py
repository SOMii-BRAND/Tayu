#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To XP-TRICKER
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Cloning.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'God by Frends '
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:love_hacker
##### LOGO #####
logo = """
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;95m██╔════╝██╔══██╗████╗░████║██║
\033[1;92m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;92m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;95m«-----------------\033[1;91mSOMI BRAND\033[1;95m-----------------»"""
logo2 = """
\033[1;92m▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇▇▇\033[1;91▇▇▇▇▇┈┈┈┈╱▔▔▔▔╲┈┈┈┈▇▇
\033[1;92m▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇ U\033[1;91m T▇▇┈┈┈▕▕╲┊┊╱▏▏┈┈┈▇▇
\033[1;92m▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇ S\033[1;91m R▇▇┈┈┈▕▕▂╱╲▂▏▏┈┈┈▇▇
\033[1;92m▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇ A\033[1;91m   I ▇▇┈┈┈┈╲┊┊┊┊╱┈┈┈┈▇▇
\033[1;92m▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇ A\033[1;91m C▇▇┈┈┈┈▕╲▂▂╱▏┈┈┈┈▇▇
\033[1;92m▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇ M\033[1;91m K ▇▇╱▔▔▔▔┊┊┊┊▔▔▔▔╲▇▇
\033[1;92m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇ A  033[1;91m E▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;92m▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇▇▇\033[1;91m▇▇▇▇▇┈┈┈┈┈┈┈┈┈┈┈┈┈┈▇▇
\033[1;93m▇▇Facebook ▇▇\033[1;93m     ▇▇  Mr SOMI▇▇
\033[1;95m«-----------------\033[1;91mSOMI BRAND\033[1;95m-----------------»"""
logo3 = """
\033[1;93m•¤ 　 　*　 ✭
　 ✭ 
　 * ★ 　 　　 ✰
¤ 　 　*　 ✭
▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒
▒▒▒▒▒████████████▒▒
▒▒▒██████████████▒▒
▒▒█▒██▒███████████▒
▒█▒██▒▒▒███████████
█▒██▒▒██▒███████████
▒███▒▒█▓▒▒█████▓▓████
███▒▒▒█▓▓▒▒███▒▒█▓▒███
█▒▒▒▒▒▒▒▒▒▒▓██████▒████
███████████▓██████████
██████████████████████
████░▓▓▒▓██████████▓██
████░▒▓░▓█████▓▓██▓▓██
████░▒▓░▒█████░░▓░░▓██
████░▒▓░▓█████▒░█▒░███
██████████████░░▓░░▓██
████▒░▒█░░████░░▓▒████
█████▓██▓▓█▓███▓██▓▓██
\033[1;95m«-----------------\033[1;91mSOMI BRAND\033[1;95m-----------------»"""

jalan("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("\033[1;93m▇▇\033[1;95m           WellCome to SOMI BRAND     \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;91m             👇Tool Using Tips👇      \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;92m            Tool Update EveryDay      \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;92m        Termux Data Clear EveryDay    \033[1;93m▇▇")
jalan("\033[1;93m▇▇\033[1;92m         Facebook Id -- SO MI    \033[1;93m▇▇")
jalan("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
print "\033[1;95m«-----------------\033[1;91mSOMI BRAND\033[1;95m-----------------»"
CorrectUsername = "SOMI"
CorrectPassword = "AWAN"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCbzezk06TnsxdInKclBlDcw')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCbzezk06TnsxdInKclBlDcw')
        ##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
        print "\033[1;95m«-----------------\033[1;91mDisclaimer\033[1;95m---------------»"
        time.sleep(0.05)
        print "\033[1;43m       \033[1;34mThis Tool is for Educational Purpose   \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mThis presentation is for educational          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mpurposes ONLY.How you use this information    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mis your responsibility.I will not be          \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mheld accountable This Tool/Channel Doesn't    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mSupport illegal activities.for any illegal    \033[1;0m"
        time.sleep(0.05)
        print "\033[1;45m\033[1;34mActivitie This Tool is for Educational Purpose\033[1;0m"
        time.sleep(0.05)
        print "\033[1;95m«-----------------\033[1;91mSOMI TRICKER\033[1;95m---------------»"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;96m Fast Cloning\033[1;92m[New Update]"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91m Exit             "
	pilih_login()
	
     def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
		blackmafiax()
	elif peak =="2":
		login1()
        elif peak =="3":
	        tokenz()
        elif peak =="4":
        
