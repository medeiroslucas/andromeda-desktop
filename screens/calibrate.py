import time
import threading
import tkinter as tk
import tkinter.font as tk_font

from utils import get_planets_dict
from tkinter import ttk
from PIL import Image, ImageTk


class CalibrateScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.selected_planet = None
        self.controller = controller
        self.running = True
        self.running_lock = threading.Lock()

        self.plantes_dict = get_planets_dict()
        self.plantes_list = self.plantes_dict.keys()

        self.create_screen()

    def create_screen(self):

        selecione_astro = tk.Label(self)
        ft = tk_font.Font(family='Times', size=18)
        selecione_astro["font"] = ft
        selecione_astro["fg"] = "#333333"
        selecione_astro["justify"] = "center"
        selecione_astro["text"] = "Selecione um astro visível\n como referência:"
        selecione_astro.place(x=70, y=70, width=260, height=50)

        planets = list(get_planets_dict().keys())
        planets_combo = ttk.Combobox(self, values=planets)
        ft = tk_font.Font(family='Times', size=15)
        planets_combo["font"] = ft
        planets_combo.set("Selecione um astro")
        planets_combo.pack(padx=5, pady=5)
        planets_combo.place(x=90, y=140, width=220, height=30)
        planets_combo.bind("<<ComboboxSelected>>", self.onselect)

        button_posicionar = tk.Button(self)
        button_posicionar["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=20)
        button_posicionar["font"] = ft
        button_posicionar["fg"] = "#000000"
        button_posicionar["justify"] = "center"
        button_posicionar["text"] = "Posicionar"
        button_posicionar.place(x=90, y=180, width=220, height=30)
        button_posicionar["command"] = self.button_visualizar_command

        button_finalizar = tk.Button(self)
        button_finalizar["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=34)
        button_finalizar["font"] = ft
        button_finalizar["fg"] = "#000000"
        button_finalizar["justify"] = "center"
        button_finalizar["text"] = "Finalizar"
        button_finalizar.place(x=70, y=350, width=320, height=65)
        button_finalizar["command"] = self.button_finalizar_command

        button_cancelar = tk.Button(self)
        button_cancelar["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=34)
        button_cancelar["font"] = ft
        button_cancelar["fg"] = "#000000"
        button_cancelar["justify"] = "center"
        button_cancelar["text"] = "Cancelar"
        button_cancelar.place(x=70, y=430, width=320, height=65)
        button_cancelar["command"] = self.button_visualizar_command

        button_arrow_up = tk.Button(self)
        button_arrow_up["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_up["font"] = ft
        button_arrow_up["fg"] = "#000000"
        button_arrow_up["justify"] = "center"
        button_arrow_up["text"] = "⮝"
        button_arrow_up.place(x=540, y=90, width=80, height=80)
        button_arrow_up["command"] = self.button_visualizar_command

        button_arrow_down = tk.Button(self)
        button_arrow_down["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_down["font"] = ft
        button_arrow_down["fg"] = "#000000"
        button_arrow_down["justify"] = "center"
        button_arrow_down["text"] = "⮟"
        button_arrow_down.place(x=540, y=320, width=80, height=80)
        button_arrow_down["command"] = self.button_visualizar_command

        button_arrow_right = tk.Button(self)
        button_arrow_right["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_right["font"] = ft
        button_arrow_right["fg"] = "#000000"
        button_arrow_right["justify"] = "center"
        button_arrow_right["text"] = "⮞"
        button_arrow_right.place(x=665, y=207, width=80, height=80)
        button_arrow_right["command"] = self.button_visualizar_command

        button_arrow_left = tk.Button(self)
        button_arrow_left["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=40)
        button_arrow_left["font"] = ft
        button_arrow_left["fg"] = "#000000"
        button_arrow_left["justify"] = "center"
        button_arrow_left["text"] = "⮜"
        button_arrow_left.place(x=415, y=207, width=80, height=80)
        button_arrow_left["command"] = self.button_visualizar_command

    def button_visualizar_command(self):
        self.running_lock.acquire()
        self.running = False
        self.running_lock.release()

        print("command")
        if self.selected_planet:
            print(f"Selected planet {self.selected_planet}")

    def button_finalizar_command(self):
        thr = threading.Thread(target=self.print_test, args=(), kwargs={})
        self.running_lock.acquire()
        self.running = True
        self.running_lock.release()

        thr.start()

    def print_test(self):
        while self.running:
            print("test")
            time.sleep(1)

        print("Out")

    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        planet = w.get()
        planet_name = self.plantes_dict[planet]
        self.selected_planet = planet_name
        print(f'You selected item: {planet_name}')
