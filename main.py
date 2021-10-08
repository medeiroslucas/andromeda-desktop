import tkinter as tk
from screens.home import HomeScreen
from screens.calibrate import CalibrateScreen
from screens.free_move import FreeMoveScreen
from app.esp_adapter_mock import EspAdapterMock
from app.esp_adapter import EspAdapter

from setting import APP_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, BLUETOOTH_MODE


class MainApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        if BLUETOOTH_MODE == "MOCK":
            self.esp = EspAdapterMock()
        else:
            self.esp = EspAdapter()

        self.lat, self.long = self.esp.get_location()
        self.dx = 0
        self.dy = 0

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # setting title
        self.title(APP_TITLE)

        width = SCREEN_WIDTH
        height = SCREEN_HEIGHT
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.main_menu = tk.Menu(self)
        self.main_menu.add_command(label="Home", command=lambda: self.show_frame("HomeScreen"))
        self.main_menu.add_command(label="Calibrar", command=lambda: self.show_frame("CalibrateScreen"))
        self.main_menu.add_command(label="Mover Livremente", command=lambda: self.show_frame("FreeMoveScreen"))
        self.main_menu.add_command(label="Exit", command=self.destroy)

        self.config(menu=self.main_menu)

        self.frames = {}

        for f in (CalibrateScreen, HomeScreen, FreeMoveScreen):
            page_name = f.__name__
            frame = f(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CalibrateScreen")

    def show_frame(self, page_name):
        """
        Show a frame for the given page name
        """
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":

    app = MainApplication()
    app.mainloop()
