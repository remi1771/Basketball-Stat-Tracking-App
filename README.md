# Patch Notes

### Version 0.03
- **Updated `README.MD` for readability.**
- **Updated ``Todo.md``**
- **Deleted ``TestSaveFile`` and ``Methods.py``**
- **Updated some icons to optimize for space:** I think the whole thing is 1kb smaller now lol :)

### Version 0.02

* **Renaming:** Renamed `patch notes.md` to `README.md` so it's accesible as soon as you enter | renamed `to-do.md` to `todo.md` so it can work with a todo extension I have.
* **Updated EasyButton Modulet Class Integration:** Updated `EasyButton` class directly to `WXtry.py` instead of having it as a separate module for troubleshooting purposes.
* **Deleted unused/unnecessary files:** deleted `HowToGUI.py`, `players.pkl`



### Version 0.01
-Created patch notes for further tracking commits and changes.

* **Icons Organization:** Moved Icons to a separate folder for better organization.
- **EasyButton Class Integration:** Added the `EasyButton` class directly to `WXtry.py` instead of having it as a separate module for troubleshooting purposes.
- **EasyButton Import Comment:** Added a comment to import the `EasyButton` module to avoid issues.
- **Notebook UI Addition:** Added a notebook below the icons in the `MainFrame` class for better UI organization.
- **New Button Feature:** Added a "new" button intended to create players and teams, allowing users to add new entities.
- **Patch Notes Documentation:** Created patch notes for further tracking commits and changes, aiding in project organization and version tracking.
- **Player Class Update:** Updated the `Player` class to include more attributes such as various attempts and made shots, passes, turnovers, steals, fouls, blocks, rebounds, etc.
- **File Dialog Integration:** Updated the `FILE_LOAD` and `FILE_SAVE` methods in the `MainFrame` class to use a file dialog for loading and saving files.
- **Button Creation in EasyButton:** Updated the `EasyButton` class to include a `create_button` method which creates a button with an icon and binds it to a method in the parent class.
- **Player List Update Method:** The `MainFrame` class has been updated to include a `update_player_list` method which updates a list of players.
- **Dribble Method in Game Class:** The `Game` class has been updated to include a `dribble` method which updates the current possession's dribbles and the last action.
- **Player Addition Method:** The `Game` class has been updated to include an `add_player` method which adds a player to the game.
- **Player List Update in Game Class:** The `Game` class has been updated to include an `update_player_list` method which updates a list of player information.