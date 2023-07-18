from tkinter import*
import random
import time


def start():
    tk=Tk()
    tk.title('Пін-понг')
    tk.resizable(0,0)
    tk.wm_attributes('-topmost',1)
    canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    class Ball:
        def __init__(self, canvas, paddle, color):
            self.paddle=paddle
            self.canvas=canvas
            self.id=canvas.create_oval(10, 10, 25, 25, fill=color)
            self.canvas.move(self.id, 245, 100)
            starts=[-3,-2,-1,1,2,3]
            random.shuffle(starts)
            self.x=starts[0]
            self.y=-3
            self.canvas_height=self.canvas.winfo_height()
            self.canvas_width=self.canvas.winfo_width()
            self.hit_bottom=False

        def hit_paddle(self, pos):
            paddle_pos=self.canvas.coords(self.paddle.id)
            if pos[2]>= paddle_pos[0] and pos[0]<=paddle_pos[2]:
                if pos[3]>=paddle_pos[1] and pos[3]<= paddle_pos[3]:
                    return True
            return False

        def draw(self):
            self.canvas.move(self.id,self.x,self.y)
            pos=self.canvas.coords(self.id)
            if pos[1]<=0:
                self.y=3
            if pos[3]>=self.canvas_height:
                self.hit_bottom=True
            if self.hit_paddle(pos)== True:
                self.y=-3
            if pos[0]<=0:
                self.x=3
            if pos[2]>=self.canvas_width:
                self.x=-3

    class Paddle:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
            self.canvas.move(self.id, 200, 300)
            self.x = random.choice([2, -2])  # Випадковий початковий напрямок руху ракетки
            self.canvas_width = self.canvas.winfo_width()

        def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = random.choice([2, 3])  # Зміна напрямку руху при досягненні лівого краю
            elif pos[2] >= self.canvas_width:
                self.x = random.choice([-2, -3])  # Зміна напрямку руху при досягненні правого краю

    paddle = Paddle(canvas, "blue")
    ball = Ball(canvas, paddle, 'green')

    while True:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
        else:
            break
        tk.update_idletasks()
        tk.update()
        time.sleep(0.015)





     
