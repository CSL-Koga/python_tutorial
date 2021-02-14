from time import sleep
import pyautogui

#Wichtige Variablen
counter = 0

#Datengewinnung
print("Welches Wort soll Gespammt werden?")
word = input("")
print("Wie oft soll das Wort Gespammt werden?")
zahlnoInt = input()
zahl = int(zahlnoInt)
zahl -= 1

#Warten
sleep(5)

#Spambot
while counter <= zahl:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    if counter >= zahl:
        print("Fertig!")
        break
    counter += 1
