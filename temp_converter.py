

class TempConverter:
    def __init__(self):
        self.state = "F"

    # Conversion switch button
    def switch_conversion(self):
        """
        This method does a toggle of state. Default state for State is F
        """
        if self.state == "F":
            self.state = "C"
        elif self.state == "C":
            self.state = "F"

    def get_current_state(self):
        """
        This method returns the current State
        :return:
        """
        return self.state

    def convert(self, input: float) -> float:
        """
        This method converts from Farenheit to Celcius or Celcius to Farenheit
        :param input: Floating value for temperature
        :return: Converted temperature
        """
        if self.state == "F":
            # Convert the value from Fahrenheit to Celsius
            result = (5 / 9) * (float(input) - 32)
        else:
            # Convert the value from Celsius to Fahrenheit
            result = ((9 / 5) * (float(input)) + 32)
        return result
