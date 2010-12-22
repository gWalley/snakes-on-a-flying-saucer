#!/usr/bin/env python

# An extremely limited prototype. Sort of just a test really, I guess?

actions = {
	'get': { 'args': 1,
		'func': lambda args: print("You get the {0}.".format(args[0])),
	},
	'kill':	{ 'args': 1,
		'func': lambda args:
			print("You try to kill the {0}.".format(args[0])),
	},
	'breathe': {
		'args': 0,
		'func': lambda:
			print("You respire for a bit. Feels good."),
	},
	'look': {
		'args': 0, # Restrictive: You could also look at a thing.
		'func': lambda: look_around(),
		# Could be ('func': look_around) if look_around was defined
		# beforehand, otherwise error ('Can't find look_around')
	},
}

# Data and stuff should be moved OUT of the source files, but this is fine as
# an example.
items = [
	'toast', 'bees', 'shoes'
]

def look_around():
	print ("You see ", ", ".join(items), ".", sep="") # wth python


def evaluate(ins):
	# This looks hella gay and should be rewritten
	ins = ins.split(' ')
	
	# unshift?
	verb = ins[0]
	ins = ins[1:]

	# So many nested ifs. No chance for additional functionality.
	if verb in actions:
		action = actions[verb]
		if (action['args'] == len(ins)):
			if (len(ins) == 0):
				action['func']()
			elif (ins[0] in items):
				# multiple arguments not supported
				action['func'](ins)
			else:
				print ("There is no {0} here to {1}.".format(
					ins[0], verb))
		else:
			print ("You cannot {0} {1} things.".format(
					verb, len(ins)))
	else:
		print ("You don't know how to {0}.".format(verb))

#
print ("An extremely simple prototype input processing loop")

# REPL!
while 1:
	print (">", end=' ')
	evaluate (input())


