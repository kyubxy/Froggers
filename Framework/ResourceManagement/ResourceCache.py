import pygame
import os
import os.path
from ResourceManagement.ImageLoader import *
from ResourceManagement.SoundLoader import *
from ResourceManagement.FontLoader import *

# preloads and handles all relevant assets
class ResourceCache:
    def __init__(self, resourcesDirectory = "res"):
        # cached resources
        self.Resources = dict()

        self.LoadedDirectories = []
        
        self.resDirectory = resourcesDirectory

        # assigning file extensions to their respective resource loaders
        self.Loaders = {
            "img" : ImageLoader(),
            "se"  : SoundLoader(),
            "fnt" : FontLoader()
        }

    # load all assets from a specified directory
    def LoadDirectory (self, directory):
        # ensure we are not loading the same thing twice
        # most implementations of this method will make this check but we are checking twice anyway
        # to prevent any unwanted memory leaks etc
        if directory in self.LoadedDirectories:
            print ("directory {0} has already been loaded".format (directory))
            return

        for asset in os.listdir (os.path.join (self.resDirectory, directory)):
            print ("loading {0}...".format (asset))
            assetType = asset.partition("_")[0]

            # check if the resource is loadable
            if assetType in self.Loaders:
                # add the resource to the cache
                _loader = self.Loaders[assetType]
                assetpath = os.path.join (self.resDirectory, directory, asset)
                if hasattr (_loader, "get_asset"):      # get only one asset
                    self.Resources[os.path.splitext (asset)[0]] = _loader.get_asset (assetpath)
                elif hasattr (_loader, "get_assets"):   # add an existing dictionary of assets to this dictionary
                    self.Resources.update (_loader.get_assets (assetpath))
                
            else:
                if os.path.splitext(asset)[1] == ".txt":
                    print ("{0} is a text file, if it is not a font size file, consider removing from resources as it is not loaded by the cache".format (asset))
                else:
                    print ("{0} of type {1} is not a supported asset and was not loaded by the cache".format (asset, assetType))

        self.LoadedDirectories.append (directory)