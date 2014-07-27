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

###File structure/description:

-build_win.py: Builds an exe suitable for distribution on Windows systems
-main.py: Contains the main game loop
-vnf.py: All of the games functions and most of its variables. Is imported into main.py
-README.md: The readme file for Github (you're reading it now)
--av 
---**intro.vnv**: Intro video, plays when game is launched
---**credits.vnv**: Credits video, plays when game is finished
---**music.vnm**: Music that plays in game
--dat
---**ast.pne**: Stores all the games assets (images). Is just a zip file at the moment
---**config.sec**: Store all the games configuration data
---**savefile**: File that the game uses for saving progress
---**store.sty**: All the data needed for the story. Is a JSON file. 
--fonts
---**debug.ttf**: Font used in debug menu
---**main.ttf**: Font used for all text in story
---**titles.ttf**: Font used for title in menu screen, other menus
--info
---**CHANGES**: Changelog for each version of the engine
---**LICENSE**: The BSD 3-clause license that the engine is license under.

###Features being worked on now:

* Multiple characters on screen
* Moving characters on screen
* Changing audio tracks in game

###Things to implement in the future:

* Fade in/out
* Sound effects
* Better error handling (handling them at all would be nice)
* Options Menu
* Info screen
* Multiple saves

If you have any questions contact me: compaqxp@gmail.com, http://www.skyllama.com
