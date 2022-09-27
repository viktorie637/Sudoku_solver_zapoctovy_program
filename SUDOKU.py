#Zápočtový program, Viktorie Pavelková

from rich.console import Console
from rich.progress import track
from time import sleep

#emojis
EMOJI = {"grinning_face_with_big_eyes": "😃", "smiling_face_with_smiling_eyes": "😊","thumbs_up": "👍","point_down": "👇","wave": "👋"}

console = Console()

print("\n")

console.print("Ahoj", EMOJI["wave"], style = "bold")

while True:
    try:
        console.print("Vlož prosím základní rozměr: ", style= "bold")
        rozmer  = int(input())
        if (rozmer <= 1):
            print("Ale neee, je to sice číselná hodnota, ale jako sudoku to nemá smysl. Zkus to znovu!", EMOJI["grinning_face_with_big_eyes"])
        elif (rozmer >= 7):
            print("Taková velikost sudoku je až příliš! Zkus zadat menší rozměr znovu.", EMOJI["grinning_face_with_big_eyes"])
        else:
            break
    except ValueError:
        print("Ale neee, musíš zadat číselnou hodnotu! Zkus to znovu:)")

print("\n")

console.print("Rozměr tabulky je:",rozmer, "x", rozmer," tudíž se doplňují číslice 1 -",(rozmer*rozmer), ".", EMOJI["point_down"])

print("\n")

def process_data():
    sleep(0.02)


for _ in track(range(100), description='[yellow]GENEROVÁNÍ SUDOKU'):
    process_data()

print("\n")



"""vzor sudoku"""
def vzor(a,b):
    return (rozmer*(a%rozmer)+a//rozmer+b)%(rozmer*rozmer)

"""náhodný generátor správného sudoku"""
from random import sample
def generator(c):
    return sample(c,len(c)) 
zakladni_rozmer = range(rozmer) 
radky = [g*rozmer + a for g in generator(zakladni_rozmer) for a in generator(zakladni_rozmer)] 
sloupce = [g*rozmer + b for g in generator(zakladni_rozmer) for b in generator(zakladni_rozmer)]
cisla  = generator(range(1,rozmer*rozmer+1))

tabulka_sudoku = [[cisla[vzor(r,c)] for c in sloupce] for r in radky]
ciselne_rozmer_tabulky = len(str(rozmer*rozmer))

"""hezčí tabulka"""
def tabulka(hrana):
    return hrana[0]+ hrana[5:9].join([hrana[1:5]*(rozmer-1)]*rozmer)+hrana[9:13]
vrchni_hrana = tabulka("╔═══╤═══╦═══╗")
ciselna_hrana  = tabulka("║ . │ . ║ . ║")
predelova_hrana = tabulka("╟───┼───╫───╢")
vyrazna_predelova_hrana = tabulka("╠═══╪═══╬═══╣")
spodni_hrana = tabulka("╚═══╧═══╩═══╝")

symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cisla = [[""]+[symbol[i] for i in radky] for radky in tabulka_sudoku]
print(vrchni_hrana)
for r in range(1,(rozmer*rozmer)+1):
    print("".join(n+s for n,s in zip(cisla[r-1],ciselna_hrana.split("."))))
    print([predelova_hrana,vyrazna_predelova_hrana,spodni_hrana][(r%(rozmer*rozmer)==0)+(r%rozmer==0)])

print("\n")



"""sudoku určité náročnosti na doplnění"""
while True:
    console.print("Nyní si vyber požadovanou obtížnost [italic][not bold](lehká / střední / těžká)[not italic][bold]: ", style = "bold")
    obtiznost  = input()
    if (obtiznost == "lehká") or (obtiznost == "střední") or (obtiznost == "těžká"):
        print("Nu dobře, nyní pojďme vygenerovat tvoje sudoku na doplnění téhle obtížnosti.", EMOJI["smiling_face_with_smiling_eyes"])
        break
    else:
        print("Ale neee, musíš zadat jednu z možností (lehká / střední / těžká)! Zkus to znovu:)")

print("\n")

def process_data():
    sleep(0.02)

for _ in track(range(100), description='[yellow]GENEROVÁNÍ SUDOKU DLE OBTÍŽNOSTI'):
    process_data()

print("\n")

"""odstranění některých číslic"""
if (obtiznost == "lehká"):
    ctverce = (rozmer*rozmer) * (rozmer*rozmer)
    prazdne = ctverce * 50//100
    for p in sample(range(ctverce),prazdne):
        tabulka_sudoku[p//(rozmer*rozmer)][p%(rozmer*rozmer)] = 0
elif (obtiznost == "střední"):
    ctverce = (rozmer*rozmer) * (rozmer*rozmer)
    prazdne = ctverce * 62//100
    for p in sample(range(ctverce),prazdne):
        tabulka_sudoku[p//(rozmer*rozmer)][p%(rozmer*rozmer)] = 0
else:
    ctverce = (rozmer*rozmer) * (rozmer*rozmer)
    prazdne = ctverce * 72//100
    for p in sample(range(ctverce),prazdne):
        tabulka_sudoku[p//(rozmer*rozmer)][p%(rozmer*rozmer)] = 0

cisla  = [[""]+[symbol[o] for o in radky] for radky in tabulka_sudoku]
print(vrchni_hrana)
for p in range(1,(rozmer*rozmer)+1):
    print( "".join(q+r for q,r in zip(cisla[p-1],ciselna_hrana.split("."))) )
    print([predelova_hrana,vyrazna_predelova_hrana,spodni_hrana][(p%(rozmer*rozmer)==0)+(p%rozmer==0)])

print("\n")
