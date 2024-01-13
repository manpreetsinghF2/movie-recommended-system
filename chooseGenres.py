from tkinter import *
import customtkinter
import getMovies, movie
from tkinter import messagebox
import register

class ChooseGenres():
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        # self.root.geometry('1300x150')
        self.root.configure(bg='white')

        # self.trending = Label(self.root, text='Trending Movies')
        # self.trending.place(x = 10, y = 10)

        lbl_product_url = Label(self.root,text="Search",font=("times new roman ", 10, "bold"),bg="white",fg = "black").place(x=50,y=20)

        self.text_product_url = Entry(self.root,font=("times new roman ", 10),bg="light yellow",fg = "black", width= 80)
        self.text_product_url.place(x=150,y=20)
        
        btn_connector = Button(self.root, text="Search ", font=("rubik", 10, "bold"), bg = 'blue', fg='white', command = self.search).place(x=950,y = 20)
        btn_connector1 = Button(self.root, text="Exit ", font=("rubik", 10, "bold"), bg = 'blue', fg='white', command = self.menuWindow).place(x=1050,y = 20)

        self.frame = customtkinter.CTkScrollableFrame(self.root, orientation=HORIZONTAL, width=1300, height=50, label_text = 'Popular Movies', label_text_color = 'purple', label_anchor = 'n')
        # self.frame = Frame(self.root, width = 1300, height=150)
        self.frame.place(x = 10, y = 200)

        self.trending = getMovies.getTrendingMovies('all')
        for index, row in self.trending.iterrows():
            # print('index is ', index)
            btn = customtkinter.CTkButton(self.frame, text = f"{row['title']}\n\n{row['tagline']}", command = lambda index = row: self.getDetail(index)).pack(padx = 10, side=LEFT)

        
        self.frame1 = customtkinter.CTkScrollableFrame(self.root, orientation=HORIZONTAL, width=1300, height=50, label_text='Trending Movies')
        self.frame1.place(x = 10, y = 370)

        self.popular = getMovies.getPopularMovies()
        for index, row in self.popular.iterrows():
            btn = customtkinter.CTkButton(self.frame1, text = f"{row['title']}\n\n{row['tagline']}", command = lambda index = row: self.getDetail(index)).pack(padx = 10, side=LEFT)

        
        self.frame2 = customtkinter.CTkScrollableFrame(self.root, orientation=HORIZONTAL, width=1300, height=50, label_text='Popular Action Movies')
        self.frame2.place(x = 10, y = 540)

        self.popular = getMovies.getTrendingMovies('action')
        for index, row in self.popular.iterrows():
            btn = customtkinter.CTkButton(self.frame2, text = f"{row['title']}\n\n{row['tagline']}", command = lambda index = row: self.getDetail(index)).pack(padx = 10, side=LEFT)

        self.root.mainloop()

    def search(self):
        self.searchMovies = getMovies.getContentRecommend(self.text_product_url.get())
        print(self.searchMovies)
        if self.searchMovies.size:
            self.frame3 = customtkinter.CTkScrollableFrame(self.root, orientation=HORIZONTAL, width=1300, height=50, label_text='Search Results')
            self.frame3.place(x = 10, y = 50)

            for index, row in self.searchMovies.iterrows():
                btn = customtkinter.CTkButton(self.frame3, text = f"{row['title']}\n\n{row['tagline']}", command = lambda index = row: self.getDetail(index)).pack(padx = 10, side=LEFT)
        else:
            messagebox.showwarning('Alert', 'Movie not found')

    def getDetail(self, ind):
        print(ind.name)
        movie.Viewmovie(ind.name)
    def menuWindow(self):
        self.root.destroy()
        obj = register.Register()
        

if __name__ == '__main__':
    ChooseGenres()