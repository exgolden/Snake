from tkinter import *
import random

#Parametros
WIDTH=700
HEIGHT=700
SPEED=200
SIZE=50
PARTES=10
COLOR_S="#FFFFFF"
COLOR_B="#000000"
COLOR_F="#FF0000"

#Clases y funciones
class Food:
    def __init__(self):
        x=random.randint(0, (WIDTH/SIZE)-1)*SIZE
        y=random.randint(0, (HEIGHT/SIZE)-1)*SIZE
        self.coordinates=[x,y]
        canvas.create_rectangle(x,y,(x+SIZE),(y+SIZE), fill=COLOR_F, tag="food")
class Snake:
    def __init__(self):
        self.body_size=PARTES
        self.coordinates=[]
        self.squares=[]
        for i in range (0, PARTES):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,(x+SIZE),(y+SIZE), fill=COLOR_S, tag="snake")
            self.squares.append(square)
def collision(snake):
    x,y=snake.coordinates[0]
    if(x<0) or (x>=WIDTH):
        return True 
    elif(y<0) or (y>=HEIGHT):
        return True 
    for parts in snake.coordinates[1:]:
        if x==parts[0] and y==parts[1]:
            return True 
    return False
def Game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
def Turn(snake, food):
    x,y=snake.coordinates[0]
    if direction=="up":
        y-=SIZE
    if direction=="down":
        y+=SIZE
    if direction=="left":
        x-=SIZE
    if direction=="right":
        x+=SIZE
    snake.coordinates.insert(0, (x,y))
    square=canvas.create_rectangle(x,y,(x+SIZE),(y+SIZE), fill=COLOR_S, tag="snake")
    snake.squares.insert(0,square) 
    if(x==food.coordinates[0]) and (y==food.coordinates[1]):
        global score
        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if collision(snake):
        Game_over()
    else:
        window.after(SPEED, Turn, snake, food)
    
def Change_direction(New_direction):
    global direction
    if New_direction=="left":
        if direction!="right":
            direction=New_direction
    elif New_direction=="right":
        if direction!="left":
            direction=New_direction
    elif New_direction=="up":
        if direction!="down":
            direction=New_direction  
    elif New_direction=="down":
        if direction!="up":
            direction=New_direction
#GUI
window=Tk()
window.title("Snake")
window.resizable(False, False)
score=0
direction="down"
label=Label(window, text="Score:{}".format(score))
label.pack()
canvas=Canvas(window, bg=COLOR_B, height=HEIGHT, width=WIDTH)
canvas.pack()
window.bind("<Left>", lambda event: Change_direction("left"))
window.bind("<Right>", lambda event: Change_direction("right"))
window.bind("<Up>", lambda event: Change_direction("up"))
window.bind("<Down>", lambda event: Change_direction("down"))


snake=Snake()
food=Food()
Turn(snake, food)



window.mainloop()