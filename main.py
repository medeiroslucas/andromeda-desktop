import tkinter as tk
from screens.home import HomeScreen


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


if __name__ == "__main__":
    root = tk.Tk()
    HomeScreen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
