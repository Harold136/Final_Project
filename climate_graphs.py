import tkinter as tk
from tkinter import ttk

temperature_options = ["Celsius", "Kelvin", "Fahrenheit"]

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

def main():
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("980x120")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=12)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Value:").grid(row=0, column=0, padx=(0, 8), sticky="w")
    value_entry = ttk.Entry(frame, width=12)
    value_entry.insert(0, "100")
    value_entry.grid(row=0, column=1, padx=(0, 14), sticky="w")

    ttk.Label(frame, text="From:").grid(row=0, column=2, padx=(0, 6), sticky="w")
    from_var = tk.StringVar(value="Celsius")
    from_menu = ttk.OptionMenu(frame, from_var, from_var.get(), *temperature_options)
    from_menu.grid(row=0, column=3, padx=(0, 14), sticky="w")

    ttk.Label(frame, text="To:").grid(row=0, column=4, padx=(0, 6), sticky="w")
    to_var = tk.StringVar(value="Kelvin")
    to_menu = ttk.OptionMenu(frame, to_var, to_var.get(), *temperature_options)
    to_menu.grid(row=0, column=5, padx=(0, 14), sticky="w")

    convert_button = ttk.Button(
        frame,
        text="Convert",
        command=lambda: result_label.config(
            text=f"Result: {round(convert_temperature(float(value_entry.get()), from_var.get(), to_var.get()), 2)} {to_var.get()}"
        ),
    )
    convert_button.grid(row=0, column=6, sticky="w")

    result_label = tk.Label(frame, text="Result will appear here", bg="#eef7ff", relief="flat", anchor="w")
    result_label.grid(row=1, column=0, columnspan=7, sticky="ew", pady=(10, 0))

    root.mainloop()


if __name__ == "__main__":
    main()