import time

while True:
    for i in ["/","-","\\","|"]:
        print "pizza \r%s" %i,
        time.sleep(.1)
