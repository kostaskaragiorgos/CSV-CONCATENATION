from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog

import pandas as pd

class CSV_CONCATENATION():
    def __init__(self,master):
        self.concatlist =[]
        self.master = master
        self.master.title("CSV CONCATENATION")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Add for concatenation",accelerator = 'Ctrl+O',command =self.addtolist)
        self.file_menu.add_command(label="Save File",accelerator= 'Ctrl+S',command = self.savefile)
        self.file_menu.add_command(label = "Show List",accelerator = 'Ctrl+F5',command = self.showlista)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.Edit_menu = Menu(self.menu,tearoff = 0)
        self.Edit_menu.add_command(label = "Delete last insert",accelerator = 'Ctrl+Z',command = self.dellast)
        self.Edit_menu.add_command(label = "Clear list",accelerator = 'Ctrl+T',command = self.clearl)
        self.menu.add_cascade(label = "Edit",menu = self.Edit_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator = 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        
        self.master.bind('<Control-o>',lambda event:self.addtolist())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Control-z>',lambda event:self.dellast())
        self.master.bind('<Control-t>',lambda event:self.clearl())
        self.master.bind('<Control-s>',lambda event: self.savefile())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F5>',lambda event:self.showlista())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        
        self.welcomleb = Label(self.master,
                               text = "Welcome to the csv concatenation\n")
        self.welcomleb.pack()
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
    
    def dellast(self):
        if self.concatlist == []:
            msg.showerror("Error","The list is empty")
        else:
            self.concatlist.pop()
            msg.showinfo("Delete" , "Success The last element of the list has been deleted ")
        if len(self.concatlist) < 2:
            self.concatanationb.configure(state = "disable")
    
    def showlista(self):
        if self.concatlist == []:
            msg.showinfo("LIST","LIST IS EMPTY")
        else:
            msg.showinfo("LIST",self.concatlist)
    
    def clearl(self):
        self.concatlist.clear()
        self.concatanationb.configure(state = "disable")
        msg.showinfo("LIST CLEARED","THE CONCATANATION LIST IS CLEAR\n"
                             +"YOU CAN CONCATANATE NEW FILES")
    
    def aboutmenu(self):
        msg.showinfo("About","About CSV CONCATENATION \nVersion 2.0\n")
    
    def helpmenu(self):
        msg.showinfo("Help","      HELP CSV CONCATENATION\n1.PRESS THE BUTTON ADD FOR CONCATENATION TO ADD THE FILES FOR CONCATENATION\n"+
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
            if len(self.concatlist) == 1:
                self.columnsofthefirst = pandascheck.columns
                msg.showinfo("SUCCESS","THE CSV FILE "+" ADDED SUCCESSFULLY")
            if (len(self.concatlist) > 1):
                if str(pandascheck.columns) == str(self.columnsofthefirst):
                    msg.showinfo("SUCCESS","THE CSV FILE "+" ADDED SUCCESSFULLY")
                else:
                    self.concatlist.pop()
                    msg.showerror("ERROR", "THE CSV FILE MUST HAVE THE SAME COLUMN NAME AS THE FIRST INSERTED FILE")
        else: 
            msg.showerror("Error","NO CSV FILE ADDED")
        if len(self.concatlist) >= 2:
            self.concatanationb.configure(state="active")
            
    def concatanation(self):
        if self.varnumset.get() == "Horizontal":
            concatdf = pd.concat(self.concatlist,axis=1)
            filenamesave =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            if '.csv' in filenamesave:
                msg.showinfo("SUCCESS","THE CSV FILE CREATED SUCCESSFULLY")
                concatdf.to_csv(filenamesave,index = False)
                self.concatlist.clear()
                self.concatanationb.configure(state = "disable")
                msg.showinfo("LIST CLEARED","THE CONCATANATION LIST IS CLEAR\n"
                             +"YOU CAN CONCATANATE NEW FILES")
            else:
                msg.showerror("ERROR","NO FILE SAVED")
        else:
            concatdf2 = pd.concat(self.concatlist,axis = 0)
            filenamesave =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            if '.csv' in filenamesave:
                msg.showinfo("SUCCESS","THE CSV FILE CREATED SUCCESSFULLY")
                concatdf2.to_csv(filenamesave,index = False)
                self.concatlist.clear()
                self.concatanationb.configure(state = "disable")
                msg.showinfo("LIST CLEARED","THE CONCATANATION LIST IS CLEAR\n"
                             +"YOU CAN CONCATANATE NEW FILES")
            else:
                msg.showerror("ERROR","NO FILE SAVED")
                
    def savefile(self):
        if len(self.concatlist) >= 2:
            self.concatanation()
        else:
            msg.showerror("SAVE ERROR","INSERT MORE FILES")
            
def main():
    root=Tk()
    CC = CSV_CONCATENATION(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
