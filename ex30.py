from os import system
from sys import argv
system('cls')

people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."	
elif cars < people:
	print "We should not take the cars."
else:
	print "We cannot decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we should take the trucks."
else:
	print "We still cannot decide."
	
if people > trucks:
	print "alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."