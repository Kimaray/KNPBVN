#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
	from vnf import *
except ImportError, message:
    raise SystemExit,  "Unable to load module. {}".format(message)

#Loop for the intro, this only ever needs to play once so it's not in the main loop
while intro == True:
	VideoPlay('intro')
	pygame.mixer.music.play()
	intro = False
	menu = True

#Main loop
while done == False:
	key = pygame.key.get_pressed()
	
	if menu == True: #This is the code for the main menu. It should always come up after the intro
		MainMenu()
		mainmenurendered = True
		DebugInfo()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
			elif key[pygame.K_q]:
				done = True
				
			elif key[pygame.K_p]:
				menu = False
				if fromgame == True:
					background = pygame.image.load(LoadFromZip(backgrounddir, StoryData(table, "background"), "jpg"))
					backgroundrect = background.get_rect()
				
			elif key[pygame.K_l]: #load save data from previous session
				with open('dat/savefile') as f:
					data = pickle.load(f)
				table = data
				storytext = StoryData(table, "dialog")
				character = StoryData(table, "character")
				menu = False
				
			elif key[pygame.K_m]: #Audio toggle. User can press M key to pause or unpause	
				MuteSound(audio)
				audio = MuteSound(audio)
	
	elif menu == False: #This is the code for the main game, when menu == false we can begin
		if table != currentscene: #Put char, bg and text on screen
			textbox = pygame.image.load(LoadFromZip(uidir, "textbox", "png"))
			textboxrect = textbox.get_rect()
			screen.blit(BGLoad()[0], BGLoad()[1])
			screen.blit(CharLoad()[0], CharLoad()[1])
			screen.blit(textbox, textboxrect)
			screen.blit(TextRender("{}".format(character), BLACK, charactername, 'main'), (40, 485))
		
			charactertextbox = pygame.Rect((15, 515, 780, 75))
			rendered_text = TextRectRender(storytext, regularfont, charactertextbox, (0, 0, 0), (191, 191, 191, 150), 0)
			screen.blit(rendered_text, charactertextbox.topleft)
        
			data = table
			currentscene = table
			DebugInfo()
		else:
			pass

		if pygame.mixer.music.get_busy() == False: #If music has finished playing start it again
			pygame.mixer.music.play()
	
		if StoryData(table, "end") == "True": #If the story is done we return to main menu.
			table = "scene1"
			storytext = StoryData(table, "dialog")
			character = StoryData(table, "character")
			VideoPlay('credits')
			intro = False
			playing = False
			done = False
			menu = True

		for event in pygame.event.get(): #Get any event (keybo/mouse presses)
			if event.type == pygame.QUIT:
				done = True

			#If the mouse is clicked get everything set up to advance to next scene
			elif (event.type == pygame.MOUSEBUTTONUP) or (key[pygame.K_RIGHT]):
				currentscene = table
				table = StoryData(table, "nextscene")
				storytext = StoryData(table, "dialog")
				character = StoryData(table, "character")
				
			elif key[pygame.K_LEFT]: #If user presses left arrow fo back to previous scene
				currentscene = table
				table = StoryData(table, "lastscene")
				storytext = StoryData(table, "dialog")
				character = StoryData(table, "character")
				
			elif key[pygame.K_m]: #Audio toggle. User can press M key to pause or unpause	
				MuteSound(audio)
				audio = MuteSound(audio)
					
			elif key[pygame.K_s]:#key for saving game
				with open('dat/savefile', 'w') as f:
					pickle.dump(data, f)
				
			elif key[pygame.K_q]: #Shortcut for quiting game. Exits right away, should ask for confirmation.
				done = True
			
			elif key[pygame.K_ESCAPE]:
				menu = True
				fromgame = True
				background = pygame.image.load(LoadFromZip(backgrounddir, "school", "jpg"))
				backgroundrect = background.get_rect()
			
	pygame.display.flip() 
	click.tick(int(config.get('settings', 'gamefps')))

pygame.quit()
