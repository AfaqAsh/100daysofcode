import colorgram
import turtle as t
import random




# def extract_colors(image_name):
#     colors = colorgram.extract(image_name, 20)
#     extracted_colors = []
#     for color in colors:
#         r = color.rgb[0]
#         g = color.rgb[1]
#         b = color.rgb[2]
#         rgb = (r, g, b)
#         extracted_colors.append(rgb)
    
#     return extracted_colors

# # tim.color(colors[0].rgb)
# extracted_colors = extract_colors('120123_r21786_g2048.webp')
# print(extracted_colors)

color_list = [(1, 13, 31), (52, 25, 16), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 83, 39), (215, 87, 64), (157, 7, 24), (164, 162, 32), (157, 63, 103), (11, 63, 32), (207, 74, 104), (97, 6, 20), (11, 97, 58), (0, 63, 145), (173, 135, 162)]

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.shape('circle')
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
print(tim.position())

def draw_row(dots):
    for _ in range(dots):
        tim.color(random.choice(color_list))
        tim.stamp()
        tim.forward(50)


def draw_grid(rows, dots):
    y = -176.78
    for i in range(rows):
        draw_row(dots)
        tim.setx(-176.78)
        y += 50
        tim.sety(y)
        
draw_grid(5, 10)

screen = t.Screen()
screen.exitonclick()