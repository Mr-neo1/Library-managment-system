from tkinter import*


class LibraryManagmentSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Managment System")
        self.root.geometry("1550x800+0+0")


        lbltitle=Label(self.root,text="LIBRARY MANAGMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue",pady=6)
        frame.place(x=0,y=130, width=1530, height=400)

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("arial",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        DataFrameRight=LabelFrame(frame,bd=12,padx=20,relief=RIDGE,bg="powder blue",font=("arial",12,"bold"),text="Book Details")
        DataFrameRight.place(x=910,y=5,width=540,height=350)
        
        #===========================Bottons frame ===================================================
        framebutton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0,y=530, width=1530, height=70)

        #======================================Information Frame =====================================
        framebutton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0,y=600, width=1530, height=195)
        



if __name__ == "__main__":
   root=Tk()
   obj=LibraryManagmentSystem(root)
   root.mainloop()

   