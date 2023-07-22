

from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import messagebox

from tkinter import *
import datetime
import time
from threading import *
from twilio.rest import Client
# User Interface Code


 
import tkinter as tk
from twilio.rest import Client
root = Tk() # Creates the window
root.title("Water Intake Tracker")
import pygame.mixer

def new_window(): 
   newWindow = Toplevel(root)
   def Threading():
    t1=Thread(target=alarm)
    t1.start()

   def alarm():
    
        while True:
        
            set_alarm_time = f"{hour.get()}:{minute.get()}" #gets the time
 
        
            time.sleep(1)
 
        
            current_time = datetime.datetime.now().strftime("%H:%M") #Hour and minute
 
        
            if current_time == set_alarm_time: #kinda self explanatory 
                pygame.mixer.init()
                pygame.mixer.music.load('notification.mp3')
                pygame.mixer.music.play()

                # allows the file to finish playing
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                account_sid = "enter sid"
                auth_token  = "enter auth"
                global pnumber
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                body="DRINK WATER", from_="+18332943083", to='+'+ pnumber
                
                )
                break
   def send_message():
        global pnumber
        pnumber = number.get()
        if not pnumber.strip(): #checks and see if pnumber is empty
            print("Enter a valid phone number")
            print(pnumber)


            

            
            
 

   Label(newWindow,text="Hydration Reminder",font=("Helvetica 15 bold"),fg="#001853").pack(pady = 2) #labels
   Label(newWindow,text="Set Time",font=("Helvetica 10 bold")).pack()
 
   frame = Frame(
        newWindow, padx=10, pady=10)
   frame.pack(expand= False)
 
   hour = StringVar(newWindow) #drop down menu for hours. 24 hrs 
   hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
   hour.set(hours[0])
 
   hrs = OptionMenu(frame, hour, *hours)
   hrs.pack(side=LEFT)
 
   minute = StringVar(newWindow) # droip down menu for minutes. 60 minutes per hour
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

   pnumber = " "

   def send_message():
        global pnumber
        pnumber = number.get()
        if not pnumber.strip(): #checks and see if pnumber is empty
            print("Enter a valid phone number")
            print(pnumber)

   Button(newWindow,text="Set Reminder",font=("Helvetica 10"),command=Threading).pack(side= BOTTOM, pady=5)


   label = tk.Label(newWindow, text='Enter your phone number(include country code)')
   number = tk.Entry(newWindow)
   number.focus_set()
   send_text = tk.Button(newWindow, text='Submit', command=send_message).pack(side=BOTTOM, padx=1, pady=5)




   label.pack(side = tk.TOP)
   number.pack()


from tkinter import *
from tkinter import messagebox

def new_window2():
    newWindow2 = Toplevel(root)

    def reset_entry():
        exercise_tf.delete(0,'end')
        weight_tf.delete(0,'end')

    def calculate_water():
        lb = int(weight_tf.get()) #sets the weight variable
        e = int(float(exercise_tf.get())) #sets exercise variable
        global water
        water = (lb*(2/3))+(12*(e/30)) #water oz formula
        water = round(water, 1)
        water_index(water)

    def water_index(water): #makes the popup that tells how much water u should drink, isnt necessary to have the > 0 but it was easier for me
    
        if water > 0:
            messagebox.showinfo('Water Intake Tracker', f'suggested daily hydration = {water} oz') 
            global waterGoal
            water = waterGoal


    var = IntVar()

    frame = Frame(
    newWindow2,
    padx=10, 
    pady=10
)
    frame.pack(expand=False)





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
    frame3.grid(row=8, columnspan=3, pady=10)

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



###########################################WATERBOTTLE#########################################################################
root.title("Water Intake Tracker") #name of the app, shows up at the top
# Haiyan: /Users/hyena/Documents/Code/Programming/water-intake/blackbottle.png
# Robert: c:\Users\rflor\Downloads\blackbottle.png
# Kyra: c:\Users\kyra\Downloads\blackbottle.png
# root.config(bg="#99A2BA") TO ADD BG COLOR (ON HOLD)

def update_image():
    global sum, goal

    sum_percent = sum / goal if goal != 0 else 0.0

    if 0.25 <= sum_percent < 0.5:
        canvas.itemconfig(image_on_canvas, image=quarter_filled_bottle)
    elif 0.5 <= sum_percent < 0.75:
        canvas.itemconfig(image_on_canvas, image=half_filled_bottle)
    elif 0.75 <= sum_percent < 1:
        canvas.itemconfig(image_on_canvas, image=three_quarter_filled_bottle)
    elif sum_percent >= 1:
        canvas.itemconfig(image_on_canvas, image=full_bottle)
    else:
        canvas.itemconfig(image_on_canvas, image=empty_bottle)

###############################################################
root.geometry("410x580")

message_label = Label(root, text="                  ", 
wraplength=20)
frame4 = tk.Frame(root)
frame4.pack(pady=10)

button1 = Button(frame4, text ="Water Calculator", command=new_window2, width=16, 
bg="gold")
button1.grid(row=0, column=1, padx= 5)

button2 = Button(frame4, text ="Water Reminder", command=new_window, width=16, 
bg="gold")
button2.grid(row=0, column=2)
Upper_left = tk.Label(button1)
Upper_left.place(relx = 1.0, rely = 1000.0, anchor ='n')



################################################################




empty_bottle = tk.PhotoImage(file=r"c:\Users\kyra\Downloads\blackbottle.png")
quarter_filled_bottle = tk.PhotoImage(file=r"c:\Users\kyra\Downloads\bottle25.png")
half_filled_bottle = tk.PhotoImage(file=r"c:\Users\kyra\Downloads\bottle50.png")
three_quarter_filled_bottle = tk.PhotoImage(file=r"c:\Users\kyra\Downloads\bottle75.png")
full_bottle = tk.PhotoImage(file=r"c:\Users\kyra\Downloads\bottle100.png")

canvas = tk.Canvas(root, width=200, height=300)
canvas.pack(side='top', fill='both', expand='yes')

image_on_canvas = canvas.create_image(5, 5, image = empty_bottle, anchor='nw')

import tkinter as tk

sum = 0
goal = 0 #goal will be depending on what the user inputs from the calculator

def submit():
    global sum  # made global so it can be used everywhere
    entered_oz = int(float(text_entry.get())) 
    sum += entered_oz  # Adds entered_oz to the sum
    print(sum)  #within context of the Water Tracker, instead of printing to the terminal we can have a text box w the 'sum' variable so it changes depending on inputs
    sum_label.config(text= 'Daily Water Intake: ' + str(sum))



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





frame1 = tk.Frame(root)
frame1.pack(pady=10)

text_label = tk.Label(frame1, text="Enter number of oz you drank:")
text_label.grid(row=0, column=0)

text_entry = tk.Entry(frame1)
text_entry.grid(row=0, column=1)

submit_button = tk.Button(root, text="Submit", command=submit) #makes submit button work
submit_button.pack(pady=1)

sum_label = tk.Label(root, text='Daily Water Intake: '+ str(sum))  # Label to display the sum
sum_label.pack(pady=1)


message_label = Label(root, text="                  ", 
wraplength=20)
message_label.pack()


root.mainloop() # Runs the main window loop