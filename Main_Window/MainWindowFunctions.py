import MCC134Reader_Directory.MCC134Reader as MCC134Reader
import time
import threading
import csv #for saving data in fil in csv format

# ------------------------------------------------------------
import sys
import os
import definitions
# Appending full path to MCC134Reader_Directory to sys.path
full_path_of_MCC134Reader_Dir = os.path.realpath(os.path.join(definitions.ROOT_DIR, 'MCC134Reader_Directory'))
sys.path.append(full_path_of_MCC134Reader_Dir)
# ------------------------------------------------------------

class MCC134_listener:
    def  __init__(self):
        self.__samples_per_channel = 0

        self._event_stop_thread1 = threading.Event()
        self._event_close_thread1 = threading.Event()
        self._thread1 = threading.Thread(target =self._thread1_function, args=(self._event_stop_thread1, self._event_close_thread1,))

        self._event_stop_thread2 = threading.Event()
        self._event_close_thread2 = threading.Event()
        self._thread2 = threading.Thread(target =self._thread2_function, args=(self._event_stop_thread2, self._event_close_thread2,))

        # open the file in the write mode
        self._dataFile = open('file_From_Python.txt', 'w')

        # create the csv writer
        self._writer = csv.writer(self._dataFile)
    
    _mcc134_reader = MCC134Reader.MCC134Reader()

    def run(self):
        if self._thread1.is_alive() == False:
            self._thread1.start()

    

    def _thread1_function(self, event_stop, event_close):
        if self._thread2.is_alive() == False: 
            # Display the header row for the data table.
            dataHeader = "   Sample,   "
            dataHeader += " Time,      "
            # print('\n  Sample', end='')
            for channel in self._mcc134_reader.channels:
                # print('     Channel', channel, end='')
                dataHeader += " Channel" + str(channel) + ","
            
            print(dataHeader)
            self._dataFile.write(dataHeader + '\n')

            samples_per_channel = 0
            startTime = float(0.0)
            self._thread2.start()

        while True:
            if event_close.is_set():
                break


    def _thread2_function(self, event_stop, event_close):
        self._delay_between_reads = 0.1 
        self._samples_per_channel  = 0
        if self._event_stop_thread2.is_set() == False:
            while (self._samples_per_channel <= 100): # Read a single value from each selected channel.d
                dataRow = []
                dataRow.append(self._samples_per_channel)
                # Display the updated samples per channel count
                print('\r{:6d}'.format(self._samples_per_channel), end='')

                if self._samples_per_channel == 0:
                    startTime = time.perf_counter()
            
                sampleTime = time.perf_counter()
                sampleTimeFromStart = sampleTime - startTime
                dataRow.append(sampleTimeFromStart)
                print('{:12.2f} s'.format(sampleTimeFromStart), end='')


                # Read a single value from each selected channel.
                for channel in self._mcc134_reader.channels:
                    value = self._mcc134_reader.get_data_from_channel(channel)

                    # dataRow.append(value)
                    # if value == mcc134.OPEN_TC_VALUE:
                    #     print('   Open    ', end='')
                    #     dataRow.append('Open')
                    # elif value == mcc134.OVERRANGE_TC_VALUE:
                    #    print(' OverRange ', end='')
                    #    dataRow.append('OverRange')
                    # elif value == mcc134.COMMON_MODE_TC_VALUE:
                    #     print('Common Mode', end='')
                    #     dataRow.append('CommonMode')
                    # else:
                    print('{:12.2f} C'.format(value), end='')
                    strValue = str(value)
                    dataRow.append(strValue)

                    self._writer.writerow(dataRow)
                    self._samples_per_channel += 1
                    # stdout.flush()
                    # Wait the specified interval between reads.
                    time.sleep(self._delay_between_reads)
                    self._samples_per_channel += 1
                    if event_close.is_set():
                        print("MCC listener is stopped")
                        break

        if event_close.is_set():
            print("MCC listener is stopped")
            return

            

            
            sleep(1)
    
    


    
       
    def start_listener_thread(self):
        if self.__mcc134_listener_thread.is_alive() == False:
            print("Start Listener thread")
            print()
            self.__mcc134_listener_thread.start()
    
    def stop_listener_thread(self):
        self.__event_close_listener_thread.set()    

if __name__ == '__main__':
    # This will only be run when the module is called directly.
    listener = MCC134_listener()
    listener.run()

