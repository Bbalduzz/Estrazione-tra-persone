from __future__ import print_function
import datetime
import atexit
from os import path
from json import dumps, loads
from rich.console import Console
from rich import print
import subprocess, platform
import numpy as np
from prettytable import PrettyTable
 
# puliamo la shell
if platform.system()=="Windows":
    subprocess.Popen("cls", shell=True).communicate()
else: #Linux e Mac
    print("\033c", end="")
 
console = Console()
table = PrettyTable()
console.print('''[bold magenta]
 _______   ________  _________  ________  ________  ________  ___  ________  ________   _______      
|\  ___ \ |\   ____\|\___   ___\|   __  \|\   __  \|\_____  \|\  \|\   __  \|\   ___  \|\  ___ \     
\ \   __/|\ \  \___|\|___ \  \_\ \  \|\  \ \  \|\  \||___/  /\ \  \ \  \|\  \ \  \| \  \ \   __/|    
 \ \  \_|/_\ \_____  \   \ \  \ \ \   _  _\ \   __  \   /  / /\ \  \ \  \|\  \ \  \| \  \ \  \_|/__  
  \ \  \_|\ \|____|\  \   \ \  \ \ \  \|  \ \|  \ \  \ /  /_/__\ \  \ \  \|\  \ \  \| \  \ \  \_|\ \ 
   \ \_______\____\_\  \   \ \__\ \ \__\| _\ \|__\ \__\|________\ \__\ \_______\ \__\| \__\ \_______|
    \|_______|\_________\   \|__|  \|__|\|__|\|__|\|__|\|_______|\|__|\|_______|\|__| \|__|\|_______|
             \|_________| 

[/bold magenta]''', justify="center")
 
# ====== SECURITY SESSION =====

# controllo quante volte lo script e' stato lanciato
def read_counter():
    return loads(open("counter.json", "r").read()) + 1 if path.exists("counter.json") else 0
 
def write_counter():
    with open("counter.json", "w") as f:
        f.write(dumps(counter))
 
counter = read_counter()
atexit.register(write_counter)
 
console.print("Estrazione fatta [bold red]{}[/bold red] volta/e".format(counter), justify="center")
 
# stampo la data e ora esatta del lancio dello script
start = datetime.datetime.now()
console.print("=== ",str(start)," ===", justify="center")
 
# ==== ESTRAZIONE SESSION ====

persone = ["persona1", "persona2", "persona3", "persona4", "persona5", "persona6", "personax"]

n = int(console.input('[yellow]Numero di persone da estrarre[/yellow]: '))
try:
    non = [int(x) for x in console.input("[yellow]Numeri da escludere[/yellow]: ").split(",")]
    for numero in non:
        numero = numero-1 
        non = [numero]
except ValueError:
    non = []

numeri = [i for i in list(range(len(persone))) if i not in non]
estratti = np.random.choice(numeri, size=n, replace=False)
for e in estratti:
    p = e+ 1
    console.print('[yellow]>>> Persona estratta: [/yellow]',p)

for nestratto in estratti:
    gruppo = persone[nestratto]
    console.print('[green]:heavy_check_mark:[/green] '+gruppo)
 

# stampo il momento esatto della fine del programma
end = datetime.datetime.now()
console.print("=== [bold red]Estrazione finita[/bold red] ===", justify="center")
console.print(str(end), justify="center")

input('premi un tasto per uscire :-)')
