import pyglet
from pyglet import font
from pyglet.font.ttf import TruetypeInfo


class ResourceHandler:
    def __init__(self):
        pyglet.resource.path = ["resources"]
        pyglet.resource.reindex()
        self.axolotl = pyglet.resource.image("enemies/axolotl.png")
        self.skeleton = pyglet.resource.image("enemies/skeleton.png")
        self.werewolf = pyglet.resource.image("enemies/werewolf.png")

    def return_image_for_name(self, name):
        if name == 'axolotl':
            return self.axolotl
        elif name == 'skeleton':
            return self.skeleton
        elif name == 'werewolf':
            return self.werewolf

    def load_font(self):
        # load external font from file
        # font_names = ['WarPriest3DRegular-Koxe', 'WarPriestCondensed-2Z8X', 'WarPriestExpanded-wpY9']
        font_names = ['EvilEmpire-4BBVK']
        for font_name in font_names:
            p = TruetypeInfo(f'./resources/fonts/evil-empire/{font_name}.ttf')
            name = p.get_name("name")
            p.close()
            font.add_file(f'./resources/fonts/evil-empire/{font_name}.ttf')
            print("Loaded font " + name)