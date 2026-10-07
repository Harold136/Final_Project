import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import sqlalchemy as sa
from random import randint
temperature_options = ["Celsius", "Kelvin", "Fahrenheit"]

class simulator():
    def create_sim(self, parent):
        self = ttk.Frame(parent)
        
        self.fig = plt.figure(figsize=(9,6))
        ax = self.fig.subplot_mosaic([["slevel", "slevel"],
                          ["magnitude", "CO2"],
                          ["phase", "angle"]])
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().grid(row=8,column=7)
        
    def update_sim():
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
    biodiversty_affection = [1,4,65,67,7,8,98,9]
    ice_melting = [12,1,4,5,6,7]
    
    def create_graph(self, parent):
        control = ttk.Frame(parent)
        control.pack(side=tk.TOP, fill="x", padx = 10, pady = 10)
        
        
        ttk.Label(control, text="Sea Level:").grid(row=0, column=0, padx=(0, 8), sticky="w")
        self.sea_level_entry = ttk.Entry(control, width=12)
        self.sea_level_entry.insert(0, ", ".join(map(str, self.sea_level)))
        self.sea_level_entry.grid(row=0, column=1)

        ttk.Label(control, text="CO2:").grid(row=0, column=2, padx=(0, 8), sticky="w")
        self.co2_entry = ttk.Entry(control, width=12)
        self.co2_entry.insert(0, ", ".join(map(str, self.co2)))
        self.co2_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(control, text="Biodiversty :").grid(row=1, column=2, padx=(0, 8), sticky="w")
        self.biodiversty = ttk.Entry(control, width=12)
        self.biodiversty.insert(0, ", ".join(map(str, self.biodiversty_affection)))
        self.biodiversty.grid(row=1, column=3, padx=5, pady=5)
        
        ttk.Label(control, text="Ice melting :").grid(row=1, column=0, padx=(0, 8), sticky="w")
        self.ice = ttk.Entry(control, width=12)
        self.ice.insert(0, ", ".join(map(str, self.ice_melting)))
        self.ice.grid(row=1, column=1, padx=5, pady=5)

        plot_button = ttk.Button(control, text="Plot Graph", command=self.update_plot)
        plot_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.fig = plt.figure(figsize=(9,6), layout='constrained', dpi=100)
        ax = self.fig.subplot_mosaic([["slevel", "slevel"],
                          ["magnitude", "CO2"],
                          ["phase", "angle"]])

        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.update_plot()

    def update_plot(self):
        try:
            sea_level = list(map(float, self.sea_level_entry.get().split(",")))
            co2 = list(map(float, self.co2_entry.get().split(",")))
            biodiversty = list(map(float, self.biodiversty.get().split(",")))
            ice_melting = list(map(float, self.ice.get().split(",")))
        except ValueError:
            return

        self.fig.clear()
        axes = self.fig.subplot_mosaic([["slevel", "slevel"],
                            ["magnitude", "CO2"],
                            ["phase", "angle"]])

        axes["slevel"].plot(sea_level, color="blue", marker="o")
        axes["slevel"].set_title("Global Sea Level Rise")
        axes["slevel"].set_ylabel("Sea_level")
        axes["slevel"].grid(True)
        axes["slevel"].set_xlabel("Over Years")
        
        axes["CO2"].plot(co2, color="red", marker="^")
        axes["CO2"].set_title("Atmospheric CO2 (ppm)")
        axes["CO2"].set_ylabel("ppm")
        axes["CO2"].grid(True)
        axes["CO2"].set_xlabel("Over Years")
        
        axes["phase"].plot(ice_melting, color="teal", marker="^")
        axes["phase"].set_title("Biodiversty ")
        axes["phase"].set_ylabel("degrading life")
        axes["phase"].grid(True)
        axes["phase"].set_xlabel("Over Years")
        
        
        axes["angle"].plot(biodiversty, color="green", marker="^")
        axes["angle"].set_title("Ice Melting")
        axes["angle"].set_ylabel("Per inch")
        axes["angle"].grid(True)
        axes["angle"].set_xlabel("Over Years")
        
        axes["magnitude"].plot(co2, color="green", marker="^")
        axes["magnitude"].set_title("Atmospheric CO2 (ppm)")
        axes["magnitude"].set_ylabel("idk")
        axes["magnitude"].grid(True)

        self.canvas.draw()
   
