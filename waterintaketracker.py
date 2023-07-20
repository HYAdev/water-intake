import tkinter as tk

root = tk.Tk()

root.geometry("600x950") #how big is the window
###########################################WATERBOTTLE#########################################################################
root.title("Water Intake Tracker") #name of the app, shows up at the top
# Haiyan: /Users/hyena/Documents/Code/Programming/water-intake/blackbottle.png
# Robert: c:\Users\rflor\Downloads\blackbottle.png
# Kyra: c:\Users\kyra\Downloads\blackbottle.png
# root.config(bg="#99A2BA") TO ADD BG COLOR (ON HOLD)

sum_percent = 0.0

def combined_functions():
    submit()
    update_image()

def update_image():
    global sum, goal, sum_percent

    sum_percent = sum / goal if goal != 0 else 1

    if sum_percent >= 0.125 and sum_percent < 0.25:
        canvas.itemconfig(image_on_canvas, image= one_eighth_bottle)
        print('Water bottle at: 25')
        print(goal) 

    
    
    elif sum_percent >= 0.25 and sum_percent < 0.375:
        canvas.itemconfig(image_on_canvas, image=quarter_filled_bottle)



    elif sum_percent >= 0.375 and sum_percent < 0.5:
        canvas.itemconfig(image_on_canvas, image=three_eighth_bottle)
        print('Water bottle at: 50')
        print(goal) 



    elif sum_percent >= 0.5 and sum_percent < 0.625:
        canvas.itemconfig(image_on_canvas, image=half_filled_bottle)



    elif sum_percent >= 0.625 and sum_percent < 0.75:
        canvas.itemconfig(image_on_canvas, image=five_eighth_bottle)
        print('Water bottle at: 75')
        print(goal) 



    elif sum_percent >= 0.75 and sum_percent < 0.875:
        canvas.itemconfig(image_on_canvas, image=three_quarter_filled_bottle)



    elif sum_percent >= 0.875 and sum_percent < 1.0:
        canvas.itemconfig(image_on_canvas, image=seven_eighth_bottle)
        print('Water bottle at: 100')
        print(goal) 

    elif sum_percent >= 1.0:
        canvas.itemconfig(image_on_canvas, image=full_bottle)

    elif sum_percent < 0.125:
        canvas.itemconfig(image_on_canvas, image=empty_bottle)
        print('Water bottle at: empty')
        print(sum_percent)    

    print ('percent is:' + str(sum_percent))
    return sum_percent
    

empty_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\blackbottle.png")
one_eighth_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle-eighth.png")
quarter_filled_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle25.png")
three_eighth_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle-3-eighth.png")
half_filled_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle50.png")
five_eighth_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle-5-eighth.png")
three_quarter_filled_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle75.png")
seven_eighth_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle-7-eighth.png")
full_bottle = tk.PhotoImage(file=r"c:\Users\rflor\Downloads\bottle100.png")

canvas = tk.Canvas(root, width=200, height=300)
canvas.pack(side='top', fill='both', expand='yes')

image_on_canvas = canvas.create_image(100, 0, image = empty_bottle, anchor='nw') #had to change the coords cus the water bottle was blocked for me



##########################################USERINPUT##########################################################################
import tkinter as tk


sum = 0
goal = 0 #goal will be depending on what the user inputs from the calculator


def submit():
    global sum,sum_percent  # made global so it can be used everywhere
    entered_oz = int(float(text_entry.get())) 
    sum += entered_oz  # Adds entered_oz to the sum
    print(sum)  #within context of the Water Tracker, instead of printing to the terminal we can have a text box w the 'sum' variable so it changes depending on inputs
    sum_percent = sum / goal if goal != 0 else 1
    
    if sum_percent < 1:
        sum_label.config(text= 'Daily Water Intake: ' + str(sum) + '   ' + 'Target Water Intake: ' + str(goal)+ '   ' + 'Progress Percentage: ' + str(float(sum_percent)*100) + '%')
    else:
        sum_label.config(text= 'Daily Water Intake: ' + str(sum) + '   ' + 'Target Water Intake: ' + str(goal)+ '   ' + 'Progress Percentage: ' + '100' + '%')
    print ('percent is:' + str(sum_percent))


def goalIntake():   #supposed to display goal as soon as its calculated, can't figure out yet
    
    sum_label = tk.Label(root, text='Daily Water Intake: '+ str(sum) + '   ' + 'Target Water Intake: ' + str(goal)+ '   ' + 'Progress Percentage: ' + str(float(sum_percent)*100) + '%')  # Label to display the sum
    sum_label.pack(pady=1) 
    print ('percent is:' + str(sum_percent))

frame1 = tk.Frame(root)
frame1.pack(pady=10)

text_label = tk.Label(frame1, text="Enter number of oz you drank:")
text_label.grid(row=0, column=0)

text_entry = tk.Entry(frame1)
text_entry.grid(row=0, column=1)

submit_button = tk.Button(root, text="Submit", command=combined_functions)
 #makes submit button work
submit_button.pack(pady=1)

sum_label = tk.Label(root, text='Daily Water Intake: '+ str(sum) + '   ' + 'Target Water Intake: ' + str(goal) + '   ' + 'Progress Percentage: ' + str(float(sum_percent)*100) + '%')  # Label to display the sum
sum_label.pack(pady=1)
print ('percent is:' + str(sum_percent))

indicator = False

if indicator == True:
    goalIntake()

Lower_left = tk.Label(root, text="Water Calculator", font=("Helvetica 15 bold"), fg="#001853") #text change position 
Lower_left.pack(pady=1)

#################################################CALCULATOR###################################################################

from tkinter import *
from tkinter import messagebox


def reset_entry():
    exercise_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_water():
    global goal, water, indicator
    lb = int(weight_tf.get()) #sets the weight variable
    e = int(float(exercise_tf.get())) #sets exercise variable
    water = (lb*(2/3))+(12*(e/30)) #water oz formula
    goal = water
    water = round(water, 1)
    water_index(water)
    
    indicator = False
    indicator = True
   

    
    

def water_index(water): #makes the popup that tells how much water u should drink, isnt necessary to have the > 0 but it was easier for me
    
    if water > 0:
        messagebox.showinfo('Water Intake Tracker', f'suggested daily hydration = {water} oz') 
        
       


water = goal
goal = water


var = IntVar()

frame = Frame(
    root,
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

exit_btn = Button( #destroys the pop up
    frame3,
    text='Exit',
    command=lambda:root.destroy()
)
exit_btn.pack(side=RIGHT)
################################################ALARM####################################################################

from tkinter import *
import datetime
import time
import winsound
from threading import *
 
 

def Threading():
    t1=Thread(target=alarm)
    t1.start()
 

from twilio.rest import Client
def alarm():
    
    while True:
        
        set_alarm_time = f"{hour.get()}:{minute.get()}" #gets the time
 
        
        time.sleep(1)
 
        
        current_time = datetime.datetime.now().strftime("%H:%M") #Hour and minute
 
        
        if current_time == set_alarm_time: #kinda self explanatory 
            

            # Your Account SID and Auth Token from console.twilio.com
            account_sid = "AC189a5cc4f644e8cb6f52b29d95e4d2fe"
            auth_token  = "3bdb0433f69c8a8d04f3603396d85da6"

            client = Client(account_sid, auth_token)

            message = client.messages.create(
            to="+19514810480",
            from_="+18332943083",
            body="it's time to hydrate!")

            print(message.sid)
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

 

Button(root,text="Set Reminder",font=("Helvetica 10"),command=Threading).pack(pady=20)


 

root.mainloop()




######################



