#simple pinging script by @codingstorm (@yfimsky)

import re # needed
import time # also needed
import pythonping # core of this script

inp = input("Enter latency between packages: ") # latency thing


def pinging(): # def coz i wanted
    x = 0 # x = packets count
    allping = 0 # all ping count
    while True:
        x += 1 # if u want u can delete this
        ping = pythonping.ping('') # put ur host here
        print("ping is " + str(ping.rtt_avg_ms)) # average ping u also can change this
        print("losses is " + str(ping.packet_loss)) # packets loss
        allping += ping.rtt_avg_ms # need to make avg ping
        avg_ping = allping / x # avg ping itself
        print("average ping is " + str(avg_ping) + "\n") # printing avg ping
        time.sleep(float(inp)) # bed time! (not really)


if re.match('[0-9]+', inp): # that u need coz u can break script if u put wrong symbol here
    pinging() # pinging starting
else:
    print(inp + ' can be only numbers') # thats what im talking about
