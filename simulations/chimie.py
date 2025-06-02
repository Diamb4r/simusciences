import tkinter as tk

def populate_chimie_tab(frame):
    label = tk.Label(frame, text="Simulation : Réaction acide-base (neutralisation)")
    label.pack(pady=10)

    description = "Lorsqu'un acide réagit avec une base, un sel et de l'eau se forment.\n\nExemple : HCl + NaOH → NaCl + H2O"
    desc_label = tk.Label(frame, text=description, justify="left")
    desc_label.pack(padx=20, pady=10)
