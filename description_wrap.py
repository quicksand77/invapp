__author__ = 'quicksand77'
########## resizing text box

import tkinter as tk

class ResizableText:
    def __init__(self, text_max_width=20):
        self.text_width = text_max_width
        self.root = tk.Tk()

        self.text = tk.Text(self.root, width=self.text_width, height=1)
        self.text.pack(expand=True)

        self.text.bind("<Key>", self.check_key)
        self.text.bind("<KeyRelease>", self.update_width)

        self.root.mainloop()

    def check_key(self, event):
        # Ignore the 'Return' key
        if event.keysym == "Return":
            return "break"

    def update_width(self, event):
        # Get text content; ignore the last character (always a newline)
        text = self.text.get(1.0, tk.END)[:-1]
        # CALCULATE needed number of lines (=height)
        lines = (len(text)-1) // self.text_width + 1
        # Apply changes on the widget
        self.text.configure(height=lines)