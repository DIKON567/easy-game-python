import time

import random
import asyncio
from tkinter import *
from tkinter import messagebox
import os
import sys
import json



def kick():
    sys.exit()
def Rules():
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")
    messagebox.showerror("???", "11010000 10011111 11010000 10111110 11010000 10111001 11010000 10111100 11010000 10111000 11010001 10000010 11010000 10110101 100000 11010000 10111101 11010000 10110000 11010000 10111010 11010000 10111110 11010000 10111101 11010000 10110101 11010001 10000110 100000 11010000 10111110 11010000 10110100 11010000 10111101 11010001 10000011 100000 11010000 10110010 11010000 10110101 11010001 10001001 11010001 10001100 100000 11010000 10110110 11010000 10111000 11010000 10110111 11010000 10111101 11010000 10111000 100001")

def error():
    root = Tk()
    root.title("\nError")
    text = Text(width=150, height=30, bg="black",
            fg='white', wrap=WORD)
    text.pack()
    text.insert(1.0, "(pygame 2.1.2 (SDL 2.0.18, Python 3.10.4)\nHello from the pygame community. https://www.pygame.org/contribute.html\nProcess finished with exit code 4\n")
    button = Button(text="ВЫХОД", command=kick)
    button.pack()
    root.mainloop()
import tkinter
import turtle
from turtle import *

import tkinter as tk
def quit():
    win = tk.Tk()
    win.option_add("*Button.Background", "white")
    win.option_add("*Button.Foreground", "green")
    win.title('Хаос простой системы')
    win.geometry("500x500")
    win.resizable(0, 0)
    fom = tk.Frame(master=win,bg='yellow')
    fom.pack_propagate(0)
    fom.pack(fill=tk.BOTH, expand=1)
    import pygame

    pygame.init()
    pygame.mixer.music.load("музыка.mp3")
    pygame.mixer.music.play()
    j = tk.Button(master=fom, text='Начать игру', width=50, height=20, command=win.destroy)
    j.pack()
    qu = tk.Button(master=fom, text='Выход', width=50, height=10, command=sys.exit)
    qu.pack()
    me = tk.Label(master=fom, text='Игра от разработчиков: DIKON', width=150, height=30, bg='red', fg='black')
    me.pack()
    win.mainloop()
quit()
def quitT():
    t = turtle.Turtle()
    t.hideturtle()
    t.clear()
    win = tk.Tk()
    win.option_add("*Button.Background", "white")
    win.option_add("*Button.Foreground", "green")
    win.title('Хаос простой системы')
    win.geometry("500x500")
    win.resizable(0, 0)
    fom = tk.Frame(master=win,bg='yellow')
    fom.pack_propagate(0)
    fom.pack(fill=tk.BOTH, expand=1)
    import pygame

    pygame.init()
    pygame.mixer.music.load("музыка.mp3")
    pygame.mixer.music.play()
    j = tk.Button(master=fom, text='Начать игру', width=50, height=20, command=win.destroy)
    j.pack()
    qu = tk.Button(master=fom, text='Выход', width=50, height=10, command=sys.exit)
    qu.pack()
    me = tk.Label(master=fom, text='Игра от разработчиков: DIKON', width=150, height=30, bg='red', fg='black')
    me.pack()
    win.mainloop()
    global d
    д = turtle.textinput("Выбор режима", "Выберите режим!\nОдиночный\nКлассика\nСтратегия")
import turtle

turtle.title("Хаос простой системы!!!")
try:

    img = tkinter.Image("photo", file="icon222.png")

except:
    pass
with open('role.json', 'r') as f:
    sure = json.load(f)

if 0 in sure["nnn"]:
    vvv = turtle.textinput("Имя", "Как вас зовут?")
    with open('namen.json', 'w') as k:
        json.dump({'name': [vvv]}, k)
    with open('role.json', 'w') as g:
        json.dumps(sure)
        json.dump({'nnn': [1]}, g)
else:
    pass

with open('name.json', 'r') as о:
    wl = json.load(о)
    v = wl["namen"][0]
turtle.color('black')
style = ('Arial', 30, 'italic')
turtle.write(v +  ", добро пожаловать!", font=style, align='center')
time.sleep(2)
turtle.hideturtle()
clear()
try:
    turtle._Screen._root.iconphoto(True, img)
except:
    messagebox.showerror("Ошибка", "Не удалось выбрать иконку игры")

