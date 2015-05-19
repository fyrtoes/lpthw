from sys import argv
from os import system
from os.path import exists
system('cls')

script, from_file, to_file = argv

indata = open(from_file).read()

open(to_file, 'w').write(indata)

