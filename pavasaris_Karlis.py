#faktoriāls - funkcija aprēķina faktoriālu un atgriež faktoriālu izmantojot parametru ar kuru pasauc funkciju, šai vērtībai katru reizi pieskaita 1 un to reizina ar katru iepriekšējo vērtību
def faktorials(n):
    fakt = 1

    for i in range(1,n+1):
        fakt = fakt * i

    n_faktorials = print (f"skaitļa {n} faktoriāls ir {fakt}")
    return(n_faktorials)

#zvaigznes - šajā funkcijā ievadītā parametra vērtību sareizina ar str"*", iegūstot parametra skaitu ar zvaigznēm un beigās atgriež zvaigznes
def zvaigznes(zvaigznes):
    kop_zvaigznes = print(zvaigznes*"*", end ="")
    return(kop_zvaigznes)

#2 tukšas rindas
def divas_tukšas_rindas():
    tuksas_rindas =print("""
""")
    return(tuksas_rindas)

#funkcija, kas sevī ietver citas funkcijas
def virsraksts():
    print("Faktoriāla aprēķināšana")
    zvaigznes(55)#zvaigznes funkcijai pievieno parametra vērtību 55
    print("")
    izpildit_while = True#while funkcija atkārtojas, kamēr izpildit_while ir True
    while izpildit_while:
        sk = int(input("ievadi veselu pozitīvu skaitli mazāku par 13:"))

        if 0<sk<13:#ievadītajam skaitlim jābūt pozitīvam un mazākam par 13
            faktorials(sk)#izsauc funkciju faktorials ar parametru sk, ko iepriekš ievadīja

        elif sk>=13:
            print("Ievadītais sakitlis ir pārāk liels")
        else:
            pass
        atkartot = input("vai atkārtot?(j/n):").lower()#lietotājs izvēlas atkārtot vai neatkārtot programmu, ja ievada n tad programma beidzas, bet ja ievada j vai jebko citu, tad programma atkārtojas

        if atkartot == "n":
            izpildit_while = False
        divas_tukšas_rindas()
virsraksts()#izsauc galveno funkciju
print("Paldies!")