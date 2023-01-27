"""
State for the Title scene
"""

import pygame as pg

from .. import prepare, state_machine, tools

SKY_COLOR = (153, 51, 255)
SKY_RECT = pg.Rect(0, 0, 1280, 1024)
MUSIC = pg.mixer.music


class Title(state_machine._State):
    """This State is updated while showing the title screen"""
    def __init__(self):
        state_machine._State.__init__(self)
        title = pg.transform.scale(prepare.titlewords, (600, 164))
        if title.get_alpha():
            title = title.convert_alpha()
        else:
            title = title.convert()
            title.set_colorkey(255,0,255)
        self.ground = title
        self.elements = self.make_elements()
        self.timer = None
        self.music = MUSIC
        self.music.load(prepare.mainTheme)

        
    def startup(self, now, persistant):
        self.persist = persistant
        self.start_time = now
        self.elements = self.make_elements()
        self.music.play(-1)


    def make_elements(self):
        group = pg.sprite.LayeredUpdates()
        group.add(AnyKey(), layer=1)
        return group

    def update(self, keys, now):
        """Updates the title screen."""
        self.now = now
        self.elements.update(now)

    def draw(self, surface, interpolate):
        surface.fill(SKY_COLOR, SKY_RECT)
        surface.blit(self.ground, SKY_RECT.topleft)
        self.elements.draw(surface)

    def get_event(self, event):
        """
        Get events from Control.  Currently changes to next state on any key
        press.
        """
        if event.type == pg.KEYDOWN:
            self.next = "GAME"
            self.done = True
            self.music.stop()


class AnyKey(pg.sprite.Sprite):
    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.raw_image = render_font(prepare._FONT_PATH, 30,
                                 "[Press Any Key]", (255,255,0))
        self.null_image = pg.Surface((1,1)).convert_alpha()
        self.null_image.fill((0,0,0,0))
        self.image = self.raw_image
        center = (prepare.SCREEN_RECT.centerx, 768)
        self.rect = self.image.get_rect(center=center)
        self.blink = False
        self.timer = tools.Timer(200)

    def update(self, now, *args):
        if self.timer.check_tick(now):
            self.blink = not self.blink
        self.image = self.raw_image if self.blink else self.null_image

def render_font(font, size, msg, color=(255,255,255)):
        """
        Takes the name of a loaded font, the size, and the color and returns
        a rendered surface of the msg given.
        """
        selected_font = pg.font.Font(font, size)
        return selected_font.render(msg, 1, color)


