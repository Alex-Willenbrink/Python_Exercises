from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", int(third)

var1 = raw_input("Give me var1: ")
var2 = raw_input("Give me var2: ")

print "var1: %s, var2 %s" % (var1, var2)
