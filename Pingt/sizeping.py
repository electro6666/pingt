import os as ping
print("Controlling the size of packets send")

size = input("enter size and site:")

ping.system("ping -s" + size)
