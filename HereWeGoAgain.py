#Fuck My Life it's clear that I can't do cmd AND tkinter at the same time because i'm a shitty af programmer, so everything on tkinter it is which fucking sucks honestly because i'm not quite sure that tkinter has a getkey() functionality or something but oh well

import tkinter as tk
import pickle
from tkinter import filedialog
from tkinter import messagebox

#Variables!
window = tk.Tk()  # Create the main window
window.title("Stat Tracking App")

player_list_label = tk.Label(window) # Create a label to display the available players
player_list_label.pack()

last_action_label = None


#Functions!
def save_players():
    with open('players.pkl', 'wb') as output:
        pickle.dump(game.players, output, pickle.HIGHEST_PROTOCOL)

def load_players():
    with open('players.pkl', 'rb') as input:
        game.players = pickle.load(input)
    game.update_player_list()

# Function to clear the window
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Function to load a file PLACEHOLDER
def load_file():
    pass

# Function to save the game PLACEHOLDER
def save_game():
    pass

def input_action_code():
    pass

#Classes:
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
        global player_list_label
        player_info = [f"{player._name}({player._number}, {player._team})" for player in self.players]
        player_list_label.config(text="Available players: " + ", ".join(player_info)) 

game = Game()

#=======Screen 1 (Create or Load a game)=======#
def show_main_menu():
    clear_window()
    tk.Button(window, text="New Game", command=show_screen_2).pack()
    tk.Button(window, text="Load", command=load_file).pack()
#=======Screen 2 (Select Players)=======#
def show_screen_2():
    """
    Displays a screen where the user can input player information, such as name, number, and team.
    Provides a button to add the player to the game and updates the list of available players.
    """
    clear_window()
    
    # Create a label to display the available players
    global player_list_label
    player_list_label = tk.Label(window)
    player_list_label.grid(row=0, column=0)

    # Player name entry
    player_name_label = tk.Label(window, text="Player Name:")
    player_name_label.grid(row=1, column=0)
    player_name_entry = tk.Entry(window)
    player_name_entry.grid(row=2, column=0)

    # Player number entry
    player_number_label = tk.Label(window, text="Number:")
    player_number_label.grid(row=1, column=2)
    player_number_entry = tk.Entry(window)
    player_number_entry.grid(row=2, column=2)

    # Team selection dropdown
    team_label = tk.Label(window)
    team_label.grid(row=2, column=1)
    team_var = tk.StringVar(window)
    team_var.set("Select Team")  # default value
    team_dropdown = tk.OptionMenu(window, team_var, "Team 1", "Team 2")  # Add your teams here
    team_dropdown.grid(row=2, column=1)

    # Add Player button
    def add_player():
        """
        Retrieves the player's name, number, and team from the input fields.
        Creates a new Player object with the retrieved information.
        Adds the player to the game.
        Clears the input fields and resets the team dropdown to its default value.
        Updates the list of available players.
        """
        player_name = player_name_entry.get()
        player_number = player_number_entry.get()
        team = team_var.get()
        player = Player(player_name, team, player_number)
        game.add_player(player)
        print(f"Added player {player_name} with number {player_number} to {team}")

        # Clear the input fields
        player_name_entry.delete(0, 'end')
        player_number_entry.delete(0, 'end')
        team_var.set("Select Team")

        # Update the list of available players
        game.update_player_list()

    # Inside show_screen_2 function
    save_button = tk.Button(window, text="Save Players", command=save_players)
    save_button.grid(row=4, column=0)

    load_button = tk.Button(window, text="Load Players", command=load_players)
    load_button.grid(row=5, column=0)
    

    # Add Player button
    add_player_button = tk.Button(window, text="Add Player", command=add_player)
    add_player_button.grid(row=4, column=1)

    # To Match button
    to_match_button = tk.Button(window, text="Start Match!", command=show_screen_3)  # You need to define show_screen_3
    to_match_button.grid(row=5, column=1)

    # Update the list of available players
    game.update_player_list()

#=======Screen 3 (Pre-Game)=======#
def show_screen_3():
    clear_window()

    # Create a label for the dropdown
    select_label = tk.Label(window, text="Select initial player possession:")
    select_label.pack()

    # Create a dropdown menu with player options
    player_var = tk.StringVar(window)
    player_var.set("Select Player")  # default value
    player_names = [player._name for player in game.players]
    player_dropdown = tk.OptionMenu(window, player_var, *player_names)
    player_dropdown.pack()

    # Define the function to start the match and go to screen 4
    def start_match():
        selected_player_name = player_var.get()
        for player in game.players:
            if player._name == selected_player_name:
                game.current_possession = player
                print(game.current_possession)
                break
        show_screen_4()  # You need to define show_screen_4

    # Create a "Start Match!" button
    start_button = tk.Button(window, text="Start Match!", command=start_match)
    start_button.pack()
    
#=======Screen 4 (Main)=======#
def show_screen_4():
    global last_action_label
    clear_window()

    # Create a label to display the current player in possession
    current_player_label = tk.Label(window, text=f"Current player in possession: {game.current_possession._name}")
    current_player_label.grid(row=0, column=0)

    # Create a label to display the last action
    last_action_label = tk.Label(window, text=f"{game.message}")
    last_action_label.grid(row=1, column=0)

    # Create a text entry for the action code
    action_code_entry = tk.Entry(window)
    action_code_entry.grid(row=2, column=0)

    # Create a button to input the action code
    input_action_button = tk.Button(window, text="Input Action Code", command=input_action_code)  # You need to define input_action_code
    input_action_button.grid(row=2, column=1)

    # Create buttons for different actions
    dribble_button = tk.Button(window, text="Dribble", command=game.dribble)  # You need to define dribble
    dribble_button.grid(row=3, column=0)

    pass_button = tk.Button(window, text="Pass", command=show_screen_pass)  # You need to define show_screen_pass
    pass_button.grid(row=4, column=0)

    shoot_button = tk.Button(window, text="Shoot", command=show_screen_shot)  # You need to define show_screen_shoot
    shoot_button.grid(row=5, column=0)

    turnover_button = tk.Button(window, text="Turnover", command=show_screen_turnover)  # You need to define show_screen_turnover
    turnover_button.grid(row=6, column=0)

    foul_button = tk.Button(window, text="Foul", command=show_screen_foul)  # You need to define show_screen_foul
    foul_button.grid(row=7, column=0)

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
window.mainloop()



