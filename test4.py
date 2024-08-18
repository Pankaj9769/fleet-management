from tkinter import *
import customtkinter as ctk

mainWindow = Tk()
mainWindow.geometry('800x500')

mainCont = Frame(mainWindow,borderwidth=2,relief='groove')
mainCont.pack(fill=BOTH,ipadx=10,ipady=10)

childCont1= Frame(mainCont, background="purple")
childCont1.pack(fill=BOTH)

vNumLab = ctk.CTkLabel(childCont1, text="Vehicle Number:", font=("Arial", 15, "bold"))
vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)

vNum = ctk.CTkLabel(childCont1, text='MH03AS8361', font=("Arial", 15))
vNum.pack(pady=5, side=LEFT)

vNameLab = ctk.CTkLabel(childCont1, text="Vehicle Name:", font=("Arial", 15, "bold"))
vNameLab.pack(padx=(25, 0), pady=5, side=LEFT)

vName = ctk.CTkLabel(childCont1, text="Skoda", font=("Arial", 15))
vName.pack(pady=5, side=LEFT)

childCont2= Frame(mainCont,background='yellow')
childCont2.pack(fill=BOTH)

vNumLab = ctk.CTkLabel(childCont2, text="Vehicle Number:", font=("Arial", 15, "bold"))
vNumLab.pack(padx=(10, 0), pady=5, side=LEFT)

vNum = ctk.CTkLabel(childCont2, text='MH03AS8361', font=("Arial", 15))
vNum.pack(pady=5, side=LEFT)

vNameLab = ctk.CTkLabel(childCont2, text="Vehicle Name:", font=("Arial", 15, "bold"))
vNameLab.pack(padx=(25, 0), pady=5, side=LEFT)

vName = ctk.CTkLabel(childCont2, text="Skoda", font=("Arial", 15))
vName.pack(pady=5, side=LEFT)

mainWindow.mainloop()