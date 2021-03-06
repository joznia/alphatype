# python program to draw letters using a turtle
# written by joznia
import turtle as tt

# turtle config
screen_size_x = 1000
screen_size_y = 600
pen_speed = 200
pen_width = 1
pen_color = 'black'
pen_show_arrow = False
letter_spacing = True     # if disabled, letters will stack on top of each other
recursive_prompt = True   # if disabled, don't keep asking for new words when finished with the initial one
prompt_spacing = True     # if disabled, every successive prompt for words won't have a space in between, regardless of the value of letter_spacing
ask_msg = 'what word(s) to draw (all lowercase):\n'

# get input for words
draw_words = input(ask_msg)

# define functions and put them in classes
t = tt.Pen()


class Funcs:
    # turn a string into a list of characters
    def str2list(self, convstring: str):
        list1 = []
        list1[:0] = convstring
        return list1

    # apply (some of) the configuration
    def applyconfig(self):
        t.speed(pen_speed)
        t.width(pen_width)
        t.color(pen_color)
        if pen_show_arrow is True:
            t.showturtle()
        else:
            t.hideturtle()

    def drawletters(self):
        wordsaslist = f.str2list(draw_words)
        for charobj in wordsaslist:
            if charobj == '!':
                f.specchar("excl")
            elif charobj == '?':
                f.specchar("ques")
            elif charobj == '.':
                f.specchar('peri')
            elif charobj == '\'':
                f.specchar('squo')
            elif charobj == '\"':
                f.specchar('dquo')
            elif charobj == '=':
                f.specchar('equa')
            elif charobj == 'l':
                f.specchar('letterl')
            elif charobj != ' ':
                t.down()
                try:
                    f.applyconfig()
                    eval('ch.'+charobj+'()')
                    c.letterspace()
                except Exception:
                    # draw an error message if there is an invalid character
                    t.color('red')
                    t.speed(100 ** 100)
                    errwords = f.str2list("error")
                    for errobj in errwords:
                        eval('ch.'+errobj+'()')
                        c.new()
            else:
                c.letterspace()

    def specchar(self, charto: str):
        t.down()
        f.applyconfig()
        eval('ch.'+charto+'()')
        c.letterspace()


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
        if letter_spacing is True:
            c.new()
        else:
            pass

    def promptspace(self):
        if prompt_spacing is True:
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
        t.left(45)
        t.forward(80)
        c.pointup()
        c.pointleft()
        t.right(46)
        t.forward(81)
        c.pointleft()
        t.up()
        t.forward(20)

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

    def letterl(self):
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

    def excl(self):
        c.pointdown()
        t.forward(100)
        t.up()
        t.forward(10)
        t.down()
        t.forward(5)
        t.up()
        c.pointup()
        t.forward(115)
        c.pointdown()

    def ques(self):
        c.pointright()
        t.forward(70)
        c.pointdown()
        t.forward(50)
        c.pointleft()
        t.forward(70)
        c.pointdown()
        t.forward(55)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        c.pointup()
        t.forward(115)
        c.pointright()

    def peri(self):
        t.up()
        c.pointdown()
        t.forward(110)
        t.down()
        t.forward(5)
        t.up()
        c.pointup()
        t.forward(115)
        c.pointdown()

    def squo(self):
        c.pointdown()
        t.forward(50)
        c.ret(50)
        c.pointdown()

    def dquo(self):
        c.pointdown()
        t.forward(50)
        c.ret(50)
        c.pointright()
        t.up()
        t.forward(15)
        t.down()
        c.pointdown()
        t.forward(50)
        c.ret(50)
        c.pointright()

    def equa(self):
        c.pointdown()
        t.up()
        t.forward(57.5)
        t.down()
        c.pointright()
        t.forward(70)
        c.ret(70)
        t.up()
        c.pointdown()
        t.forward(20)
        t.down()
        c.pointright()
        t.forward(70)
        c.ret(70)
        t.up()
        c.pointup()
        t.forward(57.5 + 20)


ch = Char()

# apply screen size
screen = tt.Screen()
screen.setup(screen_size_x, screen_size_y)

# move turtle to the left side
t.up()
ssx = screen_size_x
screen_size_x_goto = (ssx / 10) + (ssx / 2) + (ssx - (2 * ssx))
t.goto(screen_size_x_goto, 0)

# print the characters
f.drawletters()
c.promptspace()
if recursive_prompt is True:
    while True:
        draw_words = input(ask_msg)
        f.drawletters()
        c.promptspace()
    else:
        exit()
