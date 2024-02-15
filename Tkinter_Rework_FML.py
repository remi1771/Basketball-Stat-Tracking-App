#Fuck My Life it's clear that I can't do cmd AND tkinter at the same time because i'm a shitty af programmer, so everything on tkinter it is which fucking sucks honestly because i'm not quite sure that tkinter has a getkey() functionality or something but oh well

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


#Classes:
class Player:
    def __init__(self, name, team, number):
        self.name = name
        self.team = team
        self.number = number
        self.possessions = 0
        self.dribbles = 0
        
        #Passes
        self.passes = 0
        self.attempted_passes = 0
        self.received_passes = 0
        self.received_passes_from = {}
        self.made_passes_to = {}
        self.assists = 0
        self.assists_made_to = {}

        #Shooting
        self.points = 0
        self.shots_made = 0
        self.shots_attempted = 0
        self.layups_attempts = 0
        self.layups_makes = 0
        self.two_point_attempts = 0
        self.two_point_makes = 0
        self.three_point_attempts = 0
        self.three_point_makes = 0
        
        #Hustle and Defense
        self.offensive_rebounds = 0
        self.defensive_rebounds = 0
        self.steals = 0
        self.interceptions = 0
        self.turnovers = 0

#I'm thinking of removing the class team alltogether, is it REALLY necessary?
#I mean, you can just get the stats calculated by hand, and it might make it so that you can't track stats on 1v1v1 or other weird mode that requires more than 2 teams.
#No but seriously what purpose does team have?
#Actually might be helpful to determine if rebounds are offensive or defensive huh

class Team:
    def __init__(self, name):
        self.name = name
        self.possessions = {}
        self.total_points = 0
        
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
        
    #Print Stats functions    
    def start(self):
        self.update_gui()
        self.root.mainloop()

    #this will def get yeeted
    def get_stats_text(self):
        # Prepare the stats text
        stats_lines = [
            "Player Stats:",
            "=======================================================================================================================================================================================================",
            "PLAYER  |  POINTS  |  ASSISTS  |  STEALS  |  TURNOVERS  |  POSSESSIONS  |  FGA  |  FGM  |  2PM  |  2PA  |  3PM  |  3PA  |  Lym  |  LyA  |  PASSESS  |  OFFREB  |  DEFREB  |  INTERCEPTIONS  |  DRIBBLES",
            "=======================================================================================================================================================================================================",
        ]
        
        for player in self.players:
            player_stats = f"{player.name} | {player.points} | {player.assists} | {player.steals} | {player.turnovers} | {player.possessions} | {player.shots_made} | {player.shots_attempted} | {player.two_point_makes} | {player.two_point_attempts} | {player.three_point_makes} | {player.three_point_attempts} | {player.layups_makes} | {player.layups_attempts} | {player.passes} | {player.offensive_rebounds} | {player.defensive_rebounds} | {player.interceptions} | {player.dribbles}"
            stats_lines.append(player_stats)
            stats_lines.append("________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

        stats_lines.append("\nTeam Stats:")
        for team_name, team in self.teams.items():
            team_stats = f"Team: {team.name}, Total Points: {team.total_points}"
            stats_lines.append(team_stats)
        
        stats_text = "\n".join(stats_lines)
        return stats_text

    def update_gui(self):
        self.stats_display.update_stats(self.get_stats_text())
        # Schedule the update_gui method to run in the future using the 'after' method
        self.root.after(1000, self.update_gui)
        
         
    #Pre-Game Functions
         
    def set_current_possession(self, player):
        self.current_possession = player   
                   
    def select_player(self):
        print("Select a player for possession:")
        for i, player in enumerate(self.players):
            print(f"{i+1}. {player.name} (#{player.number})")
        player_number = int(input("Enter the number of the player: ")) - 1

        # Check if the player number is valid
        if 0 <= player_number < len(self.players):
            self.current_possession = self.players[player_number]
        else:
            print("Invalid player number.")

    #In-Game functions
    def dribble(self)
        self.current_possession.dribbles += 1
        message = f"{self.current_possession.name} dribbled ({self.current_possession.dribbles})."
        
    def input_action(self):
        message = ""
        if self.current_possession is None:
            print("No player in possession. Please select a player.")
            self.select_player()
            if self.current_possession is None:  # Check again after trying to select a player
                return
                
        while True:
            try:
                key_pressed = keyboard.read_key().lower()
                if key_pressed == 'd':

                    keyboard.read_key()
                    break
                
                elif key_pressed == 'P':
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
            
                elif key_pressed == '1':
                    self.layup_attempt(self.current_possession)
                    break
                
                elif key_pressed == '2':
                    self.shoot_two_point_attempt(self.current_possession)
                    break
                 
                elif key_pressed == '3':
                    self.shoot_three_point_attempt(self.current_possession)
                    break
                    
                elif key_pressed == 'x':
                    self.current_possession.turnovers += 1
                    self.turnover(self.current_possession)
                    break

                elif key_pressed == 'q':
                    print("Game over.")
                    return 'quit'  # Return a special value to signal the end of the game
                    break


            except Exception as e:
                # Handle exceptions, if any
                print(f"An error occurred: {e}")
                break  # Break the loop if there is an error

        self.clear_screen()
        self.print_stats()
        print(message)
               
    def steal_check(self):
        steals = input("Input the number of the player who got the steal, if none (or interception) then simply state null: ").lower()
        if steals != 'null':
            steals_player_number = int(steals)
            steals_player = next((p for p in self.players if p.number == steals_player_number), None)
            if steals_player is not None:
                steals_player.steals += 1
                self.current_possession = steals_player
        else:
            self.interception_check()
            
    def interception_check(self):
        interception = input("Input the number of the player who got the interception, if none then simply state null: ").lower()
        if interception != 'null':
            interception_player_number = int(interception)
            interception_player = next((p for p in self.players if p.number == interception_player_number), None)
            if interception_player is not None:
                interception_player.interceptions += 1
                self.current_possession = interception_player
        else:
            self.current_possession = None
            
    def layup_attempt(self, player):
        player.possessions += 1
        player.shots_attempted +=1
        player.layups_attempts += 1

        made = input("Did the shot go in? (y/n) ").lower() == 'y'
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
    
    tk.Button(window, text="Dribble", command=lambda: action_performed("Dribble")).pack()
    tk.Button(window, text="Dribble", command=stat_tracker.dribble).pack()
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
