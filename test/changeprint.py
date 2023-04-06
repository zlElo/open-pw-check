import sys
import time
steps = 10
print("Total steps: "+str(steps),end=' ')
time.sleep(1)
for i in range(steps):
    sys.stdout.flush()
    print("\rStep "+str(i+1)+"/"+str(steps),end=' ')
    time.sleep(1)
print("")#to change the current line
