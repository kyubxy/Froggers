To run the game, open and run Froggers.py, located at the root of this folder. All other files are intended for internal use.

# Description of important files and folders 

# Stats
contains important gameplay related statistics reported from each round

# UI
All UI elements used in the game

# Screens
this game uses screens to partition different parts of the game from each other. Each file contains information regarding what is in each screen

# res
this folder contains all the resources used by the game. each asset is prefaced by letters indicating its type followed by an underscore and its name. The prefix is to help in the loading process.

# GameObjects
this folder contains scripts that control gameplay entities. Anything that moves is a gameobject

# Framework
the underlying backbone that provides higher level tools to build the game

## Resource management
This game preloads all the necessary assets as it needs them in one specific spot as to prevent excess loading. This folder contains all the loading system logic.

### ResourceCache
Loads all the assets in a specified folder depending on the file's prefix (img, se etc...). If a prefix isn't given, then it isn't loaded

### FontLoader, ImageLoader, SoundLoader
Pygame loads different assets in different ways. These classes specify how a given file should be loaded into pygame. FontLoader uses a text file to load fonts of specified sizes. If one isn't given, it loads a font of 48pt by default.

## UI/button
Premade button class, can be customized using ButtonTheme

## Game
base class for any game's entry point. Contains initilization code and game loop

## GeometricGroup
An extension of the LayeredUpdates class from pygame. Uses its own coordinates to determine relative position for all of its children

## Screen
A room containing its own children 

## Sprite
Base class for anything to be drawn to the screen

# IO
Contains central data persistence objects

## Preference manager
Despite the misleading name, preference manager is used to store any data that needs to persist between runs. The name is to deter tampering

## Score manager
Handles scores attained by player

# Logs
contains runtime.txt. used for backtracking errors