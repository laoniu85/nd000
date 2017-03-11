import turtle
def draw_flower():
    brad =turtle.Turtle()
    brad.color("yellow")
    brad.speed("fast")
    for i in range(0,36):
        draw_diamond(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(200)
    

def draw_diamond(_t):
    _t.forward(50)
    _t.right(17)
    _t.forward(50)
    _t.right(163)
    _t.forward(50)
    _t.right(17)
    _t.forward(50)
    _t.right(163)


window =  turtle.Screen()
window.bgcolor("red")
    
draw_flower()

