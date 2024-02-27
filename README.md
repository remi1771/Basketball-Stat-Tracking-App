# Patch Notes

Version 0.02

## Changes and Additions

1. **Renaming:** Renamed `patch notes.md` to `README.md` so it's accesible as soon as you enter | renamed `to-do.md` to `todo.md` so it can work with a todo extension I have.
2. **Updated EasyButton Modulet Class Integration:** Updated `EasyButton` class directly to `WXtry.py` instead of having it as a separate module for troubleshooting purposes.
3. **Deleted unused/unnecessary files:** deleted `HowToGUI.py`, `players.pkl`



Version 0.01

-Created patch notes for further tracking commits and changes.

## Changes and Additions

1. **Icons Organization:** Moved Icons to a separate folder for better organization.
2. **EasyButton Class Integration:** Added the `EasyButton` class directly to `WXtry.py` instead of having it as a separate module for troubleshooting purposes.
3. **EasyButton Import Comment:** Added a comment to import the `EasyButton` module to avoid issues.
4. **Notebook UI Addition:** Added a notebook below the icons in the `MainFrame` class for better UI organization.
5. **New Button Feature:** Added a "new" button intended to create players and teams, allowing users to add new entities.
6. **Patch Notes Documentation:** Created patch notes for further tracking commits and changes, aiding in project organization and version tracking.
7. **Player Class Update:** Updated the `Player` class to include more attributes such as various attempts and made shots, passes, turnovers, steals, fouls, blocks, rebounds, etc.
8. **File Dialog Integration:** Updated the `FILE_LOAD` and `FILE_SAVE` methods in the `MainFrame` class to use a file dialog for loading and saving files.
9. **Button Creation in EasyButton:** Updated the `EasyButton` class to include a `create_button` method which creates a button with an icon and binds it to a method in the parent class.
10. **Player List Update Method:** The `MainFrame` class has been updated to include a `update_player_list` method which updates a list of players.
11. **Dribble Method in Game Class:** The `Game` class has been updated to include a `dribble` method which updates the current possession's dribbles and the last action.
12. **Player Addition Method:** The `Game` class has been updated to include an `add_player` method which adds a player to the game.
13. **Player List Update in Game Class:** The `Game` class has been updated to include an `update_player_list` method which updates a list of player information.