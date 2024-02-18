#Fuck My Life it's clear that I can't do cmd AND tkinter at the same time because i'm a shitty af programmer, so everything on tkinter it is which fucking sucks honestly because i'm not quite sure that tkinter has a getkey() functionality or something but oh well

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


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

    def dribble(self):
        self.current_possession.dribbles += 1
        message = f"{self.current_possession.name} dribbled ({self.current_possession.dribbles})."
        self.Last_action_player = self.current_possession
        self.Last_action_type = 'Dribbled'
        self.action_history.append({'player': self.current_possession, 'action': self.Last_action_type}) #If there's issues change  self.Last_action_type to 'Dribbled'



    def add_team(self, team):
        self.teams[team.name] = team
        
    def add_player(self, player):
        self.players.append(player)
        if player.team.name not in self.teams:
            print(f"Error: Team {player.team.name} not found in game teams.")
            return
        # Add the player to the team's list of players
        player_team = self.teams[player.team.name]
        if not hasattr(player_team, 'players'):
            player_team.players = []
        player_team.players.append(player)

        


# Screen 1: Main Menu
def show_main_menu():
    clear_window()
    tk.Button(window, text="New Game", command=show_screen_2).pack()
    tk.Button(window, text="Load", command=load_file).pack()

# Screen 2: Input Player
def show_screen_2():
    clear_window()
    
    # Player name entry
    tk.Label(window, text="Player Name:").pack()
    player_name_entry = tk.Entry(window)
    player_name_entry.pack()

    # Player number entry
    tk.Label(window, text="Player Number:").pack()
    player_number_entry = tk.Entry(window)
    player_number_entry.pack()

    # Team selection dropdown
    tk.Label(window, text="Team:").pack()
    team_var = tk.StringVar(window)
    team_var.set("Select Team")  # default value
    team_dropdown = tk.OptionMenu(window, team_var, "Team 1", "Team 2", "Team 3")  # Add your teams here
    team_dropdown.pack()

    # Add Player button
    def add_player():
        player_name = player_name_entry.get()
        player_number = player_number_entry.get()
        team = team_var.get()
        # Here you can add the code to create a new Player instance with the entered data
        print(f"Added player {player_name} with number {player_number} to {team}")

    add_player_button = tk.Button(window, text="Add Player", command=add_player)
    add_player_button.pack()

    # To Match button
    to_match_button = tk.Button(window, text="To Match!", command=show_screen_3)  # You need to define show_screen_3
    to_match_button.pack()

# Screen 3: Initial Posession
def show_screen_3():
    clear_window()

    

# Function to clear the window
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Function to load a file
def load_file():
    pass


# Function to save the game
def save_game():
    pass


# Create the main window
window = tk.Tk()
window.title("Stat Tracking App")

# Start with the main menu
show_main_menu()

# Run the application
window.mainloop()



