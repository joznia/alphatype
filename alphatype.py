# python program to draw letters using a turtle
# written by joznia, 06-feb-2021
import sys
import turtle as tt
import time

# what word(s) to draw (all lowercase):
draw_words = 'turtle'

# turtle config
screen_size_x = 1600
screen_size_y = 900
pen_speed = 200
pen_width = 3
pen_color = 'green'
pen_show_arrow = False
letter_spacing = True # with this disabled, letters will stack on top of each other
exit_on_finish = False

# define functions and put them in classes
t = tt.Pen()

class Funcs:
    def str2list(self, convstring: str):
        list1=[]
        list1[:0]=convstring
        return list1
    # apply the configuration
    def applyconfig(self):
        t.speed(pen_speed)
        t.width(pen_width)
        t.color(pen_color)
        if pen_show_arrow == True:
            t.showturtle()
        else:
            t.hideturtle()
f = Funcs()

class Letter(Funcs):
    pass

class Control(Letter):
    def reset(self):
        t.setheading(0)
    def new(self):
        t.up()
        c.pointup()
        t.right(90)
        t.forward(90)
        c.pointdown()
        t.down()
    def ret(self, dist: float):
        t.up()
        t.backward(dist)
        t.down()
    def returndown(self, dist: float):
        t.down()
        t.backward(dist)
        t.down()
    def startnew(self):
        c.pointdown()
        t.down()
        t.forward(115)
    def pointdown(self):
        t.setheading(270)
    def pointup(self):
        t.setheading(90)
    def pointleft(self):
        t.setheading(180)
    def pointright(self):
        t.setheading(0)
    def letterspace(self):
        if letter_spacing == True:
            c.new()
        else:
            pass
c = Control()

