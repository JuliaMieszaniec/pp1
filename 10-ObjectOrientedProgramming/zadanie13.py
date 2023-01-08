class TV:
    def __init__(self):
        self.is_on=False
        self.channel=1

    def set_channels(self, channels_list) :
        self.channels_list=channels_list
        
    def show_channels(self):
        print(self.channels_list)

    
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        self.volume=0
        if self.is_on == True:
            print(f'TV is on, channel {self.channel} {self.channels_list[self.channel]}')
        else:
            print('Tv is off')
    def set_channel(self, num):
        self.channel=num
    
    def show_volume(self):       
         print(self.volume)

    def increase_volume(self):
        if self.volume < 10:
            self.volume+=1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume-=1



telewizor=TV()
telewizor.show_status()
telewizor.turn_on()
telewizor.set_channel(5)
telewizor.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
telewizor.show_channels()
telewizor.show_volume()
telewizor.increase_volume()
telewizor.show_volume()