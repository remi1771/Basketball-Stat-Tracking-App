
import os
import subprocess
import keyboard
from stats_display_tk import StatsDisplayTk

class Player:
    def __init__(self, name, team, number):
        self.name = name
        self.team = team
        self.number = number
        self.possessions = 0
        self.passes = 0
        
        self.attempted_passes = 0
        self.received_passes = 0
        
        self.received_passes_from = {}
        self.made_passes_to = {}
        
        self.dribbles = 0
        self.shots_made = 0
        self.shots_attempted = 0
        self.turnovers = 0
        self.layups_attempts = 0
        self.layups_makes = 0
        self.two_point_attempts = 0
        self.two_point_makes = 0
        self.three_point_attempts = 0
        self.three_point_makes = 0
        self.offensive_rebounds = 0
        self.defensive_rebounds = 0
        self.steals = 0
        self.interceptions = 0
        self.assists = 0
        self.assists_made_to = {}
        self.points = 0
class Team:
    def __init__(self, name):
        self.name = name
        self.possessions = {}
        self.total_points = 0

class Game:
    def __init__(self):
        self.current_possession = None
        self.players = []
        self.teams = {}
        self.stats_display = StatsDisplayTk()
        self.stats_display.run()
        
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
        
    #Main Console GUI functions

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')        
 
        
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
    def input_action(self):
        message = ""
        if self.current_possession is None:
            print("No player in possession. Please select a player.")
            self.select_player()
            if self.current_possession is None:  # Check again after trying to select a player
                return

        print("Press 'D' for Dribble\nPress 'P' for Pass\nPress '1' for Layup\nPress '2' for Shoot 2\nPress '3' for Shoot 3\nPress 'x' for Turnover\nPress 'Q' to Quit")

        # We will use a loop to continuously check for key presses
        while True:
            try:
                key_pressed = keyboard.read_key().lower()
                if key_pressed == 'd':
                    self.current_possession.dribbles += 1
                    message = f"{self.current_possession.name} dribbled ({self.current_possession.dribbles})."
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
   
game = Game()
team1 = Team("Team 1")
team2 = Team("Team 2")

# Create an instance of the Player class for "John Doe" on team1 with number 39
john_doe = Player("John Doe", team2, 39)
player1 = Player("Player 1", team1,1)
player2 = Player("Player 2", team1,2)
player3 = Player("Player 3", team2,1)

game.add_team(team1)
game.add_team(team2)
game.add_player(player1)
game.add_player(player2)
game.add_player(player3)
game.add_player(john_doe)

while True:
    result = game.input_action()  # Call input_action which now includes the prompt
    
    if result == 'quit':  # Check if input_action returned the 'quit' signal
        game.stats_display.close()
        break
    elif result == 'stats':  # Add this condition to print stats
        game.print_stats()
        
game.stats_display.run()
