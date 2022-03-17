import os as ping
print("To stop pingig after sometime use")
timeout = input("enter time and site:")
ping.system("ping -w " + timeout)
