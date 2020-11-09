import os
import os.path
import ntpath
import logging

from pygame import Surface
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
            logging.warning ("directory {0} has already been loaded".format (directory))
            return

        for dirpath,_,assetnames in os.walk (os.path.join (self.resDirectory, directory)):
            for assetname in assetnames:
                self.LoadAsset (os.path.join(dirpath, assetname), addResDir=False)

        # add the directory that was just loaded into the loaded directories
        self.LoadedDirectories.append (directory)

    # load a single asset through a relative path
    # the resource folder does not need to be added to the path if addResDir is true
    def LoadAsset (self, path, resname = None, addResDir = True):
        asset = os.path.join (self.resDirectory, path) if addResDir else path
        assetname = os.path.splitext(ntpath.split (asset)[1])[0]
        assetType = assetname.partition("_")[0] # get the asset type (se_,img_ etc)

        # don't load something that's already been loaded
        if asset in self.Resources or resname in self.Resources:
            return

        # check if the resource is supported by loaders
        if assetType in self.Loaders:
            logging.debug ("loading {0}...".format (asset))
            # add the resource to the cache

            # find the appropriate loader
            _loader = self.Loaders[assetType]
            # get the full path of the asset
            #assetpath = os.path.join (self.resDirectory, directory, asset)

            # load the asset and add it to the dictionary
            if hasattr (_loader, "get_asset"):      # get only one asset
                resname = assetname if resname is None else resname     # give the asset a custom name only if there is one
                self.Resources[resname] = _loader.get_asset (asset)
            elif hasattr (_loader, "get_assets"):   # add an existing dictionary of assets to this dictionary
                self.Resources.update (_loader.get_assets (asset))
            
        else:
            # note that text files may still contain valuable information
            if os.path.splitext(asset)[1] == ".txt":
                logging.warning ("{0} is a text file, if it is not a font size file, consider removing from resources as it is not loaded by the cache".format (asset))
            else:
                logging.warning ("{0} of type {1} is not a supported asset and was not loaded by the cache".format (asset, assetType))