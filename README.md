#KNPB 0.15

This is a test piece of software. If it crashes your computer or corrupts a file
it's your own fault. I can not and will not be held responsible for such things.

The goal of this software is to create a simple VN engine using Python and the
Pygame library. It's very basic and should not be used for any serious projects.

All story data is stored in JSON files. All options for 
the game can be found in dat/config.sec in a fairly common style for config 
files. If you don't know what you're doing *do not* edit any files! 

###Controls:

* **Any Mouse Button** - Advance Story
* **Right Arrow** - Advance Story
* **Left Arrow** - Move back in story
* **M** - Toggle music on or off
* **S** - Saves while in game
* **Q** - Quit (No confirmation, just quits immediately)
* **ESC** - Return to main menu (P to go back to game)


###Config.sec parameters:

* **devmode:** True or False, skips the intro and goes right to the main menu
* **debugmode:** True or False, provides some basic info on what the game is doing.
* **gamefps:** Accepts an int, is set to 30 by default. I wouldn't set it above 60 though.
* **volume:** A number from 0.0 to 1.0. Default is 0.2. Changes in game volume.
* **fullscreen:** True or False, enables or disables fullscreen mode 

*Do not change any other options!*

###Debug mode abbreviations:

* **CS =** Current Scene
* **CC =** Current Character
* **DN =** Sees if the game has been told to go to credits. If you see True in game something is wrong.
* **DM =** Shows if Devmode is enabled or not
* **AP =** 0 if audio is not playing, 1 if it is.
* **AM =** Shows if audio is paused or not
* **AL =** Returns current volume

If you have any questions contact me: compaqxp@gmail.com, http://www.skyllama.com
