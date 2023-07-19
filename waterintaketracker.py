import tkinter as tk

root = tk.Tk()

root.title("Water Intake Tracker")
photo = tk.PhotoImage(file= r"c:\Users\kyra\Downloads\blackbottle.png")
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(100, 100, image=photo, anchor='nw')
# root.config(bg="#99A2BA") TO ADD BG COLOR (ON HOLD)

from tkinter import *
from tkinter import messagebox

def reset_entry():
    exercise_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_water():
    lb = int(weight_tf.get())
    e = int(float(exercise_tf.get()))
    water = (lb*(2/3))+(12*(e/30))
    water = round(water, 1)
    water_index(water)

def water_index(water):
    
    if water > 0:
        messagebox.showinfo('Water Intake Tracker', f'suggested daily hydration = {water} oz') 


var = IntVar()

frame = Frame(
    root,
    padx=10, 
    pady=10
)
frame.pack(expand=True)


age_lb = Label(
    frame,
    text="Enter Age (2 - 120)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)


exercise_lb = Label(
    frame,
    text="Enter Minutes of Exercise  "
)
exercise_lb.grid(row=3, column=1)

exercise_tf = Entry(
    frame, 
)
exercise_tf.grid(row=3, column=2, pady=5)

weight_lb = Label(
    frame,
    text="Enter Weight (lb)  ",

)
weight_lb.grid(row=4, column=1)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=6, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_water
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:root.destroy()
)
exit_btn.pack(side=RIGHT)


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
            break
 

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