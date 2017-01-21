import Tkinter
import tkMessageBox
from tkFileDialog import askopenfilename
from Phase1_codes import Phase1
from Phase2_codes import Phase2
import os
from ttk import *

top = Tkinter.Tk()
top.style = Style()
top.style.theme_use("default")
top.configure(background="#a1dbcd")
top.title("Ecommerce Tool")
global lblInst
lblInst = Tkinter.Label(top, text="Please load test data first:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
#and pack it into the window
lblInst.pack()
def loadTestData():
	global filename
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	filename=filename.replace("/", "\\")
	lblInst.config(text="Data Loaded")
	lblInst2 = Tkinter.Label(top, text=filename+" loaded:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 8))
	lblInst2.pack()
	C.config(state='normal')
	F.config(state='normal')


def loadP1():
	Phase1.phase1(filename)
	lblInst2 = Tkinter.Label(top, text="Phase 1 Complete:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 8))
	lblInst2.pack()
	D.config(state='normal')

	

def loadP2():
	Phase2.phase2()
	lblInst2 = Tkinter.Label(top, text="Phase 2 Complete:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 8))
	lblInst2.pack()
	E.config(state='normal')


def results():
	os.startfile('Phase2_data/itemsboughtinsession.csv')

def visualize():
	os.startfile('profile.html')

B = Tkinter.Button(top, text ="Test File", command = loadTestData, fg="#a1dbcd", bg="#383a39",width = 20)
C = Tkinter.Button(top, text ="Phase 1", command = loadP1,fg="#a1dbcd", bg="#383a39",width = 20)
D = Tkinter.Button(top, text ="Phase 2", command = loadP2,fg="#a1dbcd", bg="#383a39",width = 20)
E = Tkinter.Button(top, text ="Prediction", command = results,fg="#a1dbcd", bg="#383a39",width = 20)
F= Tkinter.Button(top, text ="Visualize", command = visualize,fg="#a1dbcd", bg="#383a39",width = 20)
C.config(state='disabled')
D.config(state='disabled')
E.config(state='disabled')
F.config(state='disabled')
B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
top.mainloop()