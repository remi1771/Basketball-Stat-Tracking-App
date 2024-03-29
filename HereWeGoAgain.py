#Fuck My Life it's clear that I can't do cmd AND tkinter at the same time because i'm a shitty af programmer, so everything on tkinter it is which fucking sucks honestly because i'm not quite sure that tkinter has a getkey() functionality or something but oh well
#This is it boys



import pickle
import wx
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#Variables!
mainwindow1 = tk.Tk()  # Create the main mainwindow1
mainwindow1.geometry("512x512")
mainwindow1.maxsize(512, 512)

mainwindow1.title("Basketball Stat Tracking App by Remi1771")

player_list = tk.Label(mainwindow1) # Create a label to display the available players


last_action_label = None


#region Functions!
def save_players():
    try:
        with open('players.pkl', 'wb') as output:
            pickle.dump(game.players, output, pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_players():
    with open('players.pkl', 'rb') as input:
        game.players = pickle.load(input)
    game.update_player_list()
    show_screen_2()


# Function to clear the mainwindow1
def clear_window():
    for widget in mainwindow1.winfo_children():
        widget.destroy()

# Function to load a file PLACEHOLDER
def load_file():
    pass

# Function to save the game PLACEHOLDER
def save_game():
    pass

def input_action_code():
    pass
#endregion

#region Classes:

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = "Basketball Stat Tracking App by Remi1771", pos = wx.DefaultPosition, size = wx.Size(512,512), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        self.new_game_button = wx.Button(self, wx.ID_ANY, "New Game", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.new_game_button, 0, wx.ALL, 5)
        
        self.load_button = wx.Button(self, wx.ID_ANY, "Load", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.load_button, 0, wx.ALL, 5)
        
        self.SetSizer(bSizer1)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.new_game_button.Bind(wx.EVT_BUTTON, self.show_screen_2)
        self.load_button.Bind(wx.EVT_BUTTON, self.load_file)



class Player:
    def __init__(self, name, team, number):
        self._name = name
        self._team = team
        self._number = number
        self._possessions = 0
        self._dribbles = 0

class Team:
    def __init__(self, name):
        self.name = name
        self.has_the_ball = False
        self.possessions = {}
        self.total_points = 0
        
class Game:
    def __init__(self):
        self.current_possession = None
        self.players = []
        self.teams = [] #Was a dictionary changed it to index because teams should be numbers not names no one cares about names, lol
        self.current_possession = None
        self.Last_action_player_initiator = None
        self.Last_action_player_reciever = None
        self.Last_action_type = None
        self.action_history = []
        self.message = None
        self.message_history = []

    def dribble(self):
        self.current_possession._dribbles += 1
        self.Last_action_player_initiator = self.current_possession
        self.Last_action_player_reciever = self.current_possession
        self.Last_action_type = 'Dribbled'
        self.action_history.append({'player': self.current_possession, 'action': self.Last_action_type})
        self.message = f"{self.current_possession._name} dribbled {self.current_possession._dribbles} times!"
        self.message_history.append(self.message)
        print(self.message)
        last_action_label.config(text=self.message)

    def add_team(self, team):
        self.teams[team.name] = team
        
    def add_player(self, player):
        self.players.append(player)

    def update_player_list(self):
        global player_list
        player_info = [f"{player._name}({player._number}, {player._team})" for player in self.players]
        player_list.config(text=", ".join(player_info))
        player_list
#endregion
        
game = Game()

#region ====Screen 1 (Create or Load a game)====
def show_main_menu():
    try:
        clear_window()
        tk.Button(mainwindow1, text="New Game", command=show_screen_2).pack()
        tk.Button(mainwindow1, text="Load", command=load_file).pack()
    except Exception as e:
        messagebox.showerror("Error", str(e))
#endregion
  
#region ====Screen 2 (Select Players)====
def show_screen_2():
    clear_window()

    def start_match():
        try:
            team1_players = [player for player in game.players if player._team == "Team 1"]
            team2_players = [player for player in game.players if player._team == "Team 2"]
            if len(team1_players) < 2 or len(team2_players) < 2:
                raise ValueError("There must be at least two players on each team.")
            if not game.current_possession:
                raise ValueError("A player must have possession before starting the match.")
            selected_player_name = player_var.get()
            for player in game.players:
                if player._name == selected_player_name:
                    game.current_possession = player
                    print(game.current_possession)
                    break
            show_screen_3()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
              
    def add_player():
        try:
            player_name = player_name_entry.get()
            player_number = player_number_entry.get()
            team = team_var.get()
            if not player_name or not player_number:
                raise ValueError("Both player name and number must be provided.")
            player = Player(player_name, team, player_number)
            game.add_player(player)
            print(f"Added player {player_name} with number {player_number} to {team}")

            # Clear the input fields
            player_name_entry.delete(0, 'end')
            player_number_entry.delete(0, 'end')
            team_var.set("Select Team")

            # Update the list of available players
            game.update_player_list()
            show_screen_2()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    #region Buttons
    # Create a label to display the available players
    global player_list
    player_list_label_label = tk.Label(mainwindow1, text="Players Available")
    player_list_label_label.grid(row=7, column=0)
    player_list = tk.Label(mainwindow1)
    player_list.grid(row=7, column=1)

    # Player name entry
    player_name_label = tk.Label(mainwindow1, text="Player Name:")
    player_name_label.grid(row=1, column=0)
    player_name_entry = tk.Entry(mainwindow1)
    player_name_entry.grid(row=2, column=0)

    # Player number entry
    player_number_label = tk.Label(mainwindow1, text="Number:")
    player_number_label.grid(row=1, column=2)
    player_number_entry = tk.Entry(mainwindow1)
    player_number_entry.grid(row=2, column=2)

    # Team selection dropdown
    team_label = tk.Label(mainwindow1)
    team_label.grid(row=2, column=1)
    team_var = tk.StringVar(mainwindow1)
    team_var.set("Team 1")  # default value
    team_dropdown = tk.OptionMenu(mainwindow1, team_var, "Team 1", "Team 2")  # Add your teams here
    team_dropdown.grid(row=2, column=1)

    #Save and Load Buttons
    save_button = tk.Button(mainwindow1, text="Save Players", command=save_players)
    save_button.grid(row=4, column=0)

    load_button = tk.Button(mainwindow1, text="Load Players", command=load_players)
    load_button.grid(row=5, column=0)

    # Add Player button
    add_player_button = tk.Button(mainwindow1, text="Add Player", command=add_player)
    add_player_button.grid(row=4, column=1)

    # Initial posession player dropdown
    select_label = tk.Label(mainwindow1, text="Select initial player possession:")
    select_label.grid(row=6, column=0)

    player_var = tk.StringVar(mainwindow1)
    player_var.set("Select Player")  # default value
    player_names = [player._name for player in game.players]
    player_dropdown = tk.OptionMenu(mainwindow1, player_var, *player_names)
    player_dropdown.grid(row=6, column=1)
    
    #"Start Match!" button
    start_button = tk.Button(mainwindow1, text="Start Match!", command=start_match)
    start_button.grid(row=8, column=0)
    #endregion

    # Update the list of available players
    game.update_player_list()
#endregion
























#region ====Screen 3 (Main)====
def show_screen_3():
    global last_action_label
    clear_window()

    # Create a label to display the current player in possession
    current_player_label = tk.Label(mainwindow1, text=f"Current player in possession: {game.current_possession._name}")
    current_player_label.grid(row=0, column=0)

    # Create a label to display the last action
    last_action_label = tk.Label(mainwindow1, text=f"{game.message}")
    last_action_label.grid(row=1, column=0)

    # Create a text entry for the action code
    action_code_entry = tk.Entry(mainwindow1)
    action_code_entry.grid(row=2, column=0)

    # Create a button to input the action code
    input_action_button = tk.Button(mainwindow1, text="Input Action Code", command=input_action_code)  # You need to define input_action_code
    input_action_button.grid(row=2, column=1)

    # Create buttons for different actions
    dribble_button = tk.Button(mainwindow1, text="Dribble", command=game.dribble)  # You need to define dribble
    dribble_button.grid(row=3, column=0)

    pass_button = tk.Button(mainwindow1, text="Pass", command=show_screen_pass)  # You need to define show_screen_pass
    pass_button.grid(row=4, column=0)

    shoot_button = tk.Button(mainwindow1, text="Shoot", command=show_screen_shot)  # You need to define show_screen_shoot
    shoot_button.grid(row=5, column=0)

    turnover_button = tk.Button(mainwindow1, text="Turnover", command=show_screen_turnover)  # You need to define show_screen_turnover
    turnover_button.grid(row=6, column=0)

    foul_button = tk.Button(mainwindow1, text="Foul", command=show_screen_foul)  # You need to define show_screen_foul
    foul_button.grid(row=7, column=0)
#endregion


#=======Screen 5 (Pass)=======#
def show_screen_pass():
    pass
#=======Screen 6 (Shot)=======#
def show_screen_shot():
    pass
#=======Screen 6.a (Assist)=======#

#=======Screen 6.b (Rebound)=======#

#=======Screen 7 (Turnover)=======#   
def show_screen_turnover():
    pass

#=======Screen 8 (Foul)=======#
def show_screen_foul():
    pass
    

# Start with the main menu
show_main_menu()

# Run the application
mainwindow1.mainloop()


