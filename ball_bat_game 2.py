from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
o=1
p=1
FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

deltaX = 1
deltaY = 1
time_interval = 10  # try  2,5,7 msec
key_x=WINDOW_WIDTH-30

class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


ball = RECTA(100, 100, 120, 120)  # initial position of the ball
wall = RECTA(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player = RECTA(0, 0, 60, 10)  # initial position of the bat
player2= RECTA(WINDOW_WIDTH-60,WINDOW_HEIGHT-10,WINDOW_WIDTH,WINDOW_HEIGHT)

# Initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)


def DrawRectangle(rect):
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def drawText(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.13, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)


def Test_Ball_Wall(ball, wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    if ball.right >= wall.right:
        return FROM_RIGHT
    if ball.left <= wall.left:
        return FROM_LEFT
    if ball.top >= wall.top:
        return FROM_TOP
    if ball.bottom <= wall.bottom:
        return FROM_BOTTOM


def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom == player.top and ball.left >= player.left-20 and ball.right <= player.right+20 and deltaY == -1: #(try this)
        global o
        o=0
        return True
    return False

def Test_Ball_Player2(ball, player):  # Collision Detection between Ball and Bat
    if ball.top == player.bottom and ball.left >= player.left-20 and ball.right <= player.right+20 and deltaY == 1: #(try this)
        global p
        p=0
        return True
    return False

# Key Board Messages
def keyboard(key, x, y):
    global key_x
    if key ==b"a":
        key_x-=20
    elif key==b"d":
        key_x+=20
    if key == b"q":
        sys.exit(0)


mouse_x = 0


def MouseMotion(x, y):
    global mouse_x
    mouse_x = x


def Timer(v):
    Display()

    glutTimerFunc(time_interval, Timer, 1)


p2result = 0
p1result = 0


def Display():
    global p2result
    global p1result
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY
    global o,p
    glClear(GL_COLOR_BUFFER_BIT)

    string = "Player 2 : " + str(p2result)
    drawText(string, 10, 440)
    string = "Player 1 : " + str(p1result)
    drawText(string, 10, 400)

    ball.left = ball.left + deltaX  # updating ball's coordinates
    ball.right = ball.right + deltaX
    ball.top = ball.top + deltaY
    ball.bottom = ball.bottom + deltaY
    if o>=0 and o<1:
        o+=.1
    if p>=0 and p<1:
        p+=.1
    glColor(1, 1, 1)  # White color

    DrawRectangle(ball)

    if Test_Ball_Wall(ball, wall) == FROM_RIGHT:
        deltaX = -1

    if Test_Ball_Wall(ball, wall) == FROM_LEFT:
        deltaX = 1

    if Test_Ball_Wall(ball, wall) == FROM_TOP:
        deltaY = -1
        p1result=p1result +1

    if Test_Ball_Wall(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        p2result = p2result + 1

    player.left = mouse_x - 30
    player.right = mouse_x + 30
    player2.left = key_x-30
    player2.right = key_x+30
    glColor(1,o,o)
    DrawRectangle(player)
    glColor(1,p,p)
    DrawRectangle(player2)

    if Test_Ball_Player(ball, player) == True:
        deltaY = 1
        p1result = p1result + 1

    if Test_Ball_Player2(ball, player2) == True:
        deltaY = -1
        p2result = p2result + 1

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Simple Ball Bat OpenGL game");
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    init()
    glutMainLoop()


main()
