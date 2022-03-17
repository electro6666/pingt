import os as ping
print("Changing the time interval")
time = input("enter intervel time and site:")
ping.system("ping -i" + time)
