"""

Assistant app for Time Tracking & billing the time for tasks or jobs.

"""


from sys import version_info
import csv
from os import startfile

if version_info.major < 3:
    import Tkinter as tk
    import tkMessageBox as msg
else:
    import tkinter as tk
    from tkinter import messagebox as msg

from datetime import date, datetime, time




# The time tracking file

with open('Log_file.csv','a',newline='') as log_file:
    header =['Date','Task','Start Time','End Time', 'Total Time' ]
    writer = csv.DictWriter(log_file, fieldnames=header)
    d = {}
    d['Date'] = datetime.now().today()
    writer.writeheader()
     

def update_log_file(data={}):
    d.update(data)
    return d


##    with open('Log_file.csv','a') as log_file:
##        reader = csv.DictReader(log_file, fieldnames=['Date','Task','Start Time','End Time', 'Total Time'])
##        #previous_data = [line for line in reader]
##        #previous_data.append(data)
##        #print(previous_data)
##        writer = csv.DictWriter(log_file, fieldnames=['Date','Task','Start Time','End Time', 'Total Time'])
##        writer.writerow(data)

time_list = []

def total_time(time_list):
    print(time_list)
    end_time = time_list.pop()
    start_time = time_list.pop()
    h2 = end_time.hour
    m2 = end_time.minute
    s2 = end_time.second
    ms2 = end_time.microsecond

    h1 = start_time.hour
    m1 = start_time.minute
    s1 = start_time.second
    # ms1 = start_time.microsecond

    h_diff = h2 - h1 
    m_diff = m2 - m1 
    s_diff = s2 - s1
    # ms_diff = ms2 - ms1
    # total = "{h_diff}:{m_diff}:{s_diff}:{ms_diff}".format(h_diff=h_diff, m_diff=m_diff, s_diff=s_diff,ms_diff=ms_diff)

    total = "{h_diff}:{m_diff}:{s_diff}".format(h_diff=h_diff, m_diff=m_diff, s_diff=s_diff)
    total = total.replace(':', ':')
    data = {'Total Time': str(total)}
    update_log_file(data)
    print("Total: ", total)



def save_start_time():
    if time_list and time_list[0] != None:
        restart_it = msg.askyesno("Error", "Timer already started.\nShall we restart it?")
        if not(restart_it):
            return time_list[0]
    name = task_name.get()
    if name in ('', None):
        msg.showerror("Error", "Need a name for the task")
        return 
    print(name)
    start = datetime.now().time()
    time_list.append(start)
    print('start : ', start)
    data = {'Task': str(name)}
    update_log_file(data)
    data = {'Start Time': str(start)}
    update_log_file(data)
    
    return

def save_end_time():
    if len(time_list) == 0:
        msg.showerror("Error", "Timer not started yet!!!")
        return
    end = datetime.now().time()
    print('end : ',end)
    time_list.append(end)
    if len(time_list) > 0: total_time(time_list)
    data = {'End Time': str(end)}
    update_log_file(data)
    return

def save_changes():
    task_name.delete(0, tk.END)
    with open('Log_file.csv','a', newline="") as log_file:
        writer = csv.DictWriter(log_file, fieldnames=['Date','Task','Start Time','End Time', 'Total Time'])
        data = update_log_file()
        writer.writerow(data)
    
    open_file = msg.askokcancel("Saved","Changes Saved!\n Open File?")
    if open_file:
        startfile('Log_file.csv')

def clear():
    task_name.delete(0, tk.END)

root = tk.Tk()
root.title('Time Tracking assistance')
root.geometry("350x250")

task = tk.Label(root, text="Task Name")
task.grid(row=1, column=3)


task_name = tk.Entry(root, width="25")
task_name.grid(row=2, column=3)

start_time = tk.Button(root, text="Start", command=save_start_time)
start_time.grid(row=4, column=2, padx=10, pady=10)

end_time = tk.Button(root, text="Finish", command=save_end_time)
end_time.grid(row=4, column=3, padx=10, pady=10)

save_time = tk.Button(root, text="Save", command=save_changes)
save_time.grid(row=5, column=2, padx=10, pady=10)

clear_text = tk.Button(root, text="Clear Text", command=clear)
clear_text.grid(row=2, column=4, padx=10, pady=10)

##
##recurring_tasks = ['t1', 't2', 't3']
##
##max_row = 5
##max_col = 3

##def update_label(label):
##    print(label)
##    task_name.insert(0, label)
##    return
##
##
##for ind, task_text in enumerate(recurring_tasks):
##    #print(task_text)
##    #tk.Button(root, text=task_text, command=update_label(task_text)).grid(row=max_row + 1, column=max_col + ind)
##    tk.Radiobutton(root, text=task_text, value=0).grid(row=max_row + 1 + ind, column=1)
##    
##

root.mainloop()
