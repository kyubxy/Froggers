import pygame
import os

class FontLoader:
    def __init__ (self):
        pass

    def get_assets (self, path):
        # load all requested sizes of this font
        sizefilepath = os.path.join (os.path.dirname(path), os.path.splitext (path.partition("_")[2])[0] + ".txt")
        sizes = []
        if os.path.isfile (sizefilepath):
            # convert all string numbers to ints
            with open (sizefilepath, "r") as sf:
                line = sf.readline()
                while line:
                    sizes.append (int(line))
                    line = sf.readline()
        else:
            print ("no sizes were provided for the font {0}, a 48pt version has been added anyway".format (path))
            sizes.append (48)

        fonts = dict()
        for size in sizes:
            key = os.path.splitext (os.path.basename(path))[0] + "_" + str(size)
            fonts[key]=pygame.font.Font (path, size)

        return fonts