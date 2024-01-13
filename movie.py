from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from ast import literal_eval

df2 = pd.read_csv('datasets/tmdb_5000_movies.csv')
df2.loc[:, 'genres'] = df2.genres.apply(lambda x: ",".join(i.get('name') for i in literal_eval(x)))

class Viewmovie:
    def __init__(self, movie_id=""):
        self.root = Toplevel()
        self.root.title("Movie Details")
        self.root.resizable(False, False)
        self.root.geometry('700x400')
        try:
            self.details = df2.iloc[movie_id]
        except:
            messagebox.showwarning('Alert', 'Movie is not found.')
        self.title = Label(self.root, text=" MOVIE DETAILS",
                           font=("Georgia", 25, "bold"), bg="grey",
                           fg="white", relief=GROOVE, bd=10)  # relief is for Border Style
        self.title.pack(side=TOP, fill=X)
        
        self.name_label = Label(self.root, text=self.details["original_title"], font=("georgia", 25, "bold"), fg="#34454c")
        self.name_label.place(x=50, y=100)
        
        self.language=Label(self.root, text="Language: ", font=("georgia", 15), fg="#34454c")
        self.language.place(x=50, y=140)
        self.language_value=Label(self.root, text=self.details['original_language'], font=("georgia", 15, "bold"), fg="#34454c")
        self.language_value.place(x=160, y=140)
        self.genres=Label(self.root, text="Genres:", font=("georgia", 15), fg="#34454c")
        self.genres.place(x=50, y=170)
        self.genres_value=Label(self.root, text = self.details['genres'], font=("georgia", 15, "bold"), fg="#34454c")
        self.genres_value.place(x=150, y=170)
        
        self.releasedate=Label(self.root, text="Release Date: ", font=("georgia", 15 ), fg="#34454c")
        self.releasedate.place(x=50, y=200)
        self.release_value=Label(self.root, text=self.details["release_date"], font=("georgia", 13, "bold"), fg="#34454c")
        self.release_value.place(x=180, y=200)
        self.cast=Label(self.root, text="Runtime: ", font=("georgia", 15 ), fg="#34454c")
        self.cast.place(x=50, y=230)
        self.cast_value=Label(self.root, text=f'  {self.details["runtime"]} min.', font=("georgia", 13, "bold"), fg="#34454c")
        self.cast_value.place(x=120, y=230)
        self.root.mainloop()
        
if __name__ == '__main__':
    a = Viewmovie()