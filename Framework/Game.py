from Screen import *
from ResourceManagement.ResourceCache import *
from SpriteText import *
import pygame
import sys
import logging
# logging config
logging.basicConfig (filename = "Logs/runtime.txt", format="%(asctime)s [%(levelname)s] - %(message)s", filemode="w", level=logging.INFO)

# only write log to console if in debug mode
# otherwise, the console printing will slow the main thread
if "debug" in sys.argv:
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info ("entered debug mode")

# generic game definition 
class Game ():
    # initialises modules and fields
    def __init__(self, title = "Game", width = 1366, height = 768, fullscreen = True, resourceDir = "res"):
        # initialise relevant pygame modules
        pygame.mixer.pre_init(44100, -16, 1, 512)   # preload audio settings to minimise delays in audio
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self._title = title                                             # title of window
        self._windowSize = [width, height]                              # size of window
        self._running = True                                            # program state

        # instantiate pygame window
        if fullscreen:
            self.Window = pygame.display.set_mode ((0,0), pygame.FULLSCREEN)   
        else:
            self.Window = pygame.display.set_mode (self._windowSize)               
                 
        pygame.display.set_caption (self._title)                        # set title
        self.Clock = pygame.time.Clock ()                               # pygame clock
        
        self.CurrentScreen = Screen (self)                              # add an empty screen

        self.ResourceCache = ResourceCache (resourceDir)                # resource cache

        logging.info (f"Frogger engine is ready! If there are any issues, check the console for backtracking\n")

    # called once per frame, use exclusively for update logic
    def Update (self):
        self.CurrentScreen.Update()

    # called once per frame, use exclusively for graphics
    def Draw (self):
        self.CurrentScreen.Draw(self.Window)

    # used to change current screen
    def ChangeScreen (self, screen):
        self.CurrentScreen = screen
        logging.info (f"Entered screen {0}".format (type(screen).__name__))

    # use this to safely close the program
    def Exit (self):
        logging.info (f"Successfully exited the program")
        self._running = False

    # handles pygame events
    def OnEvent (self, event):
        if event.type == pygame.QUIT:
            self._running = False

        # keyboard events
        if event.type == pygame.KEYDOWN:
            for child in self.CurrentScreen.sprites():
                # check if it has the KeyDown attribute
                if hasattr (child, "KeyDown"):
                    child.KeyDown (event)

        # mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            for child in self.CurrentScreen:
                # check if it has the KeyDown attribute
                if hasattr (child, "MouseDown"):
                    child.MouseDown (event)


    # initiates game loop, starts the game
    def Run (self):
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

        # quit all modules
        pygame.font.quit()
        pygame.quit()
        sys.stdout.close()