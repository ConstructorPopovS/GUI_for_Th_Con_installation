import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# TODO Check, why does it works even if the file is in the Root directoru of the project
# when the path is created for definitions file, lockated in a subfolder
# TODO Change ROOT_DIR (without '..')

# # ------------------------------------------------------------
# import sys
# import os
# import definitions
# # Appending full path to MCC134Reader_Directory to sys.path
# full_path_of_MCC134Reader_Dir = os.path.realpath(os.path.join(definitions.ROOT_DIR, 'MCC134Reader_Directory'))
# sys.path.append(full_path_of_MCC134Reader_Dir)
# # ------------------------------------------------------------