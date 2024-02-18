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
        
        #Passes
        self._passes = 0
        self._attempted_passes = 0
        self._received_passes = 0
        self._received_passes_from = {}
        self._made_passes_to = {}
        self._assists = 0
        self._assists_made_to = {}

        #Shooting
        self._points = 0
        self._shots_made = 0
        self._shots_attempted = 0
        self._layups_attempts = 0
        self._layups_makes = 0
        self._two_point_attempts = 0
        self._two_point_makes = 0
        self._three_point_attempts = 0
        self._three_point_makes = 0
        
        #Hustle and Defense
        self._offensive_rebounds = 0
        self._defensive_rebounds = 0
        self._steals = 0
        self._interceptions = 0
        self._turnovers = 0
    
    def reset_stats(self):
        self._possessions = 0
        self._dribbles = 0
        self._passes = 0
        self._attempted_passes = 0
        self._received_passes = 0
        self._received_passes_from = {}
        self._made_passes_to = {}
        self._assists = 0
        self._assists_made_to = {}
        self._points = 0
        self._shots_made = 0
        self._shots_attempted = 0
        self._layups_attempts = 0
        self._layups_makes = 0
        self._two_point_attempts = 0
        self._two_point_makes = 0
        self._three_point_attempts = 0
        self._three_point_makes = 0
        self._offensive_rebounds = 0
        self._defensive_rebounds = 0
        self._steals = 0
        self._interceptions = 0
        self._turnovers = 0
    
    def __str__(self):
        return f"Player: {self._name}, Team: {self._team}, Number: {self._number}"
    
    def __eq__(self, other):
        if isinstance(other, Player):
            return self.__dict__ == other.__dict__
        return False

#I'm thinking of removing the class team alltogether, is it REALLY necessary?
#I mean, you can just get the stats calculated by hand, and it might make it so that you can't track stats on 1v1v1 or other weird mode that requires more than 2 teams.
#No but seriously what purpose does team have?
#Actually might be helpful to determine if rebounds are offensive or defensive huh

class Team:
    def __init__(self, name):
        self.name = name
        self.possessions = {}
        self.total_points = 0
        self.total_rebounds = 0
        
class Game:
    def __init__(self):
        self.current_possession = None
        self.players = []
        self.teams = [] #Was a dictionary changed it to index because teams should be numbers not names no one cares about names, lol
        
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

    def update_possession_label(self):
    current_player_label.config(text=f"Current Player in possession: {self.current_possession}")

    def set_current_possession(self, player):
        self.current_possession = player   
                   
    def select_player(self):
        pass #Here it should show all possible player, inside tkinter
        
    def dribble(self)
        self.current_possession.dribbles += 1
        message = f"{self.current_possession.name} dribbled ({self.current_possession.dribbles})."

    def passes()
        other_player_number = int(input("Input the number of the player who received the pass: "))
        other_player = next((p for p in self.players if p.number == other_player_number), None)
        if other_player is not None:
            other_player.received_passes_from[self.current_possession.number] = \
                other_player.received_passes_from.get(self.current_possession.number, 0) + 1

            # Increment the count in the made_passes_to dictionary for the current player
            self.current_possession.made_passes_to[other_player.number] = \
                self.current_possession.made_passes_to.get(other_player.number, 0) + 1

            # Increment the current player's possessions and passes count
            self.current_possession.possessions += 1
            self.current_possession.passes += 1
            self.current_possession.attempted_passes += 1

            self.current_possession = other_player
        break

    def turnover()
        self.current_possession.turnovers += 1
        pass #call a function to check for steals or interceptions
               
    def steal_check(self):
        pass #ask which player got the steal
        pass #change possession to player who got the steal
        pass #add +1 to steals to whoever stole the ball

    def interception_check(self):
        pass #ask which player got the steal
        pass #change possession to player who got the steal
        pass #add +1 to interception to whoever stole the ball
            
    def layup_attempt(self, player):
        player.possessions += 1
        player.shots_attempted +=1
        player.layups_attempts += 1

        pass #ask if player went in
        if made:
            player.shots_made +=1
            player.layups_makes += 1
            player.points +=2
            self.teams[player.team.name].total_points += 2
            self.assist_check(player)
        else:
            self.rebound_check()            
            
    def shoot_two_point_attempt(self, player):
        player.possessions += 1
        player.shots_attempted +=1
        player.two_point_attempts += 1

        made = input("Did the shot go in? (y/n) ").lower() == 'y'
        if made:
            player.shots_made +=1
            player.two_point_makes += 1
            player.points +=2
            self.teams[player.team.name].total_points += 2
            self.assist_check(player)
        else:
            self.rebound_check()
            
    def shoot_three_point_attempt(self, player):
        player.possessions += 1
        player.shots_attempted +=1
        player.three_point_attempts += 1

        made = input("Did the shot go in? (y/n) ").lower() == 'y'
        if made:
            player.shots_made +=1
            player.three_point_makes += 1
            player.points +=3
            self.teams[player.team.name].total_points += 3
            self.assist_check(player)
        else:
            self.rebound_check()
            
    def rebound_check(self):
        rebound = input("Input the number of the player who got the rebound, if none then simply state null: ").lower()
        if rebound != 'null':
            rebound_player_number = int(rebound)
            rebound_player = next((p for p in self.players if p.number == rebound_player_number), None)
            if rebound_player is not None:
                if self.current_possession.team == rebound_player.team:
                    rebound_player.offensive_rebounds += 1
                    self.current_possession = rebound_player
                else:
                    rebound_player.defensive_rebounds += 1
                    self.current_possession = rebound_player
        else:
            self.current_possession = None
                       
    def assist_check(self, player):
        assist = input("Input the number of the player who made the assist, if none then simply state null: ").lower()
        if assist != 'null':
            assist_player_number = int(assist)
            assist_player = next((p for p in self.players if p.number == assist_player_number), None)
            if assist_player is not None and assist_player != self.current_possession:
                assist_player.assists += 1
                assist_player.assists_made_to[self.current_possession.number] = assist_player.assists_made_to.get(self.current_possession.number, 0) + 1    
                
    def turnover(self, player):
        player.turnovers += 1
        player.possessions += 1
        self.current_possession = None
        self.steal_check()     