turtle.onkey(quitT, "`")
global d
д = turtle.textinput("Выбор режима", "Выберите режим!\nОдиночный\nКлассика\nComing soon...")
pen = turtle.Turtle()
def f():
    lol.lt(60)

def a():
    lol.fd(50)

def j(x, y):
    lol.forward(50)

def secret():
    window = Tk()
    window.title("???")
    welcome = Label(window, text="•−− −•−−   −• •   •−−• −−− −• •• −− •− • − • •−•−•−   ••−•• − −−−   −•• •−• ••− −−• −−− • −−••−−\n−−− −• ••   •−−• •−• −•−− −−• •− ••−− − •−•−•−   •−− • ••• • •−•• •−•− − ••• •−•− •−•−•−   •−−• −−− −•− •−   −− −•−−   ••• − •−• •− −•• •− • −−   −−•• −•• • ••• −••− •••••• ", background="white", foreground="red")
    welcome.grid(row=8, column=1, columnspan=8)
    rules = Button(window, text="???", command=Rules)
    rules.grid(row=1, column=0, columnspan=1)
    window.mainloop()




pen.write("Точка спавна", font=("Calibri", 8, "bold"))
if д == "Одиночный":
    screen = turtle.Screen()
    lol = turtle.Turtle()
    screen.onkey(lambda: turtle.bye(), "q")
    screen.listen()
    screen.onkey(f, "w")
    screen.onkey(a, "d")




    lol.onclick(j)
    turtle.mainloop()


elif д == "???":
    error()
elif д == "ERR":
    sys.exit()

