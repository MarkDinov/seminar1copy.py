# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
x, y = float(input()), float(input())
if x > 0:
    if y > 0:
        print("1 четверть")
    else:
        print("4 четверть")
else:
    if y > 0:
        print("2 четверть")
    else:
        print("3 четверть")