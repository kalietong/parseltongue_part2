
import sys
cmdLineArg = len(sys.argv)
i=0

for argv in sys.argv:
    if cmdLineArg <= len(sys.argv):
        x = sorted("Argv of "+str(i)+ " is "+ str(sys.argv[i]))
        print(sorted(x, key = len))
        i=i+1
    else:
        print ("only script name in sys.argv")

sys.argv.sort(key = len, reverse = True)
for x in sys.argv:
    print(x)
