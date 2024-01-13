from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
#import menu
#import database
import database, chooseGenres
import login

class Register:
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
        self.lab=Label(self.first,text=" USER REGISTER",anchor=E,bg="white",fg="black")
        self.lab.place(x=1020,y=120, width="270", height="45")
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
        self.specialist=Entry(self.first,textvariable=self.specialist, show='*')
        self.specialist.place(x=1100,y=350,width=210,height=30)

        
        
        #buttons

        self.loginButton = Button(self.first, text = "Submit", command = self.addDoctor)
        self.loginButton.place(x=1030,y=410,width=100,height=40)

        # self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        # self.loginButton.place(x=1100,y=410,width=100,height=40)


        self.root.mainloop()

    
    def addDoctor(self):
        data = (
            self.name.get(),
            self.specialist.get(),
        )
        if self.name.get() == '':
            messagebox.showinfo('Alert', 'Please enter name first')

        elif self.specialist.get() == "":
            messagebox.showinfo('Alert','Please enter password')

        else:
            res = database.registerUser((self.name.get(), self.specialist.get())) 
            if res:
                messagebox.showinfo('Saved', 'Register Successfully')
                self.root.destroy() 
                login.Add_doctor()
                
            else:
                messagebox.showerror('Alert', 'Something went wrong. Please try again.')

        

    def menuWindow(self):
        self.root.destroy()
        # obj = menu.AdminNav()
        # obj.navframe()

if __name__=='__main__':

     Register()
    # obj1.addDoctorFrame()
    
         
    