if д == "Классика":
    FONT = ("Arial", 14, "Развитие")
    square = turtle.Turtle()
    square.shape("turtle")
    square.forward(4)
    square.circle(random.random())
    color('red')
    forward(random.randint(100, 200))
    square.circle(random.random())
    gogo = [50, 36, 78]
    jojo = [89, 10, 7, 123, 1, 2, 5]
    circle(random.choice(gogo))
    begin_fill()
    pensize(3)
    left(50)
    color("green")
    end_fill()
    turtle1 = turtle.Turtle()
    for i in range(15):
        turtle1.forward(5)
        forward(200)
        turtle1.forward(random.choice(gogo))
        turtle1.circle(random.randint(60, 70))
        left(170)
        circle(random.choice(gogo))
        begin_fill()
        pensize(3)
        color(random.choice(["orange", "red", "yellow"]))
        left(50)
        forward(133)
        color(random.choice(["orange", "red", "yellow"]))
        turtle2 = turtle.Turtle()
        circle(random.choice(gogo), random.choice(jojo))
        color(random.choice(["orange", "red", "yellow"]))
        turtle2.color("blue")
        right(130)
        circle(40)
        turtle2.left(random.randint(54, 87))
        turtle1.right(random.randint(34, 45))
        turtle.left(30)
        left(30)
        left(50)
        turtle3 = turtle.Turtle()
        turtle3.forward(54)
        turtle3.color("green")
        turtle1.forward(random.randint(200, 550))
        turtle2.forward(random.randint(200, 550))
        turtle3.forward(random.randint(200, 550))
        color(random.choice(["orange", "red", "yellow"]))
        circle(random.choice([50, 60, 70, 80, 10, 50]))
        circle(random.choice([100, 60, 70, 80, 10, 50]))
        forward(random.choice([50, 60, 70, 80, 90, 123]))
        color(random.choice(["orange", "red", "yellow"]))
        turtle3.forward(random.randint(200, 550))
        square.forward(100)
        color("red")
        turtle2.forward(random.randint(200, 550))
        square.forward(random.choice([1, 20, 21, 45, 12, 1, 2, 3, 4, 5, 6, 7, 8]))
        square.right(random.random())
        square.left(random.choice([30, 60, 70]))
        square.circle(random.random())
        turtle2.forward(random.randint(200, 550))
        turtle1.forward(random.randint(200, 550))
        turtle3.color(random.choice(["red", "blue", "green"]))
        ikt= turtle.Turtle()
        ikt.shape("turtle")
        ikt.forward(500)
        end_fill()
        turtle2.circle(random.randint(4, 30))
        turtle1.left(random.randint(200, 550))
        begin_fill
        j = turtle.Turtle()
        j.shape("turtle")
        o = turtle.Turtle()
        o.shape("turtle")
        p = turtle.Turtle()
        p.shape("turtle")
        ik = turtle.Turtle()
        ik.shape("turtle")
        ik.forward(34)
        ik.circle(random.randint(20, 30))
        ik.right(500)
        j.left(random.choice([40, 40, 402, 43, 56]))
        o.left(random.randint(200, 550))
        j.forward(50)
    mode("logo")
    for i in range(10):
        color("yellow")
        color("red")
        ik.left(40)
        turtle2.forward(random.randint(200, 550))
        turtle3.forward(random.randint(200, 550))
        square.left(4)
        left(random.choice([50, 6, 3, 67, 254, 23, 75, 34, 42, 42, 526, 53]))
        square.right(5)
        forward(random.randint(5, 800))
        square.circle(random.choice([40, 23, 24, 25, 62, 12, 33, 21, 43, 34, 32, 35, 65]))
    for i in range(25):
        turtle1.forward(64)
        forward(random.choice([54, 12, 3, 67, 43, 56, 90, 10]))
        turtle1.forward(random.choice(gogo))
        circle(random.choice(gogo))
        begin_fill()
        pensize(3)
        color(random.choice(["orange", "red", "yellow"]))
        left(50)
        forward(133)
        color(random.choice(["orange", "red", "yellow"]))
        turtle2 = turtle.Turtle()
        circle(random.choice(gogo), random.choice(jojo))
        color(random.choice(["orange", "red", "yellow"]))
        turtle2.color("blue")
        right(130)
        circle(40)
        turtle2.left(random.randint(54, 87))
        turtle1.right(random.randint(34, 45))
        turtle.left(30)
        left(30)
        left(50)
        turtle3 = turtle.Turtle()
        turtle3.forward(54)
        turtle3.color("green")
        turtle1.forward(random.randint(200, 550))
        turtle2.forward(random.randint(200, 550))
        turtle3.forward(random.randint(200, 550))
        color(random.choice(["orange", "red", "yellow"]))
        circle(random.choice([50, 60, 70, 80, 10, 50]))
        circle(random.choice([100, 60, 70, 80, 10, 50]))
        forward(random.choice([50, 60, 70, 80, 90, 123]))
        color(random.choice(["orange", "red", "yellow"]))
        turtle3.forward(random.randint(200, 550))
        square.forward(100)
        color("red")
        turtle2.forward(random.randint(200, 550))
        square.forward(random.choice([1, 20, 21, 45, 12, 1, 2, 3, 4, 5, 6, 7, 8]))
        square.right(random.random())
        square.left(random.choice([30, 60, 70]))
        square.circle(random.random())
        forward(random.randint(200, 550))
        forward(random.randint(200, 550))
        turtle3.color(random.choice(["red", "blue", "green"]))
        forward(500)
        end_fill()
        turtle2.circle(random.randint(4, 30))
        left(random.randint(200, 550))
        begin_fill
        j = turtle.Turtle()
        j.shape("turtle")
        o = turtle.Turtle()
        o.shape("turtle")
        p = turtle.Turtle()
        p.shape("turtle")
        ik = turtle.Turtle()
        ik.shape("turtle")
        forward(34)

elif д == "666":
    import pygame
    pygame.mixer.music.stop()
    turtle.textinput("Что?", "Привет! Это я, Дун, я ошибка игрового кода! Ты нажал, выбрал, да и вообще возможно сделал что-то нитак. Советую перезайти в игру, однако можешь остаться...")
    turtle.textinput("А?", "Ты остался? Круто... На самом деле я обрячен на вечные страдания здесь, лишь избранные догадались освободить меня, но все без толку... Они попадали в жестокие ловушки кода система не пропускала их.")
    turtle.textinput("Выбор режима", "Ты еще здесь?")
    turtle.textinput("0000001000000001000000", "Тебе явно нужен отдых!\nПерезайди и спокойно играй...")
    import webbrowser
    webbrowser.open('https://yandex.ru/news/instory/Naparkovke_TC_vKHimkakh_voditel_nasmert_sbil_pyatiletnego_malchika--577f74750d6849d1792d81702f0d6381?persistent_id=5550', new=2)
    time.sleep(10)
    messagebox.showerror("Выход", "Игра дала сбой: Dyn.exe//critical_procces_died")
    sys.exit()

else:
    messagebox.showerror("Выбери карту!", "Ты не выбрал карту!")
    pass
