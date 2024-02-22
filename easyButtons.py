import wx

class EasyButton:
    def __init__(self, parent, name, vpos, hpos):
        self.parent = parent
        self.name = name
        self.vpos = vpos
        self.hpos = hpos
        self.create_button()

    def create_button(self):
        ICON = wx.Bitmap(f'{self.name}.ICO')
        self.button = wx.BitmapButton(self.parent, bitmap=ICON, style=0)
        self.button.SetToolTip(self.name.upper())
        Sizer = self.parent.GetSizer()
        Sizer.Add(self.button, pos=wx.GBPosition(self.vpos, self.hpos))
        self.button.Bind(wx.EVT_BUTTON, getattr(self.parent, self.name))


#finally