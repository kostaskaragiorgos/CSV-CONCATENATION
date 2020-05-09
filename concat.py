"""
You can concat your csv files
"""
from tkinter import Menu, Tk, Label, Button, OptionMenu
from tkinter import messagebox as msg, StringVar
from tkinter import filedialog
import pandas as pd
def aboutmenu():
    """ about menu """
    msg.showinfo("About", "About CSV CONCATENATION \nVersion 2.0\n")
def helpmenu():
    """ help menu """
    msg.showinfo("Help", "HELP CSV CONCATENATION\n1."+
                 "PRESS THE BUTTON ADD FOR CONCATENATION TO ADD THE FILES FOR CONCATENATION\n"+
                 "2.CHOOSE VERTICAL OR HORIZONTAL\n3."+
                 "PRESS THE CONCATENATION BUTTON TO SAVE THE NEW CSV FILE")
class CsvConcatenation():
    """ csv concatenation class"""
    def __init__(self, master):
        self.concatlist = []
        self.master = master
        self.master.title("CSV CONCATENATION")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.menu = Menu(self.master)
        # menu 
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Add for concatenation",
                                   accelerator='Ctrl+O', command=self.addtolist)
        self.file_menu.add_command(label="Concatenation", accelerator='Ctrl+S', command=self.savefile)
        self.file_menu.add_command(label="Show List", accelerator='Ctrl+F5', command=self.showlista)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Delete first insert",
                                   accelerator='Ctrl+F', command=self.delfirst)
        self.edit_menu.add_command(label="Delete last insert",
                                   accelerator='Ctrl+Z', command=self.dellast)
        self.edit_menu.add_command(label="Clear list", accelerator='Ctrl+T', command=self.clearl)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        #keybinds
        self.master.config(menu=self.menu)
        self.master.bind('<Control-f>', lambda event: self.delfirst())
        self.master.bind('<Control-o>', lambda event: self.addtolist())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-z>', lambda event: self.dellast())
        self.master.bind('<Control-t>', lambda event: self.clearl())
        self.master.bind('<Control-s>', lambda event: self.savefile())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F5>', lambda event: self.showlista())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.welcomleb = Label(self.master,
                               text="Welcome to the csv concatenation\n")
        self.welcomleb.pack()
        self.addtoconcatlist = Button(self.master, text="ADD FOR CONCATENATION",
                                      command=self.addtolist)
        self.addtoconcatlist.pack()
        setslist = list(["Horizontal", "Vertical"])
        self.varnumset = StringVar(master)
        self.varnumset.set(setslist[0])
        self.popupsetmenu = OptionMenu(self.master, self.varnumset, *setslist)
        self.popupsetmenu.pack()
        self.concatanationb = Button(self.master, text="CONCATENATION", state="disable",
                                     command=self.concatanation)
        self.concatanationb.pack()
    def delfirst(self):
        """ deletes the first element of the list """
        if not self.concatlist:
            msg.showerror("Error", "The list is empty")
        else:
            self.concatlist.pop(0)
            msg.showinfo("Delete", "Success The first element of the list has been deleted ")
        if len(self.concatlist) < 2:
            self.concatanationb.configure(state="disable")
    def dellast(self):
        """ deletes last element of the list """
        if not self.concatlist:
            msg.showerror("Error", "The list is empty")
        else:
            self.concatlist.pop()
            msg.showinfo("Delete", "Success The last element of the list has been deleted ")
        if len(self.concatlist) < 2:
            self.concatanationb.configure(state="disable")
    def showlista(self):
        """ shows the list of files """
        if not self.concatlist:
            msg.showinfo("LIST", "LIST IS EMPTY")
        else:
            msg.showinfo("LIST", self.concatlist)
    def clearl(self):
        """ clears the list """
        self.concatlist.clear()
        self.concatanationb.configure(state="disable")
        msg.showinfo("LIST CLEARED", "THE CONCATANATION LIST IS CLEAR\n"
                     +"YOU CAN CONCATANATE NEW FILES")
    def exitmenu(self):
        """ exit menu function"""
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def concat(self, axis):
        """ concatanation button"""
        concatdf = pd.concat(self.concatlist, axis=axis)
        filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                            filetypes=(("csv files", "*.csv"),
                                                                    ("all files", "*.*")))
        if '.csv' in filenamesave:
            msg.showinfo("SUCCESS", "THE CSV FILE CREATED SUCCESSFULLY")
            concatdf.to_csv(filenamesave, index=False)
            self.concatlist.clear()
            self.concatanationb.configure(state="disable")
            msg.showinfo("LIST CLEARED", "THE CONCATANATION LIST IS CLEAR\n"
                                +"YOU CAN CONCATANATE NEW FILES")
        else:
            msg.showerror("ERROR", "NO FILE SAVED")
    def addtolist(self):
        """ adds file to list """
        filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                              filetypes=(("csv files", "*.csv"),
                                                         ("all files", "*.*")))
        if ".csv" in filename:
            pandascheck = pd.read_csv(filename)
            self.concatlist.append(pandascheck)
            if len(self.concatlist) == 1:
                self.columnsofthefirst = pandascheck.columns
                msg.showinfo("SUCCESS", "THE CSV FILE "+" ADDED SUCCESSFULLY")
            else:
                self.concatanationb.configure(state="active")
                if str(pandascheck.columns) == str(self.columnsofthefirst):
                    msg.showinfo("SUCCESS", "THE CSV FILE "+" ADDED SUCCESSFULLY")
                else:
                    self.concatlist.pop()
                    msg.showerror("ERROR", "THE CSV FILE MUST HAVE"+
                                  "THE SAME COLUMN NAME AS THE FIRST INSERTED FILE")
        else: 
            msg.showerror("Error", "NO CSV FILE ADDED")      
    def concatanation(self):
        """ concatanation button function """ 
        if self.varnumset.get() == "Horizontal":
            self.concat(axis=1)
        else:
            self.concat(axis=0)
    def savefile(self):
        """ saves the new file """
        if len(self.concatlist) >= 2:
            self.concatanation()
        else:
            msg.showerror("SAVE ERROR", "INSERT MORE FILES")
def main():
    """ main function """
    root = Tk()
    CsvConcatenation(root)
    root.mainloop()
if __name__ == '__main__':
    main()
