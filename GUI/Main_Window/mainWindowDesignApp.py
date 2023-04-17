#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import MCC134Reader


class MainWindowDesignApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel.configure(height=600, width=700)
        self.toplevel.geometry("640x480")
        self.frm_datafile_name = ttk.Frame(self.toplevel)
        self.frm_datafile_name.configure(
            borderwidth=5,
            height=50,
            padding=10,
            relief="flat",
            width=400)
        self.lbl_datafile_name = ttk.Label(self.frm_datafile_name)
        self.lbl_datafile_name.configure(text='Name of datafile:')
        self.lbl_datafile_name.grid(column=0, row=0, sticky="e")
        entry1 = ttk.Entry(self.frm_datafile_name)
        entry1.configure(takefocus=False)
        entry1.grid(column=1, row=0)
        self.frm_datafile_name.grid(column=0, row=0)
        labelframe4 = ttk.Labelframe(self.toplevel)
        labelframe4.configure(height=200, text='labelframe4', width=200)
        self.frm_tc0 = ttk.Frame(labelframe4)
        self.frm_tc0.configure(height=200, width=200)
        self.lbl_tc0 = ttk.Label(self.frm_tc0)
        self.lbl_tc0.configure(text='TC0:')
        self.lbl_tc0.grid(column=0, padx=5, row=0, sticky="e")
        self.lbl_tc0_data = ttk.Label(self.frm_tc0)
        self.lbl_tc0_data.configure(text='51.23')
        self.lbl_tc0_data.grid(column=1, row=0)
        self.frm_tc0.grid(column=0, padx=10, pady=10, row=0)
        self.frame5 = ttk.Frame(labelframe4)
        self.frame5.configure(height=200, width=200)
        self.lbl_tc1 = ttk.Label(self.frame5)
        self.lbl_tc1.configure(text='TC1:')
        self.lbl_tc1.grid(column=0, padx=5, row=0, sticky="e")
        self.lbl_tc1_data = ttk.Label(self.frame5)
        self.lbl_tc1_data.configure(text='52.33')
        self.lbl_tc1_data.grid(column=1, row=0)
        self.frame5.grid(column=0, padx=10, pady=10, row=1)
        self.frame8 = ttk.Frame(labelframe4)
        self.frame8.configure(height=200, width=200)
        self.lbl_tc2 = ttk.Label(self.frame8)
        self.lbl_tc2.configure(text='TC2:')
        self.lbl_tc2.grid(column=0, padx=5, row=0, sticky="e")
        self.lbl_tc2_data = ttk.Label(self.frame8)
        self.lbl_tc2_data.configure(text='50.39')
        self.lbl_tc2_data.grid(column=1, row=0)
        self.frame8.grid(column=0, padx=10, pady=10, row=2)
        self.frame9 = ttk.Frame(labelframe4)
        self.frame9.configure(height=200, width=200)
        self.lbl_tc3 = ttk.Label(self.frame9)
        self.lbl_tc3.configure(text='TC3:')
        self.lbl_tc3.grid(column=0, padx=5, row=0, sticky="e")
        self.lbl_tc3_data = ttk.Label(self.frame9)
        self.lbl_tc3_data.configure(text='50.01')
        self.lbl_tc3_data.grid(column=1, row=0)
        self.frame9.grid(column=0, padx=10, pady=10, row=3)
        labelframe4.grid(column=0, pady=10, row=1)
        self.btn_start = ttk.Button(self.toplevel)
        self.btn_start.configure(text='Start')
        self.btn_start.grid(column=0, row=2)
        self.btn_start.configure(command=self.start)

        # Main widget
        self.mainwindow = self.toplevel

    def run(self):
        self.mainwindow.mainloop()

    def start(self):
        MCC134Reader.printHello()
        MCC134Reader.startListening()


if __name__ == "__main__":
    app = MainWindowDesignApp()
    app.run()
