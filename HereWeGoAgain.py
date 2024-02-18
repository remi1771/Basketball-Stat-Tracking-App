#Fuck My Life it's clear that I can't do cmd AND tkinter at the same time because i'm a shitty af programmer, so everything on tkinter it is which fucking sucks honestly because i'm not quite sure that tkinter has a getkey() functionality or something but oh well

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Stat Tracking App")


def save_players():
    # Code to save players goes here
    pass

def load_players():
    # Code to load players goes here
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

    def update_player_list(self):
        global player_list_label
        player_info = [f"{player._name}({player._number}, {player._team})" for player in self.players]
        player_list_label.config(text="Available players: " + ", ".join(player_info)) 

game = Game()

# Screen 1: Main Menu
def show_main_menu():
    clear_window()
    tk.Button(window, text="New Game", command=show_screen_2).pack()
    tk.Button(window, text="Load", command=load_file).pack()

def show_screen_2():
    """
    Displays a screen where the user can input player information, such as name, number, and team.
    Provides a button to add the player to the game and updates the list of available players.
    """
    clear_window()
    
    # Create a label to display the available players
    player_list_label = tk.Label(window)
    player_list_label.grid(row=0, column=0)

    # Player name entry
    player_name_label = tk.Label(window, text="Player Name:")
    player_name_label.grid(row=0, column=0)
    player_name_entry = tk.Entry(window)
    player_name_entry.grid(columnspan=1, row=0, column=1)

    # Player number entry
    player_number_label = tk.Label(window, text="Number:")
    player_number_label.grid(row=0, column=2)
    player_number_entry = tk.Entry(window)
    player_number_entry.grid(row=0, column=3)

    # Team selection dropdown
    team_label = tk.Label(window, text="Team:")
    team_label.grid(row=1, column=1)
    team_var = tk.StringVar(window)
    team_var.set("Select Team")  # default value
    team_dropdown = tk.OptionMenu(window, team_var, "Team 1", "Team 2")  # Add your teams here
    team_dropdown.grid(row=1, column=2)

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

    # Add Player button
    add_player_button = tk.Button(window, text="Add Player", command=add_player)
    add_player_button.grid(row=3, column=3)

    # Inside show_screen_2 function
    save_button = tk.Button(window, text="Save Players", command=save_players)
    save_button.grid(row=3, column=1)

    load_button = tk.Button(window, text="Load Players", command=load_players)
    load_button.grid(row=3, column=2)

    # To Match button
    to_match_button = tk.Button(window, text="To Match!", command=show_screen_3)  # You need to define show_screen_3
    to_match_button.grid(row=4, column=2)

    # Update the list of available players
    game.update_player_list()




# Create a label to display the available players
player_list_label = tk.Label(window)
player_list_label.pack()


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




# Start with the main menu
show_main_menu()

# Run the application
window.mainloop()



