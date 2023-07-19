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



popup = tk.Tk()
popup.title("Popup Window")

text_label = tk.Label(popup, text="Enter Number of Oz you drank:")
text_label.pack()

text_entry = tk.Entry(popup)
text_entry.pack()

submit_button = tk.Button(popup, text="Submit", command=submit)
submit_button.pack()

popup.mainloop()

