from tkinter import *
from tkinter import messagebox as msg
import csv
import pandas as pd
from tkinter import filedialog
class CSV_CONCATENATION():
    def __init__(self,master):
        self.concatlist =[]
        self.master = master
        self.master.title("CSV CONCATENATION")
        self.master.geometry("200x200")
        self.master.resizable(False,False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Exit",command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        self.master.config(menu=self.menu)
        self.addtoconcatlist = Button(self.master,text = "ADD FOR CONCATENATION"
                                      ,command = self.addtolist)
        self.addtoconcatlist.pack()
        self.concatanationb = Button(self.master,text = "CONCATENATION",
                                     command = self.concatanation)
        self.concatanationb.pack()
    def exitmenu(self):
        pass
    def file_menu(self):
        pass
    
        
    def addtolist(self):
        filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        print(filename)
        if ".csv" in filename:
            pandascheck = pd.read_csv(filename)
            self.concatlist.append(pandascheck)
    def concatanation(self):
        print(self.concatlist)
        concatdf = pd.concat(self.concatlist,axis=1)
        concatdf.to_csv("concat.csv",index = False)
def main():
    root=Tk()
    CC = CSV_CONCATENATION(root)
    root.mainloop()
    
if __name__=='__main__':
    main()