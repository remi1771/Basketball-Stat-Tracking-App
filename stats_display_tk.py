# stats_display_tk.py

import tkinter as tk
from tkinter import scrolledtext

class StatsDisplayTk:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Stats")

        # Create a scrolled text widget to display the stats
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=30)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.config(state=tk.DISABLED)  # Make the text read-only

    def update_stats(self, stats_text):
        # Update the text in the scrolled text widget with the new stats
        self.text_area.config(state=tk.NORMAL)  # Enable text editing to update the stats
        self.text_area.delete('1.0', tk.END)  # Clear the current content
        self.text_area.insert(tk.INSERT, stats_text)  # Insert the new stats
        self.text_area.config(state=tk.DISABLED)  # Disable text editing again

    def run(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def close(self):
        # Close the Tkinter window
        self.root.destroy()