import tkinter
#import tkinter as tk

def set_title(row, column):
    global curr_player
    if (game_over):
        return
    if board[row][column]["text"] != "":
        return
    board[row][column]["text"] = curr_player
    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO
    label["text"] = curr_player+ "'s turns"
    # check_winner
    check_winner()
def check_winner():
    global turns, game_over
    turns += 1
    #Horzitonnally check_winner
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text = board[row][0]["text"] + " is the Winner !", foreground="yellow")
            for column in range(3):
                board[row][column].config(foreground="yellow", background="blue")
            game_over = True
            return

    # Vertically check_winner
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the Winner !", foreground="yellow")
            for row in range(3):
                board[row][column].config(foreground="yellow", background="blue")
            game_over = True
            return

    # diagonally check_winner
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0][
            "text"] != ""):
        label.config(text=board[0][0]["text"] + " is the Winner !", foreground="yellow")
        for i in range(3):
            board[i][i].config(foreground="yellow", background="blue")
        game_over = True
        return
    # anti-diagonally check_winner
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2][
            "text"] != ""):
        label.config(text=board[0][2]["text"] + " is the Winner !", foreground="yellow")
        board[0][2].config(foreground="yellow", background="blue")
        board[1][1].config(foreground="yellow", background="blue")
        board[2][0].config(foreground="yellow", background="blue")
        game_over= True
        return
    #Tie
    if(turns == 9):
        game_over = True
        label.config(text= "Tie", foreground="yellow")


def new_game():
    global turns, game_over
    turns = 0
    game_over = False
    label.config(text=curr_player+"'s truns", foreground="white")
    for row in range(3):
        for column in range (3):
            board[row][column].config(text= "", foreground="white", background="#4584b6")



#game parameters
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = curr_player + " 's turn", font=("Consolas", 20), background="#4584b6", foreground="white")

label.grid(row=0, column=0, columnspan=3)
for row in range(3):
    for column in range(3):
        board[row][column]= tkinter.Button(frame, text="", background="#4584b6", font=("Consolas", 50, "bold"), foreground="white", width=4, height=1,
                                           command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row = row+1, column=column)
button = tkinter.Button(frame, text = "restart", background="#4584b6",  foreground="white", command=new_game )
button.grid(row=4, column=0, columnspan=3)

turns = 0
game_over = False
frame.pack()
window.mainloop()