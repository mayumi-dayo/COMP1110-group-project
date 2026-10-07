#import package manager modules

#import local modules
import modules.testmodule as test
import modules.conf as conf
import modules.playersave as save
import modules.mainmenu as mainmenu

# main program
if __name__ == "__main__":
    # load savefile
    try:
        playerdata = save.load()

# 1. init and render main menu  
# 2. load game settings
# 3. check for 