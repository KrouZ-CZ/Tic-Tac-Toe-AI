import tkinter as tk
from tkinter.messagebox import *

from minmax import *
from check import *

ar = {0:"+", 1:"X", -1:"O"}
ab = {0:"BLACK", 1:"RED", -1:"BLUE"}

class Game:
    def btn1():
        if btn1['text'] == "+":
            Game.change(0)
    def btn2():
        if btn2['text'] == "+":
            Game.change(1)
    def btn3():
        if btn3['text'] == "+":
            Game.change(2)
    def btn4():
        if btn4['text'] == "+":
            Game.change(3)
    def btn5():
        if btn5['text'] == "+":
            Game.change(4)
    def btn6():
        if btn6['text'] == "+":
            Game.change(5)
    def btn7():
        if btn7['text'] == "+":
            Game.change(6)
    def btn8():
        if btn8['text'] == "+":
            Game.change(7)
    def btn9():
        if btn9['text'] == "+":
            Game.change(8)
    def change(i):
        global area
        area[i] = 1
        Game.draw()
        if Game.check(): return
        Game.computer()
        Game.draw()
        Game.check()
    def check():
        win = check_win(area)
        if win == None: return
        if win == 1:
            showinfo(message=f'Выиграли: {ar[win]}')
        elif win == -1:
            showinfo(message=f'Выиграли: {ar[win]}')
        elif win == 0:
            showinfo(message=f'Ничья')
        return True
    def computer():
        global area
        b = AI.get(area)
        if b == None: return
        area[int(b)] = -1
    def draw():
        btn1["text"] = ar[area[0]]
        btn2["text"] = ar[area[1]]
        btn3["text"] = ar[area[2]]
        btn4["text"] = ar[area[3]]
        btn5["text"] = ar[area[4]]
        btn6["text"] = ar[area[5]]
        btn7["text"] = ar[area[6]]
        btn8["text"] = ar[area[7]]
        btn9["text"] = ar[area[8]]

        btn1["fg"] = ab[area[0]]
        btn2["fg"] = ab[area[1]]
        btn3["fg"] = ab[area[2]]
        btn4["fg"] = ab[area[3]]
        btn5["fg"] = ab[area[4]]
        btn6["fg"] = ab[area[5]]
        btn7["fg"] = ab[area[6]]
        btn8["fg"] = ab[area[7]]
        btn9["fg"] = ab[area[8]]
    def reset():
        global area
        area = [0 for i in range(9)]
        Game.draw()

area = [0 for i in range(9)]
root = tk.Tk()
root.geometry("450x600")
root.title("КРЕСТИКИ НОЛИКИ")
root.resizable(False, False)

all_btn = []

txt = tk.Label(master=root, text='Tic-Tac-Toe VS AI', font='Times 30')
txt.pack()

btn1 = tk.Button(master=root, text="+", command=Game.btn1, width=7, height=3)
btn2 = tk.Button(master=root, text="+", command=Game.btn2, width=7, height=3)
btn3 = tk.Button(master=root, text="+", command=Game.btn3, width=7, height=3)
btn4 = tk.Button(master=root, text="+", command=Game.btn4, width=7, height=3)
btn5 = tk.Button(master=root, text="+", command=Game.btn5, width=7, height=3)
btn6 = tk.Button(master=root, text="+", command=Game.btn6, width=7, height=3)
btn7 = tk.Button(master=root, text="+", command=Game.btn7, width=7, height=3)
btn8 = tk.Button(master=root, text="+", command=Game.btn8, width=7, height=3)
btn9 = tk.Button(master=root, text="+", command=Game.btn9, width=7, height=3)
res = tk.Button(master=root, text="RESET", command=Game.reset, width=7, height=1)

btn1.place(x=80, y=100)
btn2.place(x=180, y=100)
btn3.place(x=280, y=100)
btn4.place(x=80, y=200)
btn5.place(x=180, y=200)
btn6.place(x=280, y=200)
btn7.place(x=80, y=300)
btn8.place(x=180, y=300)
btn9.place(x=280, y=300)
res.place(x=180, y=400)

root.mainloop()
