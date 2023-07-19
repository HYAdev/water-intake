import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

root.title("Water Intake Tracker")
photo = tk.PhotoImage(file= r"c:\Users\rflor\Downloads\blackbottle.png")
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(100, 100, image=photo, anchor='nw')
# root.config(bg="#99A2BA") TO ADD BG COLOR (ON HOLD)

from tkinter import *
import datetime
import time
import winsound
from threading import *
 

root.geometry("600x700")
 

def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    
    while True:
        
        set_alarm_time = f"{hour.get()}:{minute.get()}"
 
        
        time.sleep(1)
 
        
        current_time = datetime.datetime.now().strftime("%H:%M")
 
        
        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            messagebox.showinfo('Water Intake Tracker', f'Reminder: Stay Hydrated, Drink Water')  #creates pop-up notif, can change later to connect to SMS message

            break #ensures sound isn't repeated
 

Label(root,text="Hydration Reminder",font=("Helvetica 20 bold"),fg="#001853").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
 
frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 

Button(root,text="Set Reminder",font=("Helvetica 15"),command=Threading).pack(pady=20)
 

root.mainloop()