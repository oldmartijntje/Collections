import random
def zakjeMEnMs(kleuren):
    zakMEnMs = list()
    while True:
        try:
            aantalKeer = int(input("hoeveel M&M's"))
            break
        except:
            print("what about a number?")
    for x in range(0,aantalKeer):
        kleurenNummer = random.randint(0, 3)
        zakMEnMs.append(kleuren[kleurenNummer])
    return zakMEnMs

kleurtjes = ["oranje","blauw","groen","bruin"]
MEnMs = zakjeMEnMs(kleurtjes)
print(MEnMs)