import os
import random
import string
import threading
import time
from queue import Queue
import requests
from colorama import Fore, init
from termcolor import colored

clear = 'clear'
os.system(clear)

print(colored(""" __   __           """, "red"))
print(colored(""" \ \ / /__  _   _  """, "red"))
print(colored("""  \ V / _ \| | | | """, "red"))
print(colored("""   | | (_) | |_| | """, "red"))                                                                                                       print(colored("""   |_|\___/ \__,_| """, "red"))
print(colored("""  _____      _           """, "white"))
print(colored(""" |_   _|   _| |__   ___  """, "white"))
print(colored("""   | || | | | '_ \ / _ \ """, "white"))
print(colored("""   | || |_| | |_) |  __/ """, "white"))
print(colored("""   |_| \__,_|_.__/ \___| """, "white"))
print(colored("""                         """, "white"))
print("[создатель @batyarimskiy1 для @termuxtop]")

def randomName(size=11, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

print(" Введите ID стрима всё что после https://www.youtube.com/watch?v= скопируйте и вставьте")
token = input("[ID] : ")
url= "https://m.youtube.com/watch?v=" + token
url2 = "https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=Syr16u8qwHnPkVqI&docid=" + token + "&ver=2&cmt=2094&ei=1EJtXou2C6eoxN8PpqqNq>
class main(object):
    def __init__(self):
        self.combolist = Queue()
        self.Writeing = Queue()
        self.printing = []
        self.botted = 0
        self.combolen = self.combolist.qsize()

    def printservice(self): #print screen
        while True:                                                                                                                                                
         if True:
                os.system(clear)
                print(Fore.LIGHTMAGENTA_EX + intro + Fore.LIGHTMAGENTA_EX)
                print(Fore.LIGHTMAGENTA_EX + f"Botted:{self.botted}\n")
                for i in range(len(self.printing) - 10, len(self.printing)):
                    try:
                        print("Усешно!")
                    except (ValueError, Exception):
                        print("Не успешно")
                time.sleep(0.5)
a = main()
class proxy():

    def update(self):
        while True:
            data = ''
            urls = ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes","https://www.proxy-list.download/api/v1/get>
            for url in urls:                                                                                                                                           data += requests.get(url).text

            self.splited += data.split("\r\n") #scraping and splitting proxies
            time.sleep(600)

    def get_proxy(self):
        random1 = random.choice(self.splited) #choose a random proxie
        return random1
    def FormatProxy(self):
            proxyOutput = {'https' :'https://'+self.get_proxy()}
            return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)

proxy1 = proxy()
def bot():
    while True:
        try:
            s = requests.session()

            resp = s.get("https://m.youtube.com/watch?v=" + token,headers={'Host': 'm.youtube.com', 'Proxy-Connection': 'keep-alive', 'User-Agent': 'M>
            url = resp.text.split(r'videostatsWatchtimeUrl\":{\"baseUrl\":\"')[1].split(r'\"}')[0].replace(r"\\u0026",r"&").replace('%2C',",").replace>
            cl = url.split("cl=")[1].split("&")[0] #parsing some infos for the URL
            ei = url.split("ei=")[1].split("&")[0]
            of = url.split("of=")[1].split("&")[0]
            vm = url.split("vm=")[1].split("&")[0]
            s.get("https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=isWmmj2C9Y2vULKF&docid=" + token + "&ver=2&cmt=7334&ei=" + ei + ">


            a.botted += 1
        except Exception as E:
            pass


time.sleep(7)
print("Сколько потоков? Рекомендую для хорошей работы 500")
maxthreads = int(input("[+] : "))
threading.Thread(target=a.printservice).start()
num = 0
while num < maxthreads :
    num += 1
    threading.Thread(target=bot).start()


threading.Thread(target=bot).start()
