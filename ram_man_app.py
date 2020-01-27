"""
Created on Wed Mar 20 16:41:17 2019

@author: ish and vishnu

This is a RAM Manager program.

This program will run in the background. If there is any process that is consuming

RAM above the specified threshold or if the amount of free space in the RAM is 

less than the threshold then the program prompts a warning which allows the user

to abort the process that is consuming the maximum memory.

"""

#imports

#the os library contains system calls to kill a process
import os

# the tkinter library will be used for developing the GUI
import tkinter as tk

#tkinter widget to display warning messages.
import tkinter.messagebox

#OS related module
import psutil

#to process at regular intervals
from apscheduler.schedulers.blocking import BlockingScheduler

#Global Variable that stores the process id
pid=0


#function to call the message box that displays the message on the state of the system
def msg_box():
    warning = tk.Tk()
    warning.title("RAM WARNING");
    #displaying the Warning Message
    tit = tk.Label(text = "Warning: RAM usage CRITICAL! Click abort to abort the process", font = "Times 12 bold", fg = "Red").place(x = 5, y= 15)
    
    warning.geometry("500x100")
    btn = tk.Button(text = "ABORT", command = callback).place(x = 180, y= 50)
    
    warning.mainloop()
    
    return

#Function that is used for killing the process that exceeds the memory threshold
def callback():
    warning_response = tk.messagebox.showinfo("ABORTED","Process Aborted Successfully!")
    global pid
    os.kill(pid,9)
    
    global warning
    
    if warning_response == True:
        warning.quit()
    



#function for identifying the memory-consuming process
def processing_job():
    global pid
    #getting info about the most memory consuming process of the time 
    
    lst= list(map(int,(os.popen("ps ux --sort -rss | awk \'{print $2 \" \" $6}\'| awk NR==2").read()).split()))
    
    pid= lst[0]
    rss = lst[1]
    #checking the memory usage against the threshold
    if(rss>100000):
        print(rss,' ',pid)
        msg_box()
    else:
        print("Looking good")
        
    

#function for the homescreen accepted button. It will start the RAM manager program
def accepted():
    
    global a_response
    a_response = tk.messagebox.showinfo("RAM MANAGER ACTIVE", "YOU HAVE SUCCESSFULLY ACTIVATED RAM MANAGER")
    
    
    if a_response == True:
        global window
        window.quit()
        
    return
        
        
    
    
#function for the homescreen not accepted button. it just closes the window    
def rejected():
    response = tk.messagebox.showinfo("RAM MANAGER INACTIVE", "RAM MANAGER IS NOT ACTIVATED")
        
    if response == True:
        global window
        window.quit()
        
    return

#function to close the ram home window.
def close_window():
    global a_response
   # if a_response ==False:
    
#    a_response = False
    
    global window
    window.destroy()      


#GUI code for the home screen that appears on the start of the program.
    
def HomeScreen():    
    global window
    
    window.title("RAM MANAGER HOME")
    window.geometry("500x150")
    
    tk.Label(window, text = "The RAM MANAGER program will be running in the background", font = "Times 12 bold").place(x=10 ,y = 10)
    
    tk.Label(window, text = "Do you want to continue?", font = "Times 12").place(x=140,y=40)
    
    tk.Button(window, text = "Yes", command=accepted).place(x=100,y=80)
    
    tk.Button(window, text = "No", command=rejected).place(x=200,y=80)
    
    
    tk.Button(window, text = "Exit", command = close_window).place(x=300,y=80)
    window.mainloop()
    
    return
    

#response variable is to store whether the user has agreed to start the program.
global a_response
global window
window = tk.Tk()
a_response = False

HomeScreen()
window.quit()



"""
Instruction for execution

1. On starting the program the home screen window pops up.
2. On clicking Yes, the program execution begins
3. On clicking No, the program is not started and the home screen window closes.


"""


if(a_response == "ok"):
    print("Starting the RAM Manager")
    scheduler = BlockingScheduler()
    scheduler.add_job(processing_job, 'interval', seconds=10)
    scheduler.start()
    
    
    














