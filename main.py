from time import sleep

import GUI.Main_Window.mainWindowDesignApp as mainWindowDesignApp
import MCC134Reader

mode = "TEST" #"TEST" or "RUN"

def main():
    # app = mainWindowDesignApp.MainWindowDesignApp()
    # app.run()
    mcc134_reader = MCC134Reader.MCC134Reader()
    samples_per_channel = 0

    while (samples_per_channel <= 10):
        data_from_channel0 = mcc134_reader.get_data_from_channel(0)
        print("C0" + str(data_from_channel0), end="     ")
        data_from_channel0 = mcc134_reader.get_data_from_channel(1)
        print("C1" + str(data_from_channel0), end="     ")
        data_from_channel0 = mcc134_reader.get_data_from_channel(2)
        print("C2" + str(data_from_channel0), end="     ")
        data_from_channel0 = mcc134_reader.get_data_from_channel(3)
        print("C3" + str(data_from_channel0), end="     ")
        print()
        samples_per_channel += 1
        sleep(1)
        # Read a single value from each selected channel.
    
        


    


if __name__ == '__main__':
    # This will only be run when the module is called directly.
    main()
