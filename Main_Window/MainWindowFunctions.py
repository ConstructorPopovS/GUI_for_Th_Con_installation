import MCC134Reader_Directory.MCC134Reader as MCC134Reader
from time import sleep
import threading

class MCC134_listener:
    def  __init__(self):
        self.__samples_per_channel = 0

        self._event_stop_thread1 = threading.Event()
        self._event_close_thread1 = threading.Event()
        self._thread1 = threading.Thread(target =self._thread1_function, args=(self._event_stop_thread1, self._event_close_thread1(),))

        self._event_stop_thread2 = threading.Event()
        self._event_close_thread2 = threading.Event()
        self._thread2 = threading.Thread(target =self._thread2_function, args=(self._event_stop_thread2, self._event_close_thread2(),))
        
    __mcc134_reader = MCC134Reader.MCC134Reader()

    def _thread1_function(self, event_stop, event_close):
        samples_per_channel  = 0
        while (samples_per_channel <= 10): # Read a single value from each selected channel.d
            print("Data")
            # data_from_channel0 = self.__mcc134_reader.get_data_from_channel(0)
            # print("C0" + str(data_from_channel0), end="     ")
            # data_from_channel0 = self.__mcc134_reader.get_data_from_channel(1)
            # print("C1" + str(data_from_channel0), end="     ")
            # data_from_channel0 = self.__mcc134_reader.get_data_from_channel(2)
            # print("C2" + str(data_from_channel0), end="     ")
            # data_from_channel0 = self.__mcc134_reader.get_data_from_channel(3)
            # print("C3" + str(data_from_channel0), end="     ")
            # print()
            samples_per_channel += 1

            if event_close.is_set():
               print("MCC listener is stopped")
               break
            sleep(1)
    
    __event_close_listener_thread = threading.Event()
    __mcc134_listener_thread = threading.Thread(target=__mcc134_listener_function, args=(__event_close_listener_thread,))
    


    
       
    def start_listener_thread(self):
        if self.__mcc134_listener_thread.is_alive() == False:
            print("Start Listener thread")
            print()
            self.__mcc134_listener_thread.start()
    
    def stop_listener_thread(self):
        self.__event_close_listener_thread.set()    

