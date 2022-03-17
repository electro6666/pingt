import os as ping 
print("To send packets as soon as possible. This is used to test network performance")
site = input("enter site:")
ping.system("ping -i 2 -f " +  site)
