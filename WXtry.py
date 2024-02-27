#Fuck My Life it's clear that I can't do cmd AND tkinter at the same time because i'm a shitty af programmer, so everything on tkinter it is which fucking sucks honestly because i'm not quite sure that tkinter has a getkey() functionality or something but oh well
#This is it boys :D


import pickle
import wx
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from easyButtons import * #because fuck you, that's why no need to do shit complicated
#I SPENT SO MUCH FUCKING TIME ON CREATING EASYBUTTONS BUT NOW IT WORKS FUCK YEAAAAAA

#region Classes:

class EasyButton:
    def __init__(self, parent, name, hpos=0, vpos=0, enabled=True):
        self.parent = parent
        self.name = name
        self.hpos = hpos
        self.vpos = vpos
        self.enabled = enabled
        self.create_button()

    def create_button(self):
        ICON = wx.Bitmap(f'ICONS/{self.name}.ICO')
        self.button = wx.BitmapButton(self.parent, bitmap=ICON, style=0)
        self.button.SetToolTip(self.name.replace('_', ' ').title())
        Sizer = self.parent.GetSizer()
        Sizer.Add(self.button, pos=wx.GBPosition(self.vpos, self.hpos))
        self.button.Bind(wx.EVT_BUTTON, getattr(self.parent, self.name))
        self.button.Enable(self.enabled)
        
class MainFrame(wx.Frame):
    def __init__(self, parent):

        horizontal_size = 376
        vertical_size = 218

        wx.Frame.__init__(self, parent, title = "Basketball Stat Tracking App by Remi1771", size = wx.Size(horizontal_size,vertical_size))
        
        #self.SetMinSize((horizontal_size, vertical_size)) #minimum size, duh
        #self.SetMaxSize((horizontal_size, -1)) #maximum size, 500 is the max width, 10000 is a large number for height

        self.Sizer = wx.GridBagSizer(1, 0)
 
        #EasyButton(self, 'NAME OF BUTTON, ICON, AND ALL', HPOS DEFAULTS TO 0, VPOS DEFAULTS TO 0, ENABLED DEFAULTS TO TRUE)
        EasyButton(self, 'FILE_LOAD')
        EasyButton(self, 'FILE_SAVE', 1)
        EasyButton(self, 'PLAYERS', 2)
        EasyButton(self, 'SHOT', 3, enabled=False)
        EasyButton(self, 'PASSING', 4, enabled=False)
        EasyButton(self, 'TURNOVER', 5)
        EasyButton(self, 'FOUL', 6)
        EasyButton(self, 'NEW', 7)
        EasyButton(self, 'SETTINGS', 8)

        self.notebook = wx.Notebook(self)
        self.page1 = wx.Window(self.notebook)
        self.page2 = wx.Window(self.notebook)
        self.notebook.AddPage(self.page1, "Teams")
        self.notebook.AddPage(self.page2, "Players")

        page1_sizer = wx.GridBagSizer(1, 0)
        self.page1.SetSizer(page1_sizer)

        
        self.Sizer.Add(self.notebook, pos=(1, 0), span=wx.GBSpan(1, 9), flag=wx.EXPAND)

        self.SetSizer(self.Sizer)
        self.page1.Layout()
        self.Layout() #This line asks the window to re-layout its components.
        self.Centre(wx.BOTH) #centers the window on the screen

        def update_player_list(self, players):
            self.player_list.Clear()
            for player in players:
                self.player_list.Append(player._name)

    #region DEF
    def NEW(self, event):
        print("Add button clicked")

    def PLAYERS(self,event):
        print("Players :D")

    def FILE_LOAD(self, event):
        dialog = wx.FileDialog(self, "Choose a file", "", "", "*.*", wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            filename = dialog.GetPath()
            with open(filename, 'rb') as f:
                return pickle.load(f)
        dialog.Destroy()

    def FILE_SAVE(self, event):
        dialog = wx.FileDialog(self, "Choose a file", "", "", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dialog.ShowModal() == wx.ID_OK:
            filename = dialog.GetPath()
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        dialog.Destroy()

    def SHOT(self, event):
        pass

    def PASSING(self, event):
        pass

    def TURNOVER(self, event):
        pass

    def FOUL(self, event):
        pass

    def SETTINGS(self, event):
        pass
    #endregion

class Player:
    def __init__(self, name, team, number):
        self._name = name
        self._team = team
        self._number = number
        self._possession = 0
        self._dribbles = 0
        self._shot_attempts = 0
        self._shot_made = 0
        self._layup_attempts = 0
        self._layup_made = 0
        self._2pt_attempts = 0
        self._2pt_made = 0
        self._3pt_attempts = 0
        self._3pt_made = 0
        self._pass_attempt = 0
        self._pass_made = 0
        self._turnovers = 0
        self._steals = 0
        self._fouls = 0
        self._blocks = 0
        self._offensive_rebounds = 0
        self._defensive_rebounds = 0
        self_total_rebounds = 0

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


app = wx.App()
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()


