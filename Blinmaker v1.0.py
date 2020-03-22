import time
print("Hello There!")
time.sleep(1)
print("Blinmaker is starting up...")
comradeCakeUnlocked = 0
firstLoop = 1
time.sleep(3)
print("")
print("")
print("CAPITACHA v.2")
time.sleep(1)
a = input("Enter your name to proceed: ") ## a simpliest capitacha

if firstLoop == 1:
    if a == "vadim":
            print("CAPITACHA FAILED")
            time.sleep(1)
            print("Because")
            time.sleep(1)
            print("Vadim blyat")
            exit()
    elif a == "Vadim":
            print("CAPITACHA FAILED")
            time.sleep(1)
            print("Because")
            time.sleep(1)
            print("Vadim blyat")
            exit()
    elif a == "artyom":
            print("Well done Comerade Cat!")
            comradeCakeUnlocked = 1
    elif a == "unlock.comradeCake" and firstLoop == 1:
            firstLoop = 0
            print("Unlocked: Comrade Cat's Ultimate Cake")
            comradeCakeUnlocked = 1
            a = input("Enter your name to proceed: ")
            if a == "vadim":
                print("CAPITACHA FAILED")
                time.sleep(1)
                print("Because")
                time.sleep(1)
                print("Vadim blyat")
                exit()
            elif a == "Vadim":
                print("CAPITACHA FAILED")
                time.sleep(1)
                print("Because")
                time.sleep(1)
                print("Vadim blyat")
                exit()
            elif a == "artyom":
                print("Well done Comerade Cat!")
                comradeCakeUnlocked = 1
            else:
                print("Capitacha completed")
    else:
            print("Capitacha completed")
else:
    if a == "vadim":
            print("CAPITACHA FAILED")
            time.sleep(1)
            print("Because")
            time.sleep(1)
            print("Vadim blyat")
            exit()
    elif a == "Vadim":
            print("CAPITACHA FAILED")
            time.sleep(1)
            print("Because")
            time.sleep(1)
            print("Vadim blyat")
            exit()
    elif a == "artyom":
            print("Well done Comerade Cat!")
            comradeCakeUnlocked = 1
    else:
            print("Capitacha completed")
print("")
time.sleep(1)
print("What do you want to make today?")
print("")
time.sleep(1)
print("gopnik cake")
print("")
time.sleep(1)
print("gopnik cookies")
print("")
time.sleep(1)
print("semechki chalva")
print("")
time.sleep(1)
if comradeCakeUnlocked == 1:
        print("Comrade cat's Ultimate cake")
        print("")
        time.sleep(1)

print("Please select from listed above!")
a = input("")

if a == "gopnik cake":
        print("Good choice!")
        print("")
        time.sleep(2)
        print("How many supplies do you have?")
        flour = int(input("How many grams of flour do you have? : "))
        milk = int(input("How many liters of milk do you have? : "))
        eggs = int(input("How many eggs do you have? : "))
        gopniks = int(input("How many gopniks to help do you have? : "))

        if flour >= 1500 and milk >= 2 and eggs >= 6 and gopniks >= 1:
                print("There will be a good cake today! :D")
        elif flour >= 1500 and milk >= 2 and eggs >= 6 and gopniks == 69:
                        print("How there is that much gopniks in one place..")
        else:
                print("There will be no cake today! :c ")
elif a == "gopnik cookies":
        print("Good choice!")
        print("")
        time.sleep(2)
        print("How many supplies do you have?")
        flour = int(input("How many grams of flour do you have? : "))
        milk = int(input("How many liters of milk do you have? : "))
        eggs = int(input("How many eggs do you have? : "))
        gopniks = int(input("How many gopniks to help do you have? : "))

        if flour >= 1500 and milk >= 2 and eggs >= 6 and gopniks >= 1:
                print("There will be a good cake today! :D")
        elif flour >= 1500 and milk >= 2 and eggs >= 6 and gopniks == 69:
                        print("How there is that much gopniks in one place..?")
        else:
                print("There will be no cake today! :c ")
elif a == "semechki chalva":
        print("Good choice")
        print("")
        time.sleep(2)
        print("How many supplies do you have?")
        time.sleep(1)
        print("")
        semechki = int(input("How many grams of semechki do you have?"))
        time.sleep(1)
        print("")
        gopniks = int(input("How many gopniks do you have?"))
        time.sleep(1)
        if semechki >= 150 and semechki <= 999 and gopniks >= 2:
            print("There will be a good Semechki chalva today :)")
        elif semechki >= 1000 and gopniks >=2
            print("So... Anatoli again got drunk in Belarus?")
            print("No problem! There will be more chalva than usual!")
elif a == "Comrade Cat's Ultimate Cake":
        print("Unbelivable!")
        print("How you done that?")
        time.sleep(1)
        print("")
        print("How many supplies do you have?")
        time.sleep(1)
        print("")
        flour = int(input("How much grams of flour do you have? (needed 17500)"))
        time.sleep(1)
        print("")
        milk = int(input("How many liters of milk do you have? (needed: 20)"))
        time.sleep(1)
        print("")
        eggs = int(input("How many eggs do you have? (needed: 200)"))
        time.sleep(1)
        print("")
        gopniks = int(input("How many gopniks do you have? (needed: 1337)"))

if flour >= 17500 and milk >= 20 and eggs >= 200 and gopniks >= 1337:
    print("ok")


else:
        print(" I said from listed above debil!")
        exit()

print("")
time.sleep(2)
print("Thanks for using Blinmaker")
time.sleep(2)
print("Blinmaker is shutting down...")
time.sleep(2)
