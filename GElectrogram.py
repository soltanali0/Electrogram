import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

k = 8.99 * 10**9  # Coulomb's constant

def electric_field(q, r, x, y):

    r_squared = r**2
    e_x = (k * q * x) / r_squared
    e_y = (k * q * y) / r_squared
    return e_x, e_y

def plot_electric_field(charges):

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    
    for charge in charges:
        q, qx, qy = charge
        r = np.sqrt((X - qx)**2 + (Y - qy)**2)
        e_x, e_y = electric_field(q, r, X - qx, Y - qy)
        Ex += e_x
        Ey += e_y
    
    plt.figure()
    plt.streamplot(X, Y, Ex, Ey, density=2, arrowsize=2, color='blue')  
    
    for charge in charges:
        q, qx, qy = charge
        plt.scatter(qx, qy, color='red' if q < 0 else 'blue')  
        if q > 0:
            plt.text(qx, qy, f"+{q}", verticalalignment='bottom', horizontalalignment='right', color='blue')
        else:
            plt.text(qx, qy, f"{q}", verticalalignment='top', horizontalalignment='right', color='red')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Electric Field')
    plt.show()

def add_field():
    global fields
    fields += 1
    
    label = tk.Label(root, text=f"Charge {fields}:", font=("Helvetica", 12))
    label.grid(row=fields+3, column=0, sticky="w")
    
    charge_entry = tk.Entry(root, font=("Helvetica", 12))
    charge_entry.grid(row=fields+3, column=1, padx=5)
    
    x_label = tk.Label(root, text="X Position:", font=("Helvetica", 12))
    x_label.grid(row=fields+3, column=2)
    
    x_entry = tk.Entry(root, font=("Helvetica", 12))
    x_entry.grid(row=fields+3, column=3, padx=5)
    
    y_label = tk.Label(root, text="Y Position:", font=("Helvetica", 12))
    y_label.grid(row=fields+3, column=4)
    
    y_entry = tk.Entry(root, font=("Helvetica", 12))
    y_entry.grid(row=fields+3, column=5, padx=5)
    
    entry_widgets.append((label, charge_entry, x_entry, y_entry))

def remove_field():
    global fields
    if fields > 0:
        label, charge_entry, x_entry, y_entry = entry_widgets.pop()
        label.destroy()
        charge_entry.destroy()
        x_entry.destroy()
        y_entry.destroy()
        fields -= 1

        # Shift fields up to fill the gap
        for i in range(fields+1, len(entry_widgets)+1):
            label, charge_entry, x_entry, y_entry = entry_widgets[i-1]
            label.grid(row=i+2, sticky="w")
            charge_entry.grid(row=i+2, column=1, padx=5)
            x_entry.grid(row=i+2, column=3, padx=5)
            y_entry.grid(row=i+2, column=5, padx=5)

def on_submit():
    charges = []
    for entry in entry_widgets:
        charge = entry[1].get()
        x = entry[2].get()
        y = entry[3].get()
        if charge and x and y:
            try:
                charge = float(charge)
                x = float(x)
                y = float(y)
                charges.append((charge, x, y))
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values for charge and position.")
                return
    plot_electric_field(charges)

root = tk.Tk()
root.title("Electric Field Visualization")

fields = 0
entry_widgets = []

root.grid_rowconfigure(3, weight=20)
root.grid_columnconfigure(0, weight=20)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))

add_button = ttk.Button(root, text="Add Field", command=add_field)
add_button.grid(row=1, column=0)

remove_button = ttk.Button(root, text="Remove Field", command=remove_field)
remove_button.grid(row=1, column=1)

submit_button = ttk.Button(root, text="Plot Electric Field", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
