from time import sleep

# ------------------------------------------------------------
import sys
import os
from definitions import ROOT_DIR
# Appending full path to Main_Window_Directory to sys.path
# full_path_to_Main_Window_Directory = os.path.realpath(os.path.join(ROOT_DIR, 'Main_Window_Directory'))
# sys.path.append(full_path_to_Main_Window_Directory)
# import definitions_for_Main_Window
# import Main_Window_Directory.MainWindowFunctions as Functions
# ------------------------------------------------------------

# import Main_Window_Directory.mainWindowDesignApp as mainWindowDesignApp
# from . import Main_Window_Directory
import Main_Window_module


mode = "TEST" #"TEST" or "RUN"

def main():
    app = Main_Window_module.mainWindowDesignApp.MainWindowDesignApp()
    app.run()


if __name__ == '__main__':
    # This will only be run when the module is called directly.
    main()
