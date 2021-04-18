import pyglet



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
