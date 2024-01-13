from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# import database


class Add_doctor:
    def __init__(self):
        self.root=Tk()
        self.root.state('zoomed')
        self.root.title("HOME")
        self.root.configure(bg='black')  # Set the background color of the parent widget (you can use any color)

      
    def addDoctorFrame(self):
        
        self.image = Image.open("m.webp")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.root,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="2000",height="1000")
        

        #self.first= Frame(self.root, bg="white")
        #self.first.place(x=0,y=0,width="900",height="600")
        
        #create and place labels 
        self.lab=Label(self.root,text="MOVIE RECOMMENDATION SYSTEM",anchor=E,bg=self.root['bg'],fg="yellow")
        self.lab.place(x=300,y=30, width="650", height="45")
        self.lab.config(font=("calibri",30,"bold"))

        #self.lab1=Label(self.first,text="Name",anchor=E,bg="white",fg="black")
        #self.lab1.place(x=450,y=100, width="80", height="30")
 #       self.lab1.config(font=("calibri",18,"bold"))
#
  #      self.lab1=Label(self.first,text="Specialist",anchor=E,bg="white",fg="black")
   #     self.lab1.place(x=433,y=150, width="100", height="30")
    #    self.lab1.config(font=("calibri",18,"bold"))
 #entries

        
        self.name=StringVar()
        self.name=Entry(self.root,textvariable=self.name)
        self.name.place(x=500,y=150,width=350,height=35)
        
        
      
        #buttons

        self.searchButton = Button(self.root, text = "Search")
        self.searchButton.place(x=630,y=250,width=100,height=40)

        #self.loginButton = Button(self.root, text = "Back")
       # self.loginButton.place(x=590,y=410,width=100,height=40)


        self.root.mainloop()

    
   # def menuWindow(self):
        self.root.destroy()
       
if __name__=='__main__':
    obj1 = Add_doctor()
    obj1.addDoctorFrame()
    
         
    
