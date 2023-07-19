from tkinter import *
from tkinter import messagebox

def reset_entry():
    exercise_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_water():
    lb = int(weight_tf.get())
    e = int(exercise_tf.get())
    water = (lb*2/3)+(12*e/30)
    water = round(water, 1)
    water_index(water)

def water_index(water):
    
    if water > 0:
        messagebox.showinfo('Water Intake Tracker', f'suggested daily hydration = {water} oz') 

ws = Tk()
ws.title('Water Intake Tracker Calculator')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
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

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

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
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
