#!/usr/bin/env python
# Yet another test script.
# Try going to London twice in a row, using different capitalisation (LONDON)
# you can also go to Canada, but you're there already in the beginning.

# TODO:
#	Turn  player  and  areas  into classes.
#	Turn go_to into a function of Player on a Place, like:
#		player.go_to (turn_a_string_into_a_game_entity('London'))
#	Possibly turn Player into a subclass of a Character class? (FUTURE)
#	Be proud of Python's exception mechanism (it's less insane than Java)
#	Get rid of all references to any kind of switch-esque mechanism.

player = {
	'location': 'canada',
}

areas = { # this is only temporary anyways, until we get a data thingy sorted
	'canada': {
		'pos': (0, 0, 0),
		'description': "A Klondike bar.",
		'contents': { "Pirate", "Jew", "Ninja pirate jew" },
	}, # or whatever
	'london': {
		'pos': (6, 7, 8),
		'description': "The Queen lives here. It smells funny.",
		'contents': { "Queen", "Paris" },
	},
}

def go_to (where): # 'where' is a string perhaps
	if where == '?':
		print ("You can go to these places:")
		for i in areas:
			print ("\t", i.capitalize(), sep='')
		return 3
	if (player['location'] == where):
		return 2
	elif where in areas:
		player['location'] = where
		return 1
	else:
		return 0

def describe (place):
	print ("You go to ", place.capitalize(), ".", sep='')
	print (areas[place]['description'])
	print ("You see:")
	for i in areas[place]['contents']:
		print ("\ta", i)

while 1:
	print ("> go ", end="")
	try: # EXCEPTIONS
		instr = input()
	except (KeyboardInterrupt, EOFError): # ^C, ^D respectively
		print ("\nBye then.")
		exit (0)
	
	[ # Lol switch
		# yes, this is temporary, don't worry
		lambda: print ("You can't go there!"),
		lambda: describe (instr.lower()),
		lambda: print ("You are already there."),
		lambda: 1 # do nothing
	][go_to (instr.lower())]()


