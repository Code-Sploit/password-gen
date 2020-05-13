def main():
    import random
    with open("lib/dictionary.txt","r") as words:
        wordlist = list()
        for i in words.readlines():
            current = i.strip()
            wordlist.append(current)
    with open("lib/ciphers.txt","r") as ciphers:
        ciphersl = list()
        for i in ciphers.readlines():
            current = i.strip()
            ciphersl.append(current)
    with open("lib/charactars.txt","r") as ch:
        chl = list()
        for i in ch.readlines():
            current = i.strip()
            chl.append(current)
    stop = False
    while stop == False:
        eags = input(str("[E]asy | [A]dvanced | [G]ood | [S]uper | [Q]uit ? "))
        if (eags == "E"):
            amount = input(str("How many passwords should be generated? "))
            for i in range(1,int(amount) + 1):
                print("Password " + str(i) + ": " + random.choice(wordlist) + random.choice(ciphersl))
        elif (eags == "A"):
            amount = input(str("How many passwords should be generated? "))
            for i in range(1,int(amount) + 1):
                print("Password " + str(i) + ": " + random.choice(wordlist) + random.choice(chl)) + random.choice(ciphersl)
        elif (eags == "G"):
            amount = input(str("How many passwords should be generated? "))
            for i in range(1,int(amount) + 1):
                print("Password " + str(i) + ": " + random.choice(ciphersl) + random.choice(wordlist) + random.choice(chl) + random.choice(ciphersl))
        elif (eags == "S"):
            amount = input(str("How many passwords should be generated? "))
            for i in range(1,int(amount) + 1):
                print("Password " + str(i) + ": " + random.choice(chl) + random.choice(wordlist) + random.choice(chl) + random.choice(ciphersl) + random.choice(wordlist) + random.choice(chl))
        elif (eags == "Q"):
            print("Quitting... ")
            stop = True
        else:
            print("Illegal option!")

main()
