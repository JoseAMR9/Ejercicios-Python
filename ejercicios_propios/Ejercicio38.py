weather = int(input("Type the temperature in °C: "))

if weather > 35:
    print("Too hot")
elif 20 < weather < 34:
    print("Fine")
elif 10 < weather < 19:
    print("Cold")
else:
    print("Too cold")
