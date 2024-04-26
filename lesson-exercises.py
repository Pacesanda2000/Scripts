def prva_uloha():
    cisla = [10, 20, 30, 40, 50, 60, 70, 80]
    cisla[2:5] = reversed(cisla[2:5])
    print(cisla)

def druha_uloha():
    cisla = [10, 20, 30, 40, 50, 60, 70, 80]
    print("Máme dostupný zoznam:", cisla)
    start = int(input("Zadaj začiatočný index: "))
    end = int(input("Zadaj koncový index: "))
    cisla[start:end+1] = reversed(cisla[start:end+1])
    print("Výsledok (po reverse):", cisla)

def tretia_uloha():
    farby1 = ['Red', 'Green', 'Blue']
    farby2 = ['Red', 'Blue', 'Yellow', 'Black']
    spolocneFarby = [farba for farba in farby1 if farba in farby2]
    print("Spoločné prvky uvedených zoznamov:", spolocneFarby)

def stvrta_uloha():
    pismena = ['a', 'b', 'c', 'd', 'e', 'f']
    cisla = [1, 2, 3, 4, 5]
    slovnik = {pismena[I]: cisla[I] for I in range(len(cisla))}
    print(slovnik)

def piata_uloha():
    a = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
    b = [1, 2, 2, 1]
    c = [1, 3, 1]
    d = [1, 3, 2, 1]
    zoznam = [a, b, c, d]
    seq = []
    for I in zoznam:
        if I == I[::-1]:
            seq.append("True")
        else:
            seq.append("False")
    for Y in range(len(seq)):
        print(f"Zoznam/sekvencia {zoznam[Y]} je palindrom: {seq[Y]}")

def siesta_uloha():
    slovnik = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
    najmensiKluc = min(slovnik, key=slovnik.get)
    najvacsiaHodnota = max(slovnik.values())
    najvacsiKluc = max(slovnik, key=slovnik.get)
    print(f"Najmensiu hodnotu/cislo obsahuje kluc: {najmensiKluc}")
    print(f"Najvacsiu hodnotu/cislo obsahuje kluc: {najvacsiKluc}")

def siedma_uloha():
    povodnySlovnik = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
    pocetHodnot = {}
    for hodnota in povodnySlovnik.values():
        if hodnota in pocetHodnot:
            pocetHodnot[hodnota] += 1
        else:
            pocetHodnot[hodnota] = 1
    print("Pocet prvkov pre danu hodnotu:", pocetHodnot)

def osma_uloha():
    ntice = [
        (1, 2, 3, 4),
        (3, 5, 2, 1),
        (2, 2, 3, 1)
    ]

    vysledky = []
    for i in range(len(ntice[0])):
        sucet = 0
        for j in range(len(ntice)):
            sucet += ntice[j][i]
        vysledky.append(sucet)

    return tuple(vysledky)

# testovanie funkcie
print(osma_uloha()) # (6, 9, 8, 6)