# Screen 1: Main Menu
def show_main_menu():
    clear_window()
    tk.Button(window, text="New Game", command=show_screen_2).pack()
    tk.Button(window, text="Load", command=load_file).pack()

# Screen 2: Game Screen
def show_screen_2():
    clear_window()
    global loaded_file_label, current_player_label
    loaded_file_label = tk.Label(window, text="File: None")
    loaded_file_label.pack()
    current_player_label = tk.Label(window, text="Current Player in possession:")
    current_player_label.pack()
    
    tk.Button(window, text="Dribble", command=dribble).pack()
    tk.Button(window, text="Pass", command=lambda: action_performed("Pass")).pack()
    tk.Button(window, text="Layup", command=lambda: action_performed("Layup")).pack()
    tk.Button(window, text="Shoot 2", command=lambda: action_performed("Shoot 2")).pack()
    tk.Button(window, text="Shoot 3", command=lambda: action_performed("Shoot 3")).pack()
    tk.Button(window, text="Turnover", command=lambda: action_performed("Turnover")).pack()
    tk.Button(window, text="Save", command=save_game).pack()

# Function to clear the window
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Function to load a file
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Spreadsheet files", "*.csv *.xlsx"), ("All files", "*.*")])
    if file_path:
        show_screen_2()
        loaded_file_label.config(text=f"File: {file_path}")

# Function to handle an action (like "Dribble", "Pass", etc.)
def action_performed(action):
    # Here you can add your logic to handle each action
    print(f"Action performed: {action}")

# Function to save the game
def save_game():
    # Here you can add your logic to save the game
    messagebox.showinfo("Save", "Game saved successfully (not really, just a placeholder).")

# Create the main window
window = tk.Tk()
window.title("Stat Tracking App")

# Start with the main menu
show_main_menu()

# Run the application
window.mainloop()




'''
---------------------------------------

To integrate the dribble function into the GUI, you would first need to adapt it to work in 
an event-driven environment like Tkinter, as opposed to the loop and keyboard checks in a console application.

Here's a simplified version of your dribble function adapted for the GUI:


class StatTracker: #que vendria a ser game en realidad
    def __init__(self, window):
        self.window = window
        self.current_possession = None  # You'll need to set this when a player is selected
        
        # ... other initialization code ...

    def select_player(self):
        # This method should allow the user to select a player
        # Placeholder for selecting a player - you will need to implement this
        pass

    def dribble(self):
        self.current_possession.dribbles += 1
        message = f"{self.current_possession.name} dribbled ({self.current_possession.dribbles})."
        print(message)  # You might want to update this to show the message in the GUI

    # ... other methods ...

# Example Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.dribbles = 0

# Then, in the GUI setup function, you would bind the dribble action to a button:

def show_screen_2(stat_tracker):
    clear_window()
    global loaded_file_label, current_player_label
    loaded_file_label = tk.Label(window, text="File: None")
    loaded_file_label.pack()
    current_player_label = tk.Label(window, text="Current Player in possession:")
    current_player_label.pack()
    
    # Dribble button with command linked to the dribble method of the stat tracker
    tk.Button(window, text="Dribble", command=stat_tracker.dribble).pack()

    # ... other buttons ...

# And when creating the StatTracker instance:
tracker = StatTracker(window)
show_screen_2(tracker)

# Remember to include the rest of the GUI setup and the main loop
In this adapted code, when the "Dribble" button is pressed in the GUI, it will call the dribble method of the StatTracker instance tracker. The dribble method will then check if there is a current player in possession and, if so, increment their dribble count and print the message. The Player class is a placeholder for whatever player object you're using to track stats.

Please note that the GUI version does not continuously check for key presses like the console version. Instead, it reacts to events (like button presses). Also, in a GUI application, you typically would not print to the console; you would update the GUI with new information, perhaps in a label or text box.'''
