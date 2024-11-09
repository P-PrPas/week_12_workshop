import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

class Polygon:
    def __init__(self):
        self.option = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        self.num_sides = 3
        self.size = 1
        self.orientation = 0
        self.location = [0,0]
        self.color = self.get_new_color()
        self.reduction_ratio = 0.618
        self.border_size = 1

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def random_stats(self):
        self.num_sides = random.randint(3, 5)  # triangle, square, or pentagon
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)

    def reposition(self):
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

    def adjust_size(self):
        self.size *= self.reduction_ratio

    def case1(self):
        for i in range(30):
            self.draw_polygon()
            self.reposition()
            self.random_stats()
            self.num_sides = 3
        turtle.done()

    def case2(self):
        for i in range(30):
            self.num_sides = 4
            self.draw_polygon()
            self.reposition()
            self.random_stats()
        turtle.done()

    def case3(self):
        for i in range(30):
            self.num_sides = 5
            self.draw_polygon()
            self.reposition()
            self.random_stats()
        turtle.done()

    def case4(self):
        for i in range(30):
            self.draw_polygon()
            self.reposition()
            self.random_stats()
        turtle.done()

    def case5(self):
        for i in range(30):
            self.num_sides = 3
            for j in range(3):
                self.draw_polygon()
                self.reposition()
                self.adjust_size()
            self.random_stats()
        turtle.done()

    def case6(self):
        for i in range(30):
            self.num_sides = 4
            for j in range(3):
                self.draw_polygon()
                self.reposition()
                self.adjust_size()
            self.random_stats()
        turtle.done()

    def case7(self):
        for i in range(30):
            self.num_sides = 5
            for j in range(3):
                self.draw_polygon()
                self.reposition()
                self.adjust_size()
            self.random_stats()
        turtle.done()

    def case8(self):
        for i in range(30):
            for j in range(3):
                self.draw_polygon()
                self.reposition()
                self.adjust_size()
            self.random_stats()
        turtle.done()

    def case9(self):
        for i in range(24):
            if i in [0, 5, 11, 17, 23]:
                self.draw_polygon()
                self.reposition()
            else:
                for j in range(3):
                    self.draw_polygon()
                    self.reposition()
                    self.adjust_size()
            self.random_stats()
        turtle.done()

    def select_case(self):
        if self.option == 1:
            self.case1()
        elif self.option == 2:
            self.case2()
        elif self.option == 3:
            self.case3()
        elif self.option == 4:
            self.case4()
        elif self.option == 5:
            self.case5()
        elif self.option == 6:
            self.case6()
        elif self.option == 7:
            self.case7()
        elif self.option == 8:
            self.case8()
        else:
            self.case9()

art = Polygon()

art.select_case()

'''
def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original 
draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()'''