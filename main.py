import colorgram
import turtle as t
import random

#extracting photo colors
rgb_col = []
colors = colorgram.extract('col.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_col.append(new_color)
    
print(rgb_col)

# col = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)

for dot_c in range(1,100+1):
    tim.dot(20,random.choice(rgb_col))
    tim.fd(40)
    if dot_c % 10 == 0:
        tim.setheading(90)
        tim.fd(40)
        tim.setheading(180)
        tim.fd(400)
        tim.setheading(0)
    
    

sc = t.Screen()
sc.exitonclick()