import pygame
import os
import logging

# loads fonts of varying sizes
class FontLoader:
    def __init__ (self):
        pass

    def get_assets (self, path):
        # load all requested sizes of this font
        sizefilepath = os.path.join (os.path.dirname(path), os.path.splitext (path.partition("_")[2])[0] + ".txt")
        sizes = []
        # check if the size file xists
        if os.path.isfile (sizefilepath):
            # read file, convert all string numbers to ints
            with open (sizefilepath, "r") as sf:
                line = sf.readline()
                while line:
                    sizes.append (int(line))
                    line = sf.readline()
        else:
            # if there isn't a file, load the font anyway with size 48pt
            # in general, there should always be a size file for each font
            logging.warning ("no sizes were provided for the font {0}, a 48pt version has been added anyway".format (path))
            sizes.append (48)

        fonts = dict()  # dictionary to be returned
        for size in sizes:  # add each font size to the dictionary
            key = os.path.splitext (os.path.basename(path))[0] + "_" + str(size)
            fonts[key]=pygame.font.Font (path, size)

        return fonts