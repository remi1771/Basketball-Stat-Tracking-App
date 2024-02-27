import wx

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


#finally