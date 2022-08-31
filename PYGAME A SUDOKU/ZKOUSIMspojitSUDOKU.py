import rich
from rich import print
 

prezdivka = input("Zadej přezdívku: ")
while True:
    try:
        rozmer  = int(input("Ahoj, vlož prosím základní rozměr: "))
        if rozmer <= 1:
            print("Ale neee, je to sice číselná hodnota, ale jako sudoku to nemá smysl. Zkus to znovu!")
        else:
            break
    except ValueError:
        print("Ale neee, musíš zadat číselnou hodnotu! Zkus to znovu:)")


print("\n")

print("Rozměr tabulky je:", rozmer, "x", rozmer,", tudíž budeš dopňovat číslice 1 -",(rozmer*rozmer), ".")

print("\n")

from rich.progress import track
from time import sleep


def process_data():
    sleep(0.03)


for _ in track(range(100), description='[yellow]NAČÍTÁNÍ HRY'):
    process_data()

print("\n")

import time
pocatecni_cas = time.localtime()


"""vzor sudoku"""
def vzor(a,b):
    return (rozmer*(a%rozmer)+a//rozmer+b)%(rozmer*rozmer)

"""náhodný generátor správného sudoku"""
from random import sample
def generator(c):
    return sample(c,len(c)) 
rBase = range(rozmer) 
radky = [g*rozmer + a for g in generator(rBase) for a in generator(rBase)] 
sloupce = [g*rozmer + b for g in generator(rBase) for b in generator(rBase)]
cisla  = generator(range(1,rozmer*rozmer+1))

tabulka_sudoku = [[cisla[vzor(r,c)] for c in sloupce] for r in radky]


"""odstranění některých číslic"""
ctverce = (rozmer*rozmer) * (rozmer*rozmer)
prazdne = ctverce * 3//4
for p in sample(range(ctverce),prazdne):
    tabulka_sudoku[p//(rozmer*rozmer)][p%(rozmer*rozmer)] = 0


numSize = len(str(rozmer*rozmer))

"""hezčí tabulka"""
def tabulka(hrana):
    return hrana[0]+ hrana[5:9].join([hrana[1:5]*(rozmer-1)]*rozmer)+hrana[9:13]
vrchni_hrana = tabulka("╔═══╤═══╦═══╗")
ciselna_hrana  = tabulka("║ . │ . ║ . ║")
predelova_hrana = tabulka("╟───┼───╫───╢")
vyrazna_predelova_hrana = tabulka("╠═══╪═══╬═══╣")
spodni_hrana = tabulka("╚═══╧═══╩═══╝")

symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums   = [ [""]+[symbol[n] for n in row] for row in tabulka_sudoku]
print(vrchni_hrana)
for r in range(1,(rozmer*rozmer)+1):
    print( "".join(n+s for n,s in zip(nums[r-1],ciselna_hrana.split("."))) )
    print([predelova_hrana,vyrazna_predelova_hrana,spodni_hrana][(r%(rozmer*rozmer)==0)+(r%rozmer==0)])



print("\n")


import rich

from rich.progress import track
from time import sleep


def process_data():
    sleep(0.05)

for _ in track(range(100), description='[yellow]Tvůj časový limit (zatím je to jen pokus, takže je zkrácený):'):
    process_data()

konecny_cas = time.localtime()
pocatecni_cas = time.strftime("%I:%M:%S %p", pocatecni_cas)
konecny_cas = time.strftime("%I:%M:%S %p", konecny_cas)

print("\n")

from rich.console import Console
from rich.table import Table

table = Table(title="VYHODNOCENÍ")

table.add_column("DÉLKA STRANY", style="magenta")
table.add_column("HRÁČ", style="cyan", no_wrap=True)
table.add_column("POČÁTEČNÍ ČAS", style="magenta")
table.add_column("KONEČNÝ ČAS", justify="right", style="green")

table.add_row((str(rozmer*rozmer)), prezdivka, pocatecni_cas, konecny_cas)


console = Console()
console.print(table)
