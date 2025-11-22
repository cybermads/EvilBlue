import subprocess

c = "\033[38;5;117m"
r = "\033[0m"

def scan():
    subprocess.run("hcitool scan", shell=True) 
    input(f"[{c}+{r}] Finish{c}...{r}")
