import os
from lib.scan import *
from lib.dos import *

c = "\033[38;5;117m"
g = "\033[38;5;118m"
r = "\033[0m"
    
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{c}
▓█████ ██▒   █▓ ██▓ ██▓     ▄▄▄▄    ██▓     █    ██ ▓█████ 
▓█   ▀▓██░   █▒▓██▒▓██▒    ▓█████▄ ▓██▒     ██  ▓██▒▓█   ▀ 
▒███   ▓██  █▒░▒██▒▒██░    ▒██▒ ▄██▒██░    ▓██  ▒██░▒███   
▒▓█  ▄  ▒██ █░░░██░▒██░    ▒██░█▀  ▒██░    ▓▓█  ░██░▒▓█  ▄ 
░▒████▒  ▒▀█░  ░██░░██████▒░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▒
░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░▓  ░░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░
 ░ ░  ░  ░ ░░   ▒ ░░ ░ ▒  ░▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░
   ░       ░░   ▒ ░  ░ ░    ░    ░   ░ ░    ░░░ ░ ░    ░   
   ░  ░     ░   ░      ░  ░ ░          ░  ░   ░        ░  ░
           ░                     ░                         
{r}
    [{c}01{r}] {c}|{r} Bluetooth scan
    [{c}02{r}] {c}|{r} Bluetooth dos
    [{c}03{r}] {c}|{r} Exit

""")


def main():
    while True:
        banner()
        select = input(f"""
╔═══[{c}root{r}@{c}EvilBlue{r}]
╚══{c}>{r} """)
                                        
        if select == "1":
            scan()

        elif select == "2":
            DOS()
             


if __name__ == "__main__":
    main()


