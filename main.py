import colorama
from colorama import Fore
from follow_bot import spotify
import threading, os, time

os.system('cls')
print(Fore.BLACK)
os.system('cls')
lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
def logo_():

    print(Fore.LIGHTBLACK_EX + '''
                                 ██▒   █▓ ██▓  ██████  █    ██  ▄▄▄       ██▓    
                                ▓██░   █▒▓██▒▒██    ▒  ██  ▓██▒▒████▄    ▓██▒    
                                 ▓██  █▒░▒██▒░ ▓██▄   ▓██  ▒██░▒██  ▀█▄  ▒██░    
                                  ▒██ █░░░██░  ▒   ██▒▓▓█  ░██░░██▄▄▄▄██ ▒██░    
                                   ▒▀█░  ░██░▒██████▒▒▒▒█████▓  ▓█   ▓██▒░██████▒
                                   ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░
                                   ░ ░░   ▒ ░░ ░▒  ░ ░░░▒░ ░ ░   ▒   ▒▒ ░░ ░ ▒  ░
                                     ░░   ▒ ░░  ░  ░   ░░░ ░ ░   ░   ▒     ░ ░   
                                      ░   ░        ░     ░           ░  ░    ░  ░
                                     ░        

                                            https://discord.gg/ZqURQFra7B
    ''')
logo_()
spotify_profile = str(input(Fore.LIGHTBLACK_EX + "                                             Spotify Link or Username: "))
os.system('cls')
logo_()
threads = int(input(Fore.LIGHTBLACK_EX + "                                                     Threads: "))
os.system('cls')
logo_()

def load_proxies():
    if not os.path.exists("proxies.txt"):
        os.system('cls')
        logo_()
        print("                                              File proxies.txt not found")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            os.system('cls')
            logo_()
            print("                                           No proxies loaded in proxies.txt")
            time.sleep(10)
            os._exit(0)

print("                                           [1] -> Proxies  [2] -> Proxyless")
print('')
option = int(input("                                                       Choice: "))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        fl = safe_print("Followed {}".format(counter))
    else:
        safe_print(f"Error {error}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: 
            proxy_counter = 0
