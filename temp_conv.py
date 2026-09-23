
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
    sea_level = [1,2,3,4,5,6,7,7,8,9,9,1,91]
    co2 = [380,385,390,395,400,405,410,415,420,425]

    
    
    def create_graph(self, parent):
        control = ttk.Frame(parent)
        control.pack(side=tk.TOP, fill="x", padx = 10, pady = 10)


        ttk.Label(control, text="Seak Level (mm):").grid(row=0, column=0, padx=(0, 8), sticky="w")
        self.sea_level_entry = ttk.Entry(control, width=12)
        self.sea_level_entry.insert(0, ", ".join(map(str, self.sea_level)))
        self.sea_level_entry.grid(row=0, column=1)

        ttk.Label(control, text="CO2 (ppm):").grid(row=1, column=0, padx=(0, 8), sticky="w")
        self.co2_entry = ttk.Entry(control, width=12)
        self.co2_entry.insert(0, ", ".join(map(str, self.co2)))
        self.co2_entry.grid(row=1, column=1, padx=5, pady=5)

        plot_button = ttk.Button(control, text="Plot Graph", command=self.update_plot)
        plot_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.fig = plt.figure(figsize=(9,6), layout='constrained', dpi=100)
        ax = self.fig.subplot_mosaic([["signal", "signal"],
                          ["magnitude", "log_magnitude"],
                          ["phase", "angle"]])

        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.update_plot()

    def update_plot(self):
        try:
            sea_level = list(map(float, self.sea_level_entry.get().split(",")))
            co2 = list(map(float, self.co2_entry.get().split(",")))
        except ValueError:
            return

        self.fig.clear()
        axes = self.fig.subplot_mosaic([["signal", "signal"],
                            ["magnitude", "log_magnitude"],
                            ["phase", "angle"]])

        axes["signal"].plot(sea_level, color="blue", marker="o")
        axes["signal"].set_title("Global Sea Level Rise")
        axes["signal"].set_ylabel("mm")
        axes["signal"].grid(True)

        axes["log_magnitude"].plot(co2, color="green", marker="^")
        axes["log_magnitude"].set_title("Atmospheric CO2 (ppm)")
        axes["log_magnitude"].set_ylabel("ppm")
        axes["log_magnitude"].grid(True)


        self.canvas.draw()
   
       

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
        graph.create_graph(frame2)
        
        
        
       

        
   

if __name__ == "__main__":
    app = Main()
    app.mainloop()
   