# define how to draw characters
class Char(Letter):
    def a(self):
        c.startnew()
        t.up()
        c.pointup()
        t.forward(80)
        c.pointright()
        t.down()
        t.forward(70)
        c.pointdown()
        t.forward(80)
        c.ret(80)
        c.pointup()
        t.forward(35)
        c.pointleft()
        t.forward(70)
        c.pointdown()
    def b(self):
        c.startnew()
        c.pointright()
        t.forward(70)
        c.pointup()
        t.forward(57)
        c.pointleft()
        t.forward(60)
        c.pointup()
        t.forward(1)
        c.pointright()
        t.forward(60)
        c.pointup()
        t.forward(57)
        c.pointleft()
        t.forward(70)
        c.pointdown()
    def c(self):
        c.startnew()
        c.pointright()
        t.forward(70)
        c.ret(70)
        t.up()
        c.pointup()
        t.forward(115)
        c.pointright()
        t.down()
        t.forward(70)
        c.ret(70)
        c.pointdown()
    def d(self):
        c.startnew()
        c.pointright()
        diagangle = 62
        t.left(diagangle)
        t.forward(71)
        c.pointup()
        t.left(diagangle / 2)
        t.forward(64)
        c.pointdown()
        t.forward(3)
        c.ret(3)
    def e(self):
        c.startnew()
        for _ in range(3):
            c.pointright()
            t.forward(70)
            c.ret(70)
            c.pointup()
            t.up()
            t.forward(57.5)
            t.down()
        t.up()
        c.pointdown()
        t.forward(57.5)
    def f(self):
        t.up()
        c.pointright()
        t.forward(115 / 2 + (115 / 7))
        t.down()
        t.backward(70)
        t.right(90)
        t.forward(35)
        t.left(90)
        t.forward(50)
        c.ret(50)
        t.right(90)
        t.forward(80)
        c.pointleft()
        t.up()
        t.forward(70)
        c.pointup()
        t.forward(115)
        c.pointright()
        t.forward(70)
        c.pointdown()
    def g(self):
        c.startnew()
        c.pointright()
        t.forward(70)
        c.pointup()
        t.forward(50)
        c.pointleft()
        t.forward(50)
        c.ret(50)
        c.pointup()
        t.up()
        t.forward(65)
        c.pointleft()
        t.down()
        t.forward(70)
        c.pointdown()
    def h(self):
        c.startnew()
        t.up()
        c.ret(57.5)
        c.pointright()
        t.down()
        t.forward(70)
        c.pointup()
        t.forward(57.5)
        c.ret(57.5)
        c.pointdown()
        t.forward(57.5)
        t.up()
        c.pointleft()
        t.forward(70)
        c.pointup()
        t.forward(115)
        c.pointdown()
    def i(self):
        c.pointright()
        t.up()
        t.forward(35)
        c.startnew()
        t.up()
        c.pointleft()
        t.forward(35)
        c.pointright()
        t.down()
        t.forward(70)
        t.up()
        c.ret(35)
        c.pointup()
        t.forward(115)
        t.up()
        c.pointright()
        t.forward(35)
        c.pointleft()
        t.down()
        t.forward(70)
        c.pointdown()
    def j(self):
        c.pointright()
        t.up()
        t.forward(35)
        c.startnew()
        c.pointleft()
        t.forward(35)
        c.pointup()
        t.forward(40)
        c.ret(40)
        c.pointleft()
        c.ret(35)
        c.pointup()
        t.forward(115)
        t.up()
        c.pointright()
        t.forward(35)
        c.pointleft()
        t.down()
        t.forward(70)
        c.pointdown()
    def k(self):
        c.startnew()
        c.ret(57.5)
        c.pointup()
        t.right(30)
        t.forward(70)
        c.ret(70)
        t.right(120)
        t.forward(70)
        c.ret(70)
        t.up()
        c.pointup()
        t.forward(57.5)
        c.pointdown()
    def l(self):
        c.startnew()
        c.pointright()
        t.forward(70)
        t.up()
        c.pointup()
        t.forward(115)
        c.pointleft()
        t.forward(70)
        c.pointdown()
    def m(self):
        c.startnew()
        c.ret(115)
        c.pointright()
        t.right(55)
        t.forward(80)
        t.left(110)
        t.forward(80)
        c.pointdown()
        t.forward(115)
        t.up()
        c.pointleft()
        t.forward(70)
        c.pointup()
        t.forward(115)
        c.pointdown()
    def n(self):
        c.startnew()
        c.ret(115)
        c.pointright()
        t.right(70)
        t.forward(120)
        c.pointup()
        t.forward(115)
        c.pointleft()
        t.up()
        t.forward(41)
        c.pointdown()
        t.forward(1)
    def o(self):
        c.startnew()
        c.pointright()
        t.forward(70)
        c.pointup()
        t.forward(115)
        c.pointleft()
        t.forward(70)
        c.pointdown()
    def p(self):
        c.startnew()
        c.ret(115)
        c.pointright()
        t.forward(70)
        c.pointdown()
        t.forward(35)
        c.pointleft()
        t.forward(70)
        c.pointup()
        t.forward(35)
        c.pointdown()
    def q(self):
        c.startnew()
        c.pointright()
        t.forward(70)
        c.pointup()
        t.forward(115)
        c.pointleft()
        t.forward(70)
        c.pointdown()
        t.up()
        t.forward(115)
        c.pointright()
        t.forward(70)
        c.pointup()
        t.left(45)
        t.down()
        t.forward(70)
        c.ret(70)
        t.up()
        c.pointup()
        t.forward(115)
        c.pointleft()
        t.forward(70)
        c.pointdown()
    def r(self):
        c.startnew()
        c.ret(115)
        c.pointright()
        t.forward(70)
        c.pointdown()
        t.forward(45)
        c.pointleft()
        t.forward(70)
        c.pointright()
        t.right(45)
        t.forward(100)
        c.ret(100)
        c.pointup()
        t.up()
        t.forward(45)
        c.pointdown()
    def s(self):
        c.pointdown()
        t.up()
        t.forward(115)
        c.pointright()
        t.down()
        t.forward(70)
        c.pointup()
        t.forward(57.5)
        c.pointleft()
        t.forward(70)
        c.pointup()
        t.forward(57.5)
        c.pointright()
        t.forward(70)
        c.ret(70)
        c.pointdown()
    def t(self):
        c.pointright()
        t.up()
        t.forward(35)
        c.startnew()
        c.pointup()
        t.forward(115)
        t.up()
        c.pointright()
        t.forward(35)
        c.pointleft()
        t.down()
        t.forward(70)
        c.pointdown()
    def u(self):
        c.startnew()
        c.pointright()
        t.forward(70)
        c.pointup()
        t.forward(115)
        t.up()
        c.pointleft()
        t.forward(70)
        c.pointdown()
    def v(self):
        c.pointdown()
        t.left(25)
        t.forward(80)
        t.left(25 * 5)
        t.forward(90)
        c.pointleft()
        t.up()
        t.forward(75)
        c.pointdown()
    def w(self):
        for _ in range(2):
            c.startnew()
            c.pointright()
            t.forward(40)
            c.pointup()
            t.forward(115)
        c.pointleft()
        t.up()
        t.forward(70)
        c.pointdown()
    def x(self):
        t.up()
        offset = 50
        c.pointdown()
        t.forward(offset + 10)
        c.pointright()
        t.forward(offset)
        c.pointup()
        t.down()
        t.right(45)
        fwd = 80
        t.forward(fwd)
        t.backward(fwd * 2)
        t.forward(fwd)
        t.left(90)
        t.forward(fwd)
        t.backward(fwd * 2)
        c.pointleft()
        t.up()
        t.forward(fwd * .8)
        c.pointup()
        t.forward(fwd * 1.4)
        c.pointdown()
    def y(self):
        c.pointdown()
        t.forward(57.5)
        c.pointright()
        t.forward(35)
        c.pointdown()
        t.forward(57.5)
        c.ret(57.5)
        c.pointright()
        t.forward(35)
        c.pointup()
        t.forward(57.5)
        t.up()
        c.pointleft()
        t.forward(70)
        c.pointdown()
    def z(self):
        c.pointright()
        fwdam = 90
        t.forward(fwdam)
        c.pointdown()
        t.right(35)
        t.forward(141)
        c.pointright()
        t.forward(fwdam)
        t.up()
        c.pointup()
        t.forward(fwdam + 27)
        c.pointleft()
        t.forward(fwdam - 15)
        c.pointdown()
l = Char()

# apply screen size
screen = tt.Screen()
screen.setup(screen_size_x, screen_size_y)

# move turtle to the left side
t.up()
screen_size_x_goto = (screen_size_x / 10) + (screen_size_x / 2) + (screen_size_x - (2 * screen_size_x))
t.goto(screen_size_x_goto, 0)

# print the characters
wordsaslist = f.str2list(draw_words)
for charobj in wordsaslist:
    if charobj != ' ':
        t.down()
        try: 
            f.applyconfig()
            eval('l.'+charobj+'()')
            c.letterspace()
        except:
            # draw an error message if there is an invalid character
            t.color('red')
            t.speed(100 ** 100)
            errwords = f.str2list("error")
            for errobj in errwords:
                eval('l.'+errobj+'()')
                c.new()
    else:
        c.letterspace()

if exit_on_finish == True:
    pass
else:
    # super lazy and stupid way of keeping the turtle window open
    while True:
        try:
            t.left(0)
        except:
            exit

        