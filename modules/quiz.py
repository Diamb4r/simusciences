import tkinter as tk
from tkinter import messagebox
import random
from database import save_score

questions = [
    {"question": "Quelle est la formule de la vitesse ?", "options": ["v = d / t", "v = m * g", "v = E / t"], "answer": "v = d / t"},
    {"question": "Quel est le pH d'une solution neutre ?", "options": ["7", "0", "14"], "answer": "7"},
]

def populate_quiz_tab(frame):
    current_q = random.choice(questions)
    question_var = tk.StringVar(value=current_q["question"])
    selected_answer = tk.StringVar()

    question_label = tk.Label(frame, textvariable=question_var, wraplength=400)
    question_label.pack(pady=10)

    for option in current_q["options"]:
        tk.Radiobutton(frame, text=option, variable=selected_answer, value=option).pack(anchor="w")

    def submit():
        if selected_answer.get() == current_q["answer"]:
            messagebox.showinfo("Résultat", "Bonne réponse !")
            save_score("quiz", 1)
        else:
            messagebox.showwarning("Résultat", "Mauvaise réponse.")
            save_score("quiz", 0)

    submit_btn = tk.Button(frame, text="Soumettre", command=submit)
    submit_btn.pack(pady=10)
