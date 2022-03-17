import os as ping
print("To only get the summary about the network use")
site = input("enter site:")
ping.system("ping -c 3 -q " + site)
#using -c 5 to stop this fast you can change it