class Data:
    def __init__(self):
        self.log_widget = None
        self.engine = sa.create_engine('sqlite:///climate_data.db')
        self.connection = self.engine.connect()
        self.table_name = 'climate_data'
        
       
            
        self.connection.execute(sa.text(f'''
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    log_type TEXT NOT NULL,
                    details TEXT NOT NULL,
                    sea_level REAL,
                    co2 REAL,
                    biodiversity REAL,
                    ice_melting REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            '''))
        
        self.connection.commit()
        
    def export_data(self, data):
        data.to_sql(self.table_name, self.connection, if_exists='replace', index=False)
        data.to_csv('climate_data.csv', index=False)

        try:
            self.connection.execute(sa.text('SELECT * FROM climate_data'))
            print("Data exported successfully.")
        except ValueError as e:
            print(f"Error exporting data: {e}")

    def print_data(self, parent=None):
    
        if parent is not None:
            if self.log_widget is None:
                self.log_widget = tk.Text(parent, wrap=tk.WORD, height=20)
                self.log_widget.pack(fill=tk.BOTH, expand=True)

            self.log_widget.config(state=tk.NORMAL)
            self.log_widget.delete(1.0, tk.END)
            self.log_widget.insert(tk.END, "Climate Data Logs:\n")

            try:
                result = self.connection.execute(sa.text('SELECT * FROM climate_data'))
                rows = result.fetchall()
                print('working here')
                if not rows:
                    self.log_widget.insert(tk.END, "No data found in the database.\n")
                else:
                    for row in rows:
                        self.log_widget.insert("end", f"{row}\n")

            except ValueError as e:
                self.log_widget.insert(tk.END, f"Error retrieving data: {e}\n")
                self.log_widget.config(state=tk.DISABLED)
            return
        
        try:
            result = self.connection.execute(sa.text('SELECT * FROM climate_data'))
            print('working fkjh')
            for row in result:
                print(row)
        except ValueError as e:
            print(f"Error retrieving data: {e}")
        
    def insert_log(self, log_type, details, sea_level=None, co2=None, biodiversity=None, ice_melting=None):
        insert_query = f'''
            INSERT INTO {self.table_name}
                (log_type, details, sea_level, co2, biodiversity, ice_melting)
            VALUES (:log_type, :details, :sea_level, :co2, :biodiversity, :ice_melting)
        '''
        self.connection.execute(
            sa.text(insert_query),
            {
                'log_type': log_type,
                'details': details,
                'sea_level': sea_level,
                'co2': co2,
                'biodiversity': biodiversity,
                'ice_melting': ice_melting,
            },
        )
        self.connection.commit()
        

class Main(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        self.geometry("800x800")
        self.title("Temperature Converter")
        self.configure(bg = 'grey')
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both')

        frame1 = ttk.Frame(notebook, width=900, height=600)
        frame2 = ttk.Frame(notebook, width=900, height=600)
        frame3 = ttk.Frame(notebook, width=900, height=600)
        
        
        notebook.add(frame1, text="Conversions and Simulator")
        notebook.add(frame2, text="Climate Graphs")
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
        data = Data()
        def log_it():
            value = value_entry.get()
            from_unit = from_var.get()
            to_unit = to_var.get()

            try:
                value = float(value_entry.get())
                converted_value = round(convert_temperature(value, from_var.get(), to_var.get()), 2)
                print('working')
            except ValueError:
                result_label.config(text="Invalid input. Please enter a numeric value.")
                data.insert_log(
                    'conversion',
                    f"from={from_unit}, to={to_unit}, value={value_entry.get()}, status=invalid",
                    sea_level=None,
                    co2=None,
                    biodiversity=None,
                    ice_melting=None,
                )
                return

            result_label.config(text=f"Result: {round(converted_value, 2)} {to_var.get()}")
            data.insert_log(
                'conversion',
                f"from={from_unit}, to={to_unit}, value={value}, status=success",
                sea_level=value,
                co2=value,
                biodiversity=value,
                ice_melting=converted_value,
            )
        
        
        convert_button = ttk.Button(frame1, text="Convert", command=log_it)
        convert_button.grid(row=0, column=6, sticky="w")
        data.print_data(frame3)
        
       

       
        simulators = simulator()
        simulators.create_sim(frame1)
        graph = climate_change_graphs()
        graph.create_graph(frame2)
        
if __name__ == "__main__":
    app = Main()
    app.mainloop()
   