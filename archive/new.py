import tkinter as tk
from twilio.rest import Client

pnumber = " "


account_sid = "AC189a5cc4f644e8cb6f52b29d95e4d2fe"
auth_token  = "3bdb0433f69c8a8d04f3603396d85da6"


def send_message():
    global pnumber
    pnumber = number.get()
    
    if not pnumber.strip():
        print("Please enter a valid phone number.")
        return
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="DRINK WATER",
        from_="+18332943083",
        to='+' + pnumber
    )

root = tk.Tk()

label = tk.Label(root, text='Enter your phone number')
number = tk.Entry(root)
number.focus_set()



send_text = tk.Button(root, text='Send Message', command=send_message)
send_text.pack(side='bottom')

label.pack(side = tk.TOP)
number.pack()

root.mainloop()
