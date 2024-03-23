#LIBRARIES AND PACKAGES
import pyfiglet
import pystyle
from pystyle import Colors, Colorate
#PSEUDOCODE

#Input Name
name = input("Please Enter Your Name: ")

#Input Dream Job
DreamJob = input("Please Enter Your Dream Job: ")

#Input Favorite Color
FaveColor = input("What is your Favorite Colour?: ")

#Print Fancy Name
FancyName = pyfiglet.figlet_format(name, font='isometric1')
print(Colorate.Horizontal(Colors.rainbow, FancyName))

#Print Fancy Job
FancyJobName = pyfiglet.figlet_format(DreamJob, font='isometric1')
print(Colorate.Horizontal(Colors.rainbow, FancyJobName))

#Print Fancy Fave Color
FancyFaveColor = pyfiglet.figlet_format(FaveColor, font='isometric1')
print(Colorate.Horizontal(Colors.rainbow, FancyFaveColor))