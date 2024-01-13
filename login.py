from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
#import menu
import database
import database, chooseGenres
import register


class Add_doctor:
    def __init__(self):
        self.root=Tk()
        self.root.state('zoomed')
        self.root.title("login window")
        self.root.configure(bg='white')
        # self.root.mainloop()
        
    # def addDoctorFrame(self):
        self.first= Frame(self.root, bg="black")
        self.first.place(x=0,y=0,width="1366",height="800")
        
        self.image = Image.open("kp.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="890",height="780")
        
   
        #create and place labels 
        self.lab=Label(self.first,text=" USER LOGIN",anchor=E,bg="white",fg="black")
        self.lab.place(x=1020,y=120, width="210", height="45")
        self.lab.config(font=("calibri",30,"bold"))

        self.lab1=Label(self.first,text="USERNAME",anchor=E,bg="white",fg="black")
        self.lab1.place(x=890,y=300, width="130", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="PASSWORD",anchor=E,bg="white",fg="black")
        self.lab1.place(x=890,y=350, width="130", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        #entries

        
        self.name=StringVar()
        self.name=Entry(self.first,textvariable=self.name)
        self.name.place(x=1100,y=300,width=210,height=30)
        
        
        self.specialist=StringVar()
        self.specialist=Entry(self.first,textvariable=self.specialist)
        self.specialist.place(x=1100,y=350,width=210,height=30)

        
        
        #buttons

        self.loginButton = Button(self.first, text = "Submit", command = self.addDoctor)
        self.loginButton.place(x=950,y=410,width=100,height=40)

        self.loginButton = Button(self.first, text = "Register", command = self.menuWindow)
        self.loginButton.place(x=1100,y=410,width=100,height=40)


        self.root.mainloop()

    
    def addDoctor(self):
        data = (
            self.name.get(),
            self.specialist.get(),
        )
        if self.name.get() == '':
            messagebox.showinfo('Alert', 'Please enter username first')

        elif self.specialist.get() == "":
            messagebox.showinfo('Alert','Please enter password')    
        else:
            res = database.loginUser((self.name.get(), self.specialist.get()))
            if res:
                self.root.destroy()
                chooseGenres.ChooseGenres()
            else:
                messagebox.showerror('Alert', 'Invalid username/password.')

    def menuWindow(self):
        self.root.destroy()
        obj = register.Register()
        # obj.navframe()

if __name__=='__main__':
    Add_doctor()
    # obj1.addDoctorFrame()
    
         
    
