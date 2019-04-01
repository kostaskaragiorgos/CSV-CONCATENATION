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
        
        self.about_menu = Menu(self.menu)
        self.about_menu.add_command(label = "About",command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu)
        self.help_menu.add_command(label = "Help",command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.addtoconcatlist = Button(self.master,text = "ADD FOR CONCATENATION"
                                      ,command = self.addtolist)
        self.addtoconcatlist.pack()
        setslist = list(["Horizontal","Vertical"])
        self.varnumset = StringVar(master)
        self.varnumset.set(setslist[0])
        self.popupsetmenu = OptionMenu(self.master,self.varnumset,*setslist)
        self.popupsetmenu.pack()
        self.concatanationb = Button(self.master,text = "CONCATENATION",state="disable",
                                     command = self.concatanation)
        self.concatanationb.pack()
    
    def aboutmenu(self):
        msg.showinfo("About","About CSV CONCATENATION \nVersion 1.0\n")
    
    def helpmenu(self):
        msg.showinfo("Help","Help CSV CONCATENATION\n1.PRESS THE BUTTON ADD FOR CONCATENATION TO ADD THE FILES FOR CONCATENATION\n"+
                     "2.CHOOSE VERTICAL OR HORIZONTAL\n3.PRESS THE CONCATENATION BUTTON TO SAVE THE NEW CSV FILE")
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
        
    def addtolist(self):
        filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        
        if ".csv" in filename:
            pandascheck = pd.read_csv(filename)
            self.concatlist.append(pandascheck)
            msg.showinfo("SUCCESS","THE CSV FILE ADDED SUCCESSFULLY")
        if len(self.concatlist) >= 2:
            self.concatanationb.configure(state="active")
            
    def concatanation(self):
        if self.varnumset.get() == "Horizontal":
            concatdf = pd.concat(self.concatlist,axis=1)
            filenamesave =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            if ".csv" in filenamesave:
                msg.showinfo("SUCCESS","THE CSV FILE CREATED SUCCESSFULLY")
                concatdf.to_csv(filenamesave,index = False)
            else:
                msg.showerror("ERROR","NO FILE SAVED")
        else:
            concatdf2 = pd.concat(self.concatlist,axis = 0)
            filenamesave =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            if ".csv" in filenamesave:
                msg.showinfo("SUCCESS","THE CSV FILE CREATED SUCCESSFULLY")
                concatdf2.to_csv(filenamesave,index = False)
            else:
                msg.showerror("ERROR","NO FILE SAVED")
        
def main():
    root=Tk()
    CC = CSV_CONCATENATION(root)
    root.mainloop()
    
if __name__=='__main__':
    main()