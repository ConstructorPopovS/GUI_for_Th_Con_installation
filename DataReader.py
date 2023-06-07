import serial
import random

# Imports for MCC134
from daqhats import mcc134, HatIDs, HatError, TcTypes
# ------------------------------------------------------------
import sys
import os
import definitions
# Appending full path to MCC134Reader_Directory to sys.path
full_path_of_MCC134Reader_Dir = os.path.realpath(os.path.join(definitions.ROOT_DIR, 'MCC134Reader_Directory'))
sys.path.append(full_path_of_MCC134Reader_Dir)
# ------------------------------------------------------------
from MCC134_Reader_module.daqhats_utils import select_hat_device, tc_type_to_string

class DataReader():
    def __init__(self) -> None:
        # Settings for Serial
        # self.ser = serial.Serial(port='COM12',baudrate=9600,timeout=15)#COM12, /dev/ttyACM0
        self.NameTC = [b'tc0', b'tc1', b'tc2']

        # Settings for MCC134
        self.tc_type = TcTypes.TYPE_K   # change this to the desired thermocouple type
        self.delay_between_reads = 0.1  # Seconds
        self.channels = (0, 1, 2, 3)

        try:
            # Get an instance of the selected hat device object.
            address = select_hat_device(HatIDs.MCC_134)
            self.hat = mcc134(address)

            for channel in self.channels:
                self.hat.tc_type_write(channel, self.tc_type)
        except:
            pass
        

    def __read(self, name):
        # self.ser.write(name)
        aData_str = "0"
        aData_str = random.randrange(20, 40) #self.ser.readline().decode('ascii')
        # aData_str = str(random.randrange(20,40))

        try:
            aData_float = float(aData_str)
            return aData_float
        except:
            print("UserExeption: convertation tc_str to float is failed")
            return 0
    
    def read_tc0(self):
        # value = self.__read(self.NameTC[0])
        value = self.read_tc(0)
        return value
    
    def read_tc1(self):
        # value = self.__read(self.NameTC[1])
        value = self.read_tc(1)
        return value
    
    def read_tc2(self):
        # value = self.__read(self.NameTC[2])
        value = self.read_tc(2)
        return value
    
    def read_tc3(self):
        # value = self.__read(self.NameTC[2])
        value = self.read_tc(3)
        return value
    
    def read_tc(self, channel):
        # Read a single value from selected channel.
        value = self.hat.t_in_read(channel)
        return value

    def close(self):
        pass# self.ser.colse()
