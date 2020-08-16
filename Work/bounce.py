# bounce.py
#
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.
height = 100
bounces = 1
while bounces <= 10:
    bounce = (height * 3 / 5)
    print(bounces, round(bounce, 4)) # round to 4 digits
    height = bounce
    bounces = bounces + 1
