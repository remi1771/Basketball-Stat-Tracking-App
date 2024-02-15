import tkinter as tk
from tkinter import scrolledtext
import time

class StatsDisplayTk:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Stats")

        # Create a scrolled text widget to display the stats
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=30)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.config(state=tk.DISABLED)  # Make the text read-only
        self.stats_text = ""

    def update_stats(self, stats_text):
        self.stats_text += stats_text

    def run(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def update_gui(self):
        # Update the text in the scrolled text widget with the new stats
        self.text_area.config(state=tk.NORMAL)  # Enable text editing to update the stats
        self.text_area.delete('1.0', tk.END)  # Clear the current content
        self.text_area.insert(tk.INSERT, self.stats_text)  # Insert the new stats
        self.text_area.config(state=tk.DISABLED)  # Disable text editing again
        self.stats_text = ""
        self.root.after(1000, self.update_gui)

    def close(self):
        # Close the Tkinter window
        self.root.destroy()