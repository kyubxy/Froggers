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

        # Directories that have already been loaded
        self.LoadedDirectories = []
        
        # head directory of all resources
        self.resDirectory = resourcesDirectory

        # array of supported loadable types
        # resource loaders must have either get_asset() or get_assets()
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
            assetType = asset.partition("_")[0] # get the asset type (se_,img_ etc)

            # check if the resource is supported by loaders
            if assetType in self.Loaders:
                # add the resource to the cache

                # find the appropriate loader
                _loader = self.Loaders[assetType]
                # get the full path of the asset
                assetpath = os.path.join (self.resDirectory, directory, asset)

                # load the asset and add it to the dictionary
                if hasattr (_loader, "get_asset"):      # get only one asset
                    self.Resources[os.path.splitext (asset)[0]] = _loader.get_asset (assetpath)
                elif hasattr (_loader, "get_assets"):   # add an existing dictionary of assets to this dictionary
                    self.Resources.update (_loader.get_assets (assetpath))
                
            else:
                # note that text files may still contain valuable information
                if os.path.splitext(asset)[1] == ".txt":
                    print ("{0} is a text file, if it is not a font size file, consider removing from resources as it is not loaded by the cache".format (asset))
                else:
                    print ("{0} of type {1} is not a supported asset and was not loaded by the cache".format (asset, assetType))

        # add the directory that was just loaded into the loaded directories
        self.LoadedDirectories.append (directory)