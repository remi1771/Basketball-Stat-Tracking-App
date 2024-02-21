import wx

app = wx.App(False)

# Create a frame
frame = wx.Frame(None, wx.ID_ANY, "Hello World")

# Load your icons
icon1 = wx.Bitmap('DCAT.ICO', wx.BITMAP_TYPE_ANY)
icon2 = wx.Bitmap('DCAT.ICO', wx.BITMAP_TYPE_ANY)
icon3 = wx.Bitmap('DCAT.ICO', wx.BITMAP_TYPE_ANY)
icon4 = wx.Bitmap('DCAT.ICO', wx.BITMAP_TYPE_ANY)
icon5 = wx.Bitmap('DCAT.ICO', wx.BITMAP_TYPE_ANY)

# Create buttons
button1 = wx.BitmapButton(frame, id=wx.ID_ANY, bitmap=icon1)
button2 = wx.BitmapButton(frame, id=wx.ID_ANY, bitmap=icon2)
button3 = wx.BitmapButton(frame, id=wx.ID_ANY, bitmap=icon3)
button4 = wx.BitmapButton(frame, id=wx.ID_ANY, bitmap=icon4)
button5 = wx.BitmapButton(frame, id=wx.ID_ANY, bitmap=icon5)

# Create a box sizer
sizer = wx.BoxSizer(wx.HORIZONTAL)

# Add buttons to the sizer
sizer.Add(button1, 0, wx.ALL, 5)
sizer.Add(button2, 0, wx.ALL, 5)
sizer.Add(button3, 0, wx.ALL, 5)
sizer.Add(button4, 0, wx.ALL, 5)
sizer.Add(button5, 0, wx.ALL, 4)

# Set the sizer
frame.SetSizer(sizer)

# Show the frame
frame.Show(True)

# Start the application
app.MainLoop()