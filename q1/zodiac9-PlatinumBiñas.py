year = int(input("Enter your birth year: "))
if year < 1900:
    raise ValueError("Invalid year, it should not be earlier than 1900.")
zodiac = year % 12
if zodiac == 0:
    print("Your Chinese zodiac sign is: Monkey (猴 / Hóu)")
elif zodiac == 1:
    print("Your Chinese zodiac sign is: Rooster (鸡 / Jī)")
elif zodiac == 2:
    print("Your Chinese zodiac sign is: Dog (狗 / Gǒu)")
elif zodiac == 3:
    print("Your Chinese zodiac sign is: Pig (猪 / Zhū)")
elif zodiac == 4:
    print("Your Chinese zodiac sign is: Rat (鼠 / Shǔ)")
elif zodiac == 5: 
    print("Your Chinese zodiac sign is: Ox (牛 / Niú)")
elif zodiac == 6:
    print("Your Chinese zodiac sign is: Tiger (虎 / Hǔ)")
elif zodiac == 7:
    print("Your Chinese zodiac sign is: Rabbit (兔 / Tù)")
elif zodiac == 8:
    print("Your Chinese zodiac sign is: Dragon (龙 / Lóng)")
elif zodiac == 9:
    print("Your Chinese zodiac sign is: Snake (蛇 / Shé)")
elif zodiac == 10:
    print("Your Chinese zodiac sign is: Horse (马 / Mǎ)")
elif zodiac == 11:
    print("Your Chinese zodiac sign is: Goat (羊 / Yáng)")

    
