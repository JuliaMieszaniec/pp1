class Temperature():
    def __init__(self):
        import random
        self.temp=random.triangular(34.0, 42.0)
        self.temperature=round(self.temp, 1)
        self.is_on=False

    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False

    def show_temperature(self):
        if self.is_on == True:
            if self.temperature >=37:
                print(f"{self.temperature} (fever)")
            elif self.temperature>=41:
                print(f"{self.temperature} (CRITICAL TEMPERATURE!!)")
            else:
                print(self.temperature)
        else:
            print("Termometr is off")

temp=Temperature()
temp.show_temperature()
temp.turn_on()
temp.show_temperature()
temp.turn_off