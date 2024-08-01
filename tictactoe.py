import tkinter # graphical user interface library

def set_tile(row, column):
    global curr_player # using global so it is not treated like a local variable

    if (game_over):
        return

    if board[row][column]["text"] != "": # prevents overriding an already taken spot
        return

    board[row][column]["text"] = curr_player # mark the board

    if curr_player == playerO: # switch players
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player+"'s turn"

    # check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # check horizontally
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=yellow)
            for column in range(3):
                board[row][column].config(foreground=yellow, background=light_gray)
            game_over = True
            return
    
    # check vertically
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=yellow)
            for row in range(3):
                board[row][column].config(foreground=yellow, background=light_gray)
            game_over = True
            return
        
    # check diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
         and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=yellow)
        for i in range(3):
            board[i][i].config(foreground=yellow, background=light_gray)
        game_over = True
        return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=yellow)
        for i in range(3):
            board[i][2 - i].config(foreground=yellow, background=light_gray)
        game_over = True
        return
    
    if (turns == 9 and game_over != True):
        game_over = True
        label.config(text="Tie!", foreground=yellow)

def new_game():
    global turns, game_over

    turns = 0
    game_over = False
    label.config(text=curr_player+"'s turn", foreground="white")
    
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=blue, background=gray)


# game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
turns = 0
game_over = False

# hexidecimal notation for colors
blue = "#4584b6"
yellow = "#ffde57"
gray = "#343434"
light_gray = "#646464"

# window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False) # does not let the user resize the window's width or height

frame = tkinter.Frame(window) # puts the window inside the frame
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20),
                      background=gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# assigning each place on the board a button
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=gray, foreground=blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column) # the label is at row 0 so offset it by 1

# creating a restart button
restart_button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=gray,
                        foreground="white", command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()