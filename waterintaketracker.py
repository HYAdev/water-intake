import tkinter as tk

root = tk.Tk()

root.geometry("600x950") #how big is the window

root.title("Water Intake Tracker") #name of the app, shows up at the top
photo = tk.PhotoImage(file= r"c:\Users\kyra\Downloads\blackbottle.png") #waterbottle png
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(100, 100, image=photo, anchor='nw')
# root.config(bg="#99A2BA") TO ADD BG COLOR (ON HOLD)

import tkinter as tk

sum = 0
goal = 0 #goal will be depending on what the user inputs from the calculator

def submit():
    global sum  # made global so it can be used everywhere
    entered_oz = int(text_entry.get())  
    sum += entered_oz  # Adds entered_oz to the sum
    print(sum)  #within context of the Water Tracker, instead of printing to the terminal we can have a text box w the 'sum' variable so it changes depending on inputs




if sum >= goal/4 and sum < goal/2:
    #code: make water bottle go to 25%
    print('') #all the prints are just so that the rest of the code runs fine

if sum >= goal/2 and sum < goal - goal/4:
    #code: make water bottle go to 50%
    print('')

if sum >= goal - goal/4 and sum < goal:
    #code: make water bottle go to 75%
    print('')

if sum >= goal:
    #code: make water bottle go to 100% and add congratulation message thingy
    print('')





text_label = tk.Label(root, text="Enter Number of Oz you drank:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()


from tkinter import *
from tkinter import messagebox

def reset_entry():
    exercise_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_water():
    lb = int(weight_tf.get()) #sets the weight variable
    e = int(float(exercise_tf.get())) #sets exercise variable
    water = (lb*(2/3))+(12*(e/30)) #water oz formula
    water = round(water, 1)
    water_index(water)

def water_index(water): #makes the popup that tells how much water u should drink, isnt necessary to have the > 0 but it was easier for me
    
    if water > 0:
        messagebox.showinfo('Water Intake Tracker', f'suggested daily hydration = {water} oz') 


var = IntVar()

frame = Frame(
    root,
    padx=10, 
    pady=10
)
frame.pack(expand=False)


Lower_left = tk.Label(root,text="Water Calculator",font=("Helvetica 15 bold"),fg="#001853") #labels
Lower_left.place(relx = 0.35, rely = 0.6, anchor ='sw')


age_lb = Label( #displays the text below
    frame,
    text="Enter Age (2 - 120)"
)
age_lb.grid(row=1, column=1) #where it is

age_tf = Entry( #adds the input box
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

cal_btn = Button( #calculates how jmuch water needed when the button is pressed
    frame3,
    text='Calculate',
    command=calculate_water
)
cal_btn.pack(side=LEFT)

reset_btn = Button( #resets all the inputs 
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button( #destroys the pop up
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
 
 

def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    
    while True:
        
        set_alarm_time = f"{hour.get()}:{minute.get()}" #gets the time
 
        
        time.sleep(1)
 
        
        current_time = datetime.datetime.now().strftime("%H:%M") #Hour and minute
 
        
        if current_time == set_alarm_time: #kinda self explanatory 
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break
 

Label(root,text="Hydration Reminder",font=("Helvetica 15 bold"),fg="#001853").pack(pady=10) #labels
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
 
frame = Frame(root)
frame.pack()
 
hour = StringVar(root) #drop down menu for hours. 24 hrs 
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root) # droip down menu for minutes. 60 minutes per hour
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