from Screen import *
from collections import deque
from SpriteText import *
import pygame

# generic game definition 

class Game ():
    def __init__(self, title = "Game", width = 1366, height = 768):
        # initialise relevant pygame modules
        pygame.font.init()

        self._title = title                                 # title of window
        self._windowSize = [width, height]                  # size of window
        self._running = True                                # program state
        self.Window = None                                  # pygame window
        self.Clock = pygame.time.Clock ()                   # pygame clock
        
        self.CurrentScreen = Screen (self)                        # add an empty screen

    def Update (self):
        self.CurrentScreen.Update()

    def Draw (self):
        self.CurrentScreen.Draw(self.Window)

    # used to change current screen
    def ChangeScreen (self, screen):
        self.CurrentScreen = screen

    # handles pygame events
    def OnEvent (self, event):
        if event.type == pygame.QUIT:
            self._running = False

        # TODO experiment with checking subtypes
        
        # keyboard events
        if event.type == pygame.KEYDOWN:
            for child in self.CurrentScreen:
                # check if it has the KeyDown attribute
                if hasattr (child, "KeyDown"):
                    child.KeyDown (event)

        # mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check current screen
            if hasattr (self.CurrentScreen, "KeyDown"):
                self.CurrentScreen.KeyDown (event)

            for child in self.CurrentScreen:
                # check if it has the KeyDown attribute
                if hasattr (child, "MouseDown"):
                    child.MouseDown (event)

    def Run (self):
        self.Window = pygame.display.set_mode (self._windowSize)       # instantiate pygame window
        pygame.display.set_caption (self._title)                       # set title

        while self._running:
            # handle pygame events
            for e in pygame.event.get():
                self.OnEvent (e)

            # updating
            self.Update()  

            # drawing
            self.Window.fill ([0,0,0])
            self.Draw ()
            pygame.display.flip()   # swap buffers

            self.Clock.tick (60)        # capping game speed at 60 cycles per second