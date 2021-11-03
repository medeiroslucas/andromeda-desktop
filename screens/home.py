import threading
import time

import tkinter as tk
import tkinter.font as tk_font

from utils import get_planets_dict
from PIL import ImageTk, Image
from app.coordenates import get_planet_coord
from setting import MIN_DEG_ALT, MIN_DEG_AZ


class HomeScreen(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.selected_planet = None
        self.controller = controller

        self.positioning = False
        self.positioning_lock = threading.Lock()

        self.parent = parent
        self.plantes_dict = get_planets_dict()
        self.plantes_list = self.plantes_dict.keys()

        self.create_screen()

    def create_screen(self):

        planets_listbox = tk.Listbox(self)
        for planet in self.plantes_list:
            planets_listbox.insert(tk.END, planet)
        planets_listbox.pack()
        planets_listbox.place(x=70, y=110, width=220, height=380)
        planets_listbox.bind('<<ListboxSelect>>', self.onselect)

        selecione_astro = tk.Label(self)
        ft = tk_font.Font(family='Times', size=18)
        selecione_astro["font"] = ft
        selecione_astro["fg"] = "#333333"
        selecione_astro["justify"] = "center"
        selecione_astro["text"] = "Selecione um astro"
        selecione_astro.place(x=70, y=70, width=220, height=38)

        self.label_img = tk.Label(self)
        ft = tk_font.Font(family='Times', size=10)
        self.label_img["font"] = ft
        self.label_img["fg"] = "#333333"
        self.label_img["justify"] = "center"
        self.label_img["text"] = ""
        self.label_img.place(x=380, y=110, width=330, height=208)

        button_visualizar = tk.Button(self)
        button_visualizar["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=34)
        button_visualizar["font"] = ft
        button_visualizar["fg"] = "#000000"
        button_visualizar["justify"] = "center"
        button_visualizar["text"] = "Visualizar"
        button_visualizar.place(x=390, y=350, width=320, height=65)
        button_visualizar["command"] = self.visualizar_button_action

        button_ajuste_fino = tk.Button(self)
        button_ajuste_fino["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=34)
        button_ajuste_fino["font"] = ft
        button_ajuste_fino["fg"] = "#000000"
        button_ajuste_fino["justify"] = "center"
        button_ajuste_fino["text"] = "Ajuste Fino"
        button_ajuste_fino.place(x=390, y=430, width=320, height=65)
        button_ajuste_fino["command"] = self.ajuste_fino_button_action

    def visualizar_button_action(self):

        if not self.selected_planet or self.positioning:
            return

        thr = threading.Thread(target=self.position_planet, args=(), kwargs={}, daemon=True)
        self.positioning_lock.acquire()
        self.positioning = True
        self.positioning_lock.release()

        thr.start()

    def position_planet(self):

        while self.positioning:
            coord = get_planet_coord(self.selected_planet, self.controller.lat, self.controller.long)
            az = float(coord.az.deg) + MIN_DEG_AZ * self.controller.dx
            alt = float(coord.alt.deg) + MIN_DEG_ALT * self.controller.dy
            print(f"Az: {az}, Alt: {alt} - dx: {self.controller.dx}, dy: {self.controller.dy}")
            self.controller.esp.send_coord(az, alt)
            time.sleep(1)

    def ajuste_fino_button_action(self):
        self.controller.show_frame("FreeMoveScreen")

    def onselect(self, evt):

        if self.positioning:
            self.positioning_lock.acquire()
            self.positioning = False
            self.positioning_lock.release()

        w = evt.widget
        index = int(w.curselection()[0])
        planet = w.get(index)
        planet_name = self.plantes_dict[planet]
        self.selected_planet = planet_name
        print(f'Planeta selecionado: {planet_name}')

        fixed_height = 210

        img = Image.open(f"imgs/{planet_name}.png")

        height_percent = (fixed_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_percent)))

        resized_image = img.resize((width_size, fixed_height), Image.NEAREST)

        new_image = ImageTk.PhotoImage(resized_image)

        self.label_img.configure(image=new_image)
        self.label_img.image = new_image
