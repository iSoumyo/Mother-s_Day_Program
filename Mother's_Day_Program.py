import os
import turtle
import random
screen = turtle.Screen()
turtle.title('Happy Mothers Day')
screen.setup(width=1090,height=700)
screen.bgcolor('black')
screen.tracer(0)
os.startfile('Mom.mp3') #You can change this song
tt = turtle.Turtle()
tt.hideturtle()
colors_pen = ['green', 'white', 'blue', 'yellow', 'pink', 'purple', 'violet', 'gray']
colors_fill = ['green', 'white', 'blue', 'yellow', 'pink', 'purple', 'violet', 'gray']
tt.speed('fastest')
def gg():
    for i in range(30): 
        x,y = random.randrange(-350,350),random.randrange(-230,230)
        tt1 = turtle.Turtle() 
        tt1.color(random.choice(colors_pen))
        tt1.write('Happy Mothers Day MOM',font=('chiller',90,'italic bold'),align='center')
        tt1.clear()
        tt.penup()
        tt.goto(x,y)
        tt.pendown()
        tt.begin_fill()
        tt.color(random.choice(colors_pen))
        for i in range(6):
            tt.forward(40)
            tt.right(144)
        tt.end_fill()    
while True:
    gg()
    tt.clear()
turtle.mainloop()        
