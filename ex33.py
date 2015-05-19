from os import system
from sys import argv
system('cls')


def superloop(limit):
	i = 0
	numbers = []
	while i < limit:
		print "At the top of i is %d" % i
		numbers.append(i)
		i = i + 1
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i
	print "The numbers: "
	return numbers

num_list = superloop(6)
for num in num_list:
	print num