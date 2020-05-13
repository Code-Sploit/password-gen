def main():
    import random
    from colorama import Fore as colors
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
        eags = input(str(colors.GREEN+ "[E]asy | [A]dvanced | [G]ood | [S]uper | [Q]uit ? " + colors.RESET))
        if (eags == "E"):
            amount = input(str("How many passwords should be generated? "))
            for i in range(1,int(amount) + 1):
                print( colors.MAGENTA + "Password " + str(i) + ": " + random.choice(wordlist) + random.choice(ciphersl + colors.RESET))
        elif (eags == "A"):
            amount = input(str("How many passwords should be generated? "))
            for i in range(1,int(amount) + 1):
                print( colors.MAGENTA + "Password " + str(i) + ": " + random.choice(wordlist) + random.choice(chl) + random.choice(ciphersl) + colors.RESET)
        elif (eags == "G"):
            amount = input(str("How many passwords should be generated? ") + colors.RESET)
            for i in range(1,int(amount) + 1):
                print( colors.MAGENTA + "Password " + str(i) + ": " + random.choice(ciphersl) + random.choice(wordlist) + random.choice(chl) + random.choice(ciphersl) + colors.RESET)
        elif (eags == "S"):
            amount = input(str("How many passwords should be generated? "))
            for i in range(1,int(amount) + 1):
                print(colors.MAGENTA + "Password " + str(i) + ": " + random.choice(chl) + random.choice(wordlist) + random.choice(chl) + random.choice(ciphersl) + random.choice(wordlist) + random.choice(chl) + colors.RESET)
        elif (eags == "Q"):
            print(colors.RED + "Quitting... ")
            stop = True
        else:
            print(colors.RED + "Illegal option!" + colors.RESET)

main()
