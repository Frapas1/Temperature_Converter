import tkinter as tk
from temp_converter import TempConverter

class UI:
    def __init__(self):
        """
        Initialiazer for UI class
        """
        self.window = tk.Tk()
        self.temp_converter = TempConverter()
        self.window.title("Temperature Converter")
        self.frame_entry = tk.Frame(master=self.window)
        self.ent_temperature = tk.Entry(master=self.frame_entry, width=10)
        # self.ent_temperature.insert(0, "5.00")
        self.lbl_temp = tk.Label(master=self.frame_entry, text="\N{DEGREE FAHRENHEIT}")
        self.btn_convert = tk.Button(master=self.window, text="\N{RIGHTWARDS BLACK ARROW}", )
        self.btn_switch = tk.Button(master=self.window, text="Switch Conversion",)
        self.lbl_result = tk.Label(master=self.window, text="\N{DEGREE CELSIUS}")

        # Ensuring Temperature is positioned to the right and label to the left on the grid.
        self.ent_temperature.grid(row=0, column=0, sticky="e")
        self.lbl_temp.grid(row=0, column=1, sticky="w")

        # Positioning the Frame, Button and Label on the grid
        self.frame_entry.grid(row=0, column=0)
        self.btn_convert.grid(row=0, column=1)
        self.lbl_result.grid(row=0, column=2)
        self.btn_switch.grid(row=1, column=0)

        self.btn_convert.config(command=self.convert_button)
        self.btn_switch.config(command=self.switch_temp_scale)

    def ui_start(self):
        self.window.mainloop()

    def get_current_temperature(self) -> float:
        """
        Returns current temperature
        :return:
        """
        return float(self.ent_temperature.get())


    def convert_button(self):
        """
        Does the calculation
        :return:
        """
        result = self.temp_converter.convert(input=self.get_current_temperature())
        if self.temp_converter.get_current_state() == "F":
            self.lbl_result["text"] = f"{round(result, 3)} \N{DEGREE CELSIUS}"
        else:
            self.lbl_result["text"] = f"{round(result, 2)} \N{DEGREE FAHRENHEIT}"

    def switch_temp_scale(self):
        """
        Switches state of temp
        :return:
        """
        current_state = self.temp_converter.get_current_state()
        self.temp_converter.switch_conversion()
        new_state = self.temp_converter.get_current_state()
        if self.temp_converter.get_current_state() == "F":
            self.lbl_temp["text"] = "\N{DEGREE FAHRENHEIT}"
            self.lbl_result["text"] =  "\N{DEGREE CELSIUS}"
        else:
            self.lbl_temp["text"] = "\N{DEGREE CELSIUS}"
            self.lbl_result["text"] = "\N{DEGREE FAHRENHEIT}"
