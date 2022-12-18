class TV:
    def __init__(self):
        self.is_on=False
        self.channel=1

    
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on == True:
            print(f'TV is on, channel {self.channel}')
        else:
            print('Tv is off')
    def set_channel(self, num):
        self.channel=num


    def set_channels(self, channels_list) :
        self.channels_list=channels_list
        
    def show_channels(self):
        print(self.channels_list)

telewizor=TV()
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.set_channel(5)
telewizor.show_status()
telewizor.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
telewizor.show_channels()
