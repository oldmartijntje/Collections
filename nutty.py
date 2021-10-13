import random
def zakjeMEnMs(kleuren):
    zakMEnMs = list()
    mnmDictionaryBag = {

            'oranje': 0,
            'blauw' : 0,
            'groen' : 0,
            'bruin' : 0
        }
    while True:
        try:
            aantalKeer = int(input("hoeveel M&M's"))
            break
        except:
            print("what about a number?")
    for x in range(0, aantalKeer):
        kleurenNummer = random.randint(0, 3)
        zakMEnMs.append(kleuren[kleurenNummer])
        mnmDictionaryBag[kleuren[kleurenNummer]]+=1
    print(zakMEnMs)                                         
    return mnmDictionaryBag

kleurtjes = ["oranje", "blauw", "groen", "bruin"]
MEnMs = zakjeMEnMs(kleurtjes)
print(MEnMs)