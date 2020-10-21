from tkinter import *
import AttendanceProject as ap
window = Tk()
window.title('Automatic Attendance System')
lbl = Label(window,text='AUTOMATIC FACE RECOGNITION \n ATTENDANCE SYSTEM',font=("Helvetica", 16 , 'bold'))
lbl.place(x=75, y=50)

lbl2 = Label(window,text='Face recognition attendance system, let you mark attendance on the \nclick of button.\n'
                         'To get started, click Instructions.',font=("Helvetica", 8))
lbl2.place(x=75, y=100)

start=Button(window, text="Start", command=lambda : ap.start(), fg='blue')
register=Button(window, text="Register",command=lambda : ap.register(), fg='blue')
delete=Button(window, text="Delete",command=lambda : ap.deleteEntry(), fg='blue')
instruction=Button(window,text="Instructions",fg='blue')

start.place(x=50, y=200,width=50)
register.place(x=150, y=200,width=50)
delete.place(x=250, y=200,width=50)
instruction.place(x=350,y=200,width=80)


window.geometry("480x300")
window.resizable(False, False)
window.mainloop()