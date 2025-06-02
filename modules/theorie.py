import tkinter as tk

def populate_theory_tab(frame):
    text = """
Notions scientifiques de base :

1. La loi d'Ohm : U = R * I
   - U : tension (volts)
   - R : résistance (ohms)
   - I : intensité (ampères)

2. Réaction acide-base :
   - Un acide libère des ions H+
   - Une base libère des ions OH-
   - H+ + OH- → H2O
"""
    label = tk.Label(frame, text=text, justify="left")
    label.pack(padx=20, pady=10)
