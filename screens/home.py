import tkinter as tk
import tkinter.font as tk_font

from setting import SCREEN_HEIGHT, SCREEN_WIDTH, APP_TITLE
from utils import get_planets_dict
from PIL import ImageTk, Image


class HomeScreen(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.selected_planet = None
        self.controller = controller

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
        button_visualizar["command"] = self.button_visualizar_command

        button_ajuste_fino = tk.Button(self)
        button_ajuste_fino["bg"] = "#efefef"
        ft = tk_font.Font(family='Times', size=34)
        button_ajuste_fino["font"] = ft
        button_ajuste_fino["fg"] = "#000000"
        button_ajuste_fino["justify"] = "center"
        button_ajuste_fino["text"] = "Ajuste Fino"
        button_ajuste_fino.place(x=390, y=430, width=320, height=65)
        button_ajuste_fino["command"] = self.button_visualizar_command

    def button_visualizar_command(self):
        print("command")
        if self.selected_planet:
            print(f"Selected planet {self.selected_planet}")

    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])
        planet = w.get(index)
        planet_name = self.plantes_dict[planet]
        self.selected_planet = planet_name
        print('You selected item %d: "%s"' % (index, planet_name))

        fixed_height = 210

        img = Image.open(f"imgs/{planet_name}.png")

        height_percent = (fixed_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_percent)))

        resized_image = img.resize((width_size, fixed_height), Image.NEAREST)

        new_image = ImageTk.PhotoImage(resized_image)

        self.label_img.configure(image=new_image)
        self.label_img.image = new_image
