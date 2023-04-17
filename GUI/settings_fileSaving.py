import tkinter as tk
import tkinter.font as font


name_of_datafile = "New_datafile"
tc1_value = 40.31
tc2_value = 36.83
tc3_value = 41.21
tc4_value = 35.94

stngs_file_window = tk.Tk()
stngs_file_window.title("Settings: File saving")

# File Name
frame_file_name = tk.Frame(master=stngs_file_window, padx=5, pady=5) # relief=tk.RAISED, borderwidth=5
frame_file_name.grid(row=0, column=0, sticky="nsew")

lbl_file_name = tk.Label(master=frame_file_name, text="Name for a new datafile")
lbl_file_name.grid(row=0, column=0, sticky="nsew")

ent_file_name = tk.Entry(master=frame_file_name)
ent_file_name.insert(0, name_of_datafile)
ent_file_name.grid(row=0, column=1, sticky="nsew")

# TC1
frame_tc1 = tk.Frame(master=stngs_file_window, padx=5, pady=5) # relief=tk.RAISED, borderwidth=5
frame_tc1.grid(row=1, column=0, sticky="nsew")

lbl_tc1 = tk.Label(master=frame_tc1, text="TC1: ")
lbl_tc1.grid(row=0, column=0, sticky="nsew")

lbl_tc1_value = tk.Label(master=frame_tc1, text=str(tc1_value))
lbl_tc1_value.grid(row=0, column=1, sticky="nsew")

# TC2
frame_tc2 = tk.Frame(master=stngs_file_window, padx=5, pady=5) # relief=tk.RAISED, borderwidth=5
frame_tc2.grid(row=2, column=0, sticky="nsew")

lbl_tc2 = tk.Label(master=frame_tc2, text="TC2: ")
lbl_tc2.grid(row=0, column=0, sticky="nsew")

lbl_tc2_value = tk.Label(master=frame_tc2, text=str(tc2_value))
lbl_tc2_value.grid(row=0, column=1, sticky="nsew")

# TC3
frame_tc3 = tk.Frame(master=stngs_file_window, padx=5, pady=5) # relief=tk.RAISED, borderwidth=5
frame_tc3.grid(row=3, column=0, sticky="nsew")

lbl_tc3 = tk.Label(master=frame_tc3, text="TC3: ")
lbl_tc3.grid(row=0, column=0, sticky="nsew")

lbl_tc3_value = tk.Label(master=frame_tc3, text=str(tc3_value))
lbl_tc3_value.grid(row=0, column=1, sticky="nsew")

# TC4
frame_tc4 = tk.Frame(master=stngs_file_window, padx=5, pady=5) # relief=tk.RAISED, borderwidth=5
frame_tc4.grid(row=4, column=0, sticky="nsew")

lbl_tc4 = tk.Label(master=frame_tc4, text="TC4: ")
lbl_tc4.grid(row=0, column=0, sticky="nsew")

lbl_tc4_value = tk.Label(master=frame_tc4, text=str(tc4_value))
lbl_tc4_value.grid(row=0, column=1, sticky="nsew")


stngs_file_window.mainloop()