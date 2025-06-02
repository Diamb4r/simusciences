import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def populate_physique_tab(frame):
    label = tk.Label(frame, text="Simulation : Loi d'Ohm (U = R * I)")
    label.pack(pady=10)

    fig = Figure(figsize=(5, 3), dpi=100)
    ax = fig.add_subplot(111)
    resistances = [1, 2, 3, 4, 5]
    intensites = [i for i in range(1, 6)]
    tensions = [r * i for r, i in zip(resistances, intensites)]
    ax.plot(intensites, tensions, marker='o')
    ax.set_title("Tension en fonction de l'intensité")
    ax.set_xlabel("Intensité (A)")
    ax.set_ylabel("Tension (V)")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
