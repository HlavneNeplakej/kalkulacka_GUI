import tkinter as tk
from kalkulacka import KalkulackaModel
from kalkulacka_view import KalkukackaView
from kalkulacka_controller import KalkulackaController

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(pady=15, padx=15)
    root.title("Calculator")

model = KalkulackaModel()
view = KalkukackaView(root, None)
controller = KalkulackaController(model, view)
view.controller = controller

root.mainloop()

