import time
import threading
import csv #for saving data in fil in csv format

# ------------------------------------------------------------
import sys
import os

# Appending full path to Main_Window directory to sys.path
full_path_to_Main_Window_module = os.path.realpath(os.path.join(os.path.dirname(__file__), ''))
sys.path.append(full_path_to_Main_Window_module)
import definitions_for_Main_Window

# Appending full path to MCC134Reader_Directory to sys.path
full_path_of_MCC134Reader_Dir = os.path.realpath(os.path.join(definitions_for_Main_Window.ROOT_DIR, 'MCC134_Reader_module'))
sys.path.append(full_path_of_MCC134Reader_Dir)
import MCC134_Reader_module
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

        
    
    _mcc134_reader = MCC134_Reader_module.MCC134Reader.MCC134Reader()

    def run(self):
        if self._thread1.is_alive() == False:
            self._thread1.start()

    

    def _thread1_function(self, event_stop, event_close):
        if self._thread2.is_alive() == False: 
            self._thread2.start()
        
        while True:
            # ((JUST FOR NOW))
            event_close.set()

            if event_close.is_set():
                break


    def _thread2_function(self, event_stop, event_close):
        # open the file in the write mode
        dataFile = open('file_From_Python.txt', 'w')

        # create the csv writer
        writer = csv.writer(dataFile)

        # Display the header row for the data table.
        dataHeader = "    Sample,   "
        dataHeader += "Time,        "
        
        for channel in self._mcc134_reader.channels:
            # print('     Channel', channel, end='')
            dataHeader += "Channel" + str(channel) + ",    "
            
        print(dataHeader)
        dataFile.write(dataHeader + '\n')

        self._delay_between_reads = 0.4 
        samples_per_channel  = 0
        startTime = float(0.0)

        if self._event_stop_thread2.is_set() == False:
            while (samples_per_channel <= 20): # Read a single value from each selected channel.d
                dataRow = []
                dataRow.append(samples_per_channel)
                # Display the updated samples per channel count
                print('\r{:6d}'.format(samples_per_channel), end='')

                if samples_per_channel == 0:
                    startTime = time.perf_counter()
            
                sampleTime = time.perf_counter()
                sampleTimeFromStart = sampleTime - startTime
                dataRow.append(sampleTimeFromStart)
                print('{:12.2f} s'.format(sampleTimeFromStart), end='')


                # Read a single value from each selected channel.
                for channel in self._mcc134_reader.channels:
                    value = self._mcc134_reader.get_data_from_channel(channel)
                    print('{:12.2f} C'.format(value), end='')
                    strValue = str(value)
                    dataRow.append(strValue)
                
                writer.writerow(dataRow)
                samples_per_channel += 1
                time.sleep(self._delay_between_reads)

                # Cheching event to close the thread2
                if event_close.is_set():
                    print("MCC listener is stopped")
                    break
        
        dataFile.close()

        # ((JUST FOR NOW))
        event_close.set()

        # Cheching event to close thread2
        if event_close.is_set():
            return

     
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

