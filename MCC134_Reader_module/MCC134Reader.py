from __future__ import print_function
from time import sleep
from sys import stdout
from daqhats import mcc134, HatIDs, HatError, TcTypes

# ------------------------------------------------------------
import sys
import os
# import definitions
# Appending full path to MCC134_Reader_module to sys.path
full_path_of_MCC134_Reader_module = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(full_path_of_MCC134_Reader_module)
# ------------------------------------------------------------

from MCC134_Reader_module.daqhats_utils import select_hat_device, tc_type_to_string
import csv #for saving data in fil in csv format
import time #for creating timer during experiment

class MCC134Reader():
    def __init__(self) -> None:
        self.tc_type = TcTypes.TYPE_K   # change this to the desired thermocouple type
        self.channels = (0, 1, 2, 3)
        try:
            # MCC134 __init__
            # Get an instance of the selected hat device object.
            self.address = select_hat_device(HatIDs.MCC_134)
            self.hat = mcc134(self.address)

            for channel in self.channels:
                self.hat.tc_type_write(channel, self.tc_type)
            
        except (HatError, ValueError) as error:
            print('\n', error)

    def set_tc_type_on_channel(self, channel, tc_type):
        number_of_channel = channel
        if number_of_channel > 3:
            number_of_channel = 3
        
        new_tc_type = TcTypes.TYPE_K
        if tc_type == "K":
            new_tc_type = TcTypes.TYPE_K
        elif tc_type == "J":
            new_tc_type = TcTypes.TYPE_J

        self.hat.tc_type_write(channel, new_tc_type)

    def get_data_from_channel(self, channel):
         # Read a single value from selected channel.
        value = self.hat.t_in_read(channel)
        return(value)
    
    
# if __name__ == '__main__':
#     # This will only be run when the module is called directly.
#     main()