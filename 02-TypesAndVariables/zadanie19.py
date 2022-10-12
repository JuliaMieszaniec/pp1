masa=float(input('Wprowadź swoją wagę w kg : '))
wzrost=float(input('Wprowadź swój wzrost w cm : '))
wzrost=wzrost/100
wzrost=wzrost**2
bmi= masa/wzrost
print(' Twoj index BMI wynosi: ' , bmi)