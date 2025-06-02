import tkinter as tk
from tkinter import ttk
from modules import quiz, theorie
from simulations import physique, chimie

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("ÉducScience - Apprendre la physique et la chimie")
        self.master.geometry("800x600")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)

        self.add_theory_tab()
        self.add_quiz_tab()
        self.add_physique_tab()
        self.add_chimie_tab()

    def add_theory_tab(self):
        frame = ttk.Frame(self.notebook)
        theorie.populate_theory_tab(frame)
        self.notebook.add(frame, text="Théorie")

    def add_quiz_tab(self):
        frame = ttk.Frame(self.notebook)
        quiz.populate_quiz_tab(frame)
        self.notebook.add(frame, text="Quiz")

    def add_physique_tab(self):
        frame = ttk.Frame(self.notebook)
        physique.populate_physique_tab(frame)
        self.notebook.add(frame, text="Physique")

    def add_chimie_tab(self):
        frame = ttk.Frame(self.notebook)
        chimie.populate_chimie_tab(frame)
        self.notebook.add(frame, text="Chimie")
