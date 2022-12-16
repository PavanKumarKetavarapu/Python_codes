T=int(input("enter the air temparature °C: "))
V=int(input("enter the wind speed in kmph: "))
WCI=13.12+(0.6215*T)-(11.37*(V**0.16))+(0.3965*T*(V**0.16))
print("from the given inputs the 'Wind Chill Index' is",WCI)