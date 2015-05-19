from sys import argv
import os
os.system('cls')

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read(), "\n"

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read(), "\n"

print txt.closed
print txt_again.closed
txt.close()
txt_again.close()