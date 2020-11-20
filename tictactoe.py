from tkinter import Tk, PhotoImage, Button, DISABLED, Label
grid = [[3, 4, 5], 
        [6, 7, 8], 
        [9, 10, 11]]

def win():
        popup = Tk()
        popup.title("Winner!")
        popup.geometry("200x40")
        if player == False:
                label = Label(popup, text="Red is the winner!", font=("Verdana", 12))
                label.pack()
        else: 
                label = Label(popup, text="Green is the winner!", font=("Verdana", 12))
                label.pack()
        popup.mainloop()

def tie():
        popup = Tk()
        popup.title("Tie!")
        label = Label(popup, text="Tie!", font=("Verdana", 12))
        label.pack()
        popup.geometry("200x40")
        popup.mainloop()

def gridcheck():
        fullgrid = True
        for i in range(3):
                if grid[0][i] == grid[1][i] == grid[2][i] or grid[i][0] == grid[i][1] == grid[i][2] or grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]:
                        win()
                        fullgrid = False
                        break
        for i in range(3):
                for j in range(3):
                        if grid[i][j] != 1 and grid[i][j] != 2:
                                fullgrid = False
        if fullgrid == True:
                tie()



def windowconfig():
        window.geometry("499x499")
        window.title("Tic Tac Toe")


def onclick(num):
        for i in range(9):
                global player
                if num == i and player == True:
                        buttonlist[i] = Button(window, image = red, state = DISABLED)
                        buttonlist[i].grid(column = i%3, row = int(i/3))
                        grid[int(i/3)][i%3] = 1
                        player = False
                        break
                if num == i and player == False:
                        buttonlist[i] = Button(window, image = green, state = DISABLED)
                        buttonlist[i].grid(column = i%3, row = int(i/3))
                        grid[int(i/3)][i%3] = 2
                        player = True
                        break
        gridcheck()
window = Tk()
windowconfig()

global default, red, green, buttonlist, player
default = PhotoImage(file="default.png")
red = PhotoImage(file="red.png")
green = PhotoImage(file="green.png")  
buttonlist = [] #left -> right, top -> bottom
player = True # true = red

for i in range(9):
        buttonlist.append(Button(window, image = default, command=lambda i=i : onclick(i)))
        buttonlist[i].grid(column = i%3, row = int(i/3))

window.mainloop()