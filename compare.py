import tkinter as tk

# Initialize the window.
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)
temp_converter = TempConverter()

# Setting up Container for the Labels
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=temp_converter.convert())
btn_switch = tk.Button(master=window, text="Switch Conversion", command=temp_converter.switch_conversion())

# Ensuring Temperature is positioned to the right and label to the left on the grid.
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Positioning the Frame, Button and Label on the grid
frm_entry.grid(row=0, column=0)
btn_convert.grid(row=0, column=1)
lbl_result.grid(row=0, column=2)
btn_switch.grid(row=1, column=0)


class TempConverter(btn_convert, lbl_temp, lbl_result, ent_temperature):
    def __init__(self):
        self.state = "F"

    # Conversion switch button
    def switch_conversion(self):
        if self.state == "F":
            self.state = "C"
            btn_convert.config(command=self.convert)
            lbl_temp.config(text="\N{DEGREE CELSIUS}")
            lbl_result.config(text="\N{DEGREE FAHRENHEIT}")
        else:
            self.state = "F"
            btn_convert.config(command=self.convert)
            lbl_temp.config(text="\N{DEGREE FAHRENHEIT}")
            lbl_result.config(text="\N{DEGREE CELSIUS}")

    def convert(self):

        if self.state == "F":
            # Convert the value from Fahrenheit to Celsius
            celsius = (5 / 9) * (float(ent_temperature.get()) - 32)
            lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
        else:
            # Convert the value from Celsius to Fahrenheit
            fahrenheit = ((9 / 5) * (float(ent_temperature.get()))) + 32
            lbl_result["text"] = f"{round(fahrenheit, 3)} \N{DEGREE FAHRENHEIT}"


window.mainloop()