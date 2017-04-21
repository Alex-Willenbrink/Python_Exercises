from sys import argv
script, filename = argv

file = open(filename)

print "\n" + file.read() + "\n"
file.close()
