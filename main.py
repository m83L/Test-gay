import time 


#Main program
print(" __       __                       ______                    ")
print("/  \     /  |                     /      \                   ")
print("$$  \   /$$ |  ______   _______  /$$$$$$  |______   __    __ ")
print("$$$  \ /$$$ | /      \ /       \ $$ |_ $$//      \ /  |  /  |")
print("$$$$  /$$$$ |/$$$$$$  |$$$$$$$  |$$   |  /$$$$$$  |$$ |  $$ |")
print("$$ $$ $$/$$ |$$    $$ |$$ |  $$ |$$$$/   $$ |  $$ |$$ |  $$ |")
print("$$ |$$$/ $$ |$$$$$$$$/ $$ |  $$ |$$ |    $$ \__$$ |$$ \__$$ |")
print("$$ | $/  $$ |$$       |$$ |  $$ |$$ |    $$    $$/ $$    $$/")
print("$$/      $$/  $$$$$$$/ $$/   $$/ $$/      $$$$$$/   $$$$$$/")
print("\n")
print("\n")
print("\n")
print("[01] detecteur a homo")
print("[02] Exit")
print("\n")
option=input("[::] choisi l'option: ")

while option != "01" and option != "02" and option != "1" and option != "2":
    print("Option invalide!")
    option=input("[::] 1 ou 2: ")
if option == "01" or option == "1":
    

    print("Combien de pourcent pensais vous avoir ?")
    print("\n")
    option=input("[::] choisi l'option: ")

    print("Le resulat arrive..")
    print("\n")
    print("ce pendant sa peut prendre quelque sec..")
    print("\n")
    option=input("Tu est gay a 100 pourcent Désolé mon reuf...")
else:
    print("Exiting...")
    time.sleep(2)
    quit(0)
