import tkinter as tk
import tkinter.font as tk_font

from utils import get_planets_dict
from app.esp_adapter_mock import EspAdapterMock


class FreeMoveScreen(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.selected_planet = None
        self.controller = controller

        self.parent = parent
        self.plantes_dict = get_planets_dict()
        self.plantes_list = self.plantes_dict.keys()

        self.create_screen()

    def create_screen(self):

        selecione_astro = tk.Label(self)
        ft = tk_font.Font(family='Times', size=18)
        selecione_astro["font"] = ft
        selecione_astro["fg"] = "#333333"
        selecione_astro["justify"] = "center"
        selecione_astro["text"] = "Use as setas para movimentar\no telescópio"
        selecione_astro.place(x=50, y=120, width=300, height=50)

        button_finalizar = tk.Button(self)
        button_finalizar["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=34)
        button_finalizar["font"] = ft
        button_finalizar["fg"] = "#000000"
        button_finalizar["justify"] = "center"
        button_finalizar["text"] = "Finalizar"
        button_finalizar.place(x=40, y=250, width=320, height=65)
        button_finalizar["command"] = self.button_finalizar_command

        button_cancelar = tk.Button(self)
        button_cancelar["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=34)
        button_cancelar["font"] = ft
        button_cancelar["fg"] = "#000000"
        button_cancelar["justify"] = "center"
        button_cancelar["text"] = "Cancelar"
        button_cancelar.place(x=40, y=320, width=320, height=65)
        button_cancelar["command"] = self.button_cancelar_command

        button_arrow_up = tk.Button(self)
        button_arrow_up["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_up["font"] = ft
        button_arrow_up["fg"] = "#000000"
        button_arrow_up["justify"] = "center"
        button_arrow_up["text"] = "⮝"
        button_arrow_up.place(x=540, y=90, width=80, height=80)
        button_arrow_up["command"] = self.move_up

        button_arrow_down = tk.Button(self)
        button_arrow_down["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_down["font"] = ft
        button_arrow_down["fg"] = "#000000"
        button_arrow_down["justify"] = "center"
        button_arrow_down["text"] = "⮟"
        button_arrow_down.place(x=540, y=320, width=80, height=80)
        button_arrow_down["command"] = self.move_down

        button_arrow_right = tk.Button(self)
        button_arrow_right["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_right["font"] = ft
        button_arrow_right["fg"] = "#000000"
        button_arrow_right["justify"] = "center"
        button_arrow_right["text"] = "⮞"
        button_arrow_right.place(x=665, y=207, width=80, height=80)
        button_arrow_right["command"] = self.move_right

        button_arrow_left = tk.Button(self)
        button_arrow_left["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_left["font"] = ft
        button_arrow_left["fg"] = "#000000"
        button_arrow_left["justify"] = "center"
        button_arrow_left["text"] = "⮜"
        button_arrow_left.place(x=415, y=207, width=80, height=80)
        button_arrow_left["command"] = self.move_left

    def move_up(self):
        self.controller.dx += 1

    def move_down(self):
        self.controller.dx -= 1

    def move_left(self):
        self.controller.dy -= 1

    def move_right(self):
        self.controller.dy += 1

    def button_finalizar_command(self):

        self.controller.show_frame("HomeScreen")

    def button_cancelar_command(self):

        self.controller.dx = 0
        self.controller.dy = 0

        self.controller.show_frame("HomeScreen")
