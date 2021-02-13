import tkinter as tk
import webbrowser


#Fenster erstellen und Einrichten
root = tk.Tk()
root.title('Tutorial')
root.minsize(500, 300)

#Defintitionen
def CSGO():
    webbrowser.open('steam://rungameid/730')

#Buttons
csgo = tk.Button(root, text='CSGO', command=CSGO).pack()

#Fenster anzeigen
root.mainloop()