from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
temperature_options = ["Celsius", "Kelvin", "Fahrenheit"]

class simulator():
    pass

    
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        celsius_value = value
    elif from_unit == "Kelvin":
        celsius_value = value - 273.15
    elif from_unit == "Fahrenheit":
        celsius_value = (value - 32) * 5/9

    if to_unit == "Celsius":
        return celsius_value
    elif to_unit == "Kelvin":
        return celsius_value + 273.15
    elif to_unit == "Fahrenheit":
        return (celsius_value * 9/5) + 32

   
    


class climate_change_graphs:
   def create_graph(self, parent, x_data, y_data, title, x_label, y_label):
        fig = plt.Figure(figsize=(9, 6), dpi=100)
        ax = fig.add_subplot(111)
        
        x_data = [1,2,3]
        y_data = [1,4,9]
        ax.plot(x_data, y_data)
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        return canvas
    
       

class Data(tk.Tk):
    pass


class Main(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.title("Temperature Converter")
        self.configure(bg = 'grey')
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both')

        frame1 = ttk.Frame(notebook, width=900, height=600)
        frame2 = ttk.Frame(notebook, width=900, height=600)
        frame3 = ttk.Frame(notebook, width=900, height=600)
        notebook.add(frame1, text="Conversions and Simulator")
        notebook.add(frame2, text="Graphs and climate simulator")
        notebook.add(frame3, text="Sql logs and notes")

        
        
        basic_font = font.Font(family ="Times New Roman", size=12)
        ttk.Label(frame1, text="Value:",font=basic_font).grid(row=0, column=0, padx=(0, 8), sticky="w")
        value_entry = ttk.Entry(frame1, width=12)
        value_entry.insert(0, "100")
        value_entry.grid(row=0, column=1, padx=(0, 14), sticky="w")

        ttk.Label(frame1, text="From:", font=basic_font).grid(row=0, column=2, padx=(0, 6), sticky="w")
        from_var = tk.StringVar(value="Celsius")
        from_menu = ttk.OptionMenu(frame1, from_var, from_var.get(), *temperature_options)
        from_menu.grid(row=0, column=3, padx=(0, 14), sticky="w")

        ttk.Label(frame1, text="To:", font=basic_font).grid(row=0, column=4, padx=(0, 6), sticky="w")
        to_var = tk.StringVar(value="Kelvin")
        to_menu = ttk.OptionMenu(frame1, to_var, to_var.get(), *temperature_options)
        to_menu.grid(row=0, column=5, padx=(0, 14), sticky="w")
        
        convert_button = ttk.Button(frame1,text="Convert", command=lambda: result_label.config(text=f"Result: {round(convert_temperature(float(value_entry.get()), from_var.get(), to_var.get()), 2)} {to_var.get()}"))
        convert_button.grid(row=0, column=6, sticky="w")
        
        result_label = tk.Label(frame1, text="Result will appear here", bg="#eef7ff", relief="flat", anchor="w")
        result_label.grid(row=1, column=0, columnspan=7, sticky="ew", pady=(10, 0))
        
        graph = climate_change_graphs()
        graph.create_graph(frame2, [], [], "Climate Change Graph", "X-axis", "Y-axis")
        
        
        
       

        
   

if __name__ == "__main__":
    app = Main()
    app.mainloop()
   