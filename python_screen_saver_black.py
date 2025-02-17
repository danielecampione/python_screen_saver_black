import tkinter as tk

def exit_screensaver(event=None):
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')

# Nasconde il puntatore del mouse
root.config(cursor='none')

# Posizione iniziale del puntatore
posizione_iniziale = root.winfo_pointerx(), root.winfo_pointery()

def controllo_movimento():
    posizione_attuale = root.winfo_pointerx(), root.winfo_pointery()
    spostamento = ((posizione_attuale[0] - posizione_iniziale[0]) ** 2 + (posizione_attuale[1] - posizione_iniziale[1]) ** 2) ** 0.5
    if spostamento > 5:
        exit_screensaver()
    else:
        root.after(100, controllo_movimento)

# Vincola gli eventi per uscire
root.bind('<Escape>', exit_screensaver)
root.bind('<Button>', exit_screensaver)
root.bind('<Motion>', lambda e: None)  # Previene il blocco del movimento del mouse

controllo_movimento()
root.mainloop()
