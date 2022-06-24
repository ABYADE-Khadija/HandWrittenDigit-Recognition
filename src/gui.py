import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageGrab
from PIL import Image, ImageTk
from tkinter import filedialog
import brainCNN



class main:

    def __init__(self, master):
        self.master=master
        self.res = ""
        self.pre = [None, None]
        self.bs = 4
        self.frame1 = tk.Frame(master, width=195, height=500, bg="purple")
        self.frame1.pack(fill=tk.Y, side=tk.LEFT)

        
        #frame0
        self.frame0 = tk.Frame(master, width=195, height=500, bg="white")
        self.frame0.pack(fill=tk.Y, side=tk.LEFT)
        self.label4 = tk.Label(
            master=self.frame0,text="Welecome in HandWitten Digit Recognition",
            fg="black",bg="white",width=50,font='Helvetica 16 bold'
        )
        self.label4.pack()

        image1 = Image.open(".\mok2.png")
        print(image1)
        image1 = image1.resize((700, 420), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        print(test)
        self.label1 = tk.Label(master=self.frame0,image=test,bg="white")
        self.label1.image = test
        self.label1.pack()

        self.label2 = tk.Label(
            master=self.frame0,text="By:: Khadija & Soukaina & Dounia   ",
            fg="black",bg="white",width=50,font='Helvetica 14 '
        )
        self.label2.pack()


        self.frame3 = tk.Frame(master, width=650, height=500, bg="white")
        label0 = tk.Label(
            master=self.frame3,text="Digit Recognition Python MNIST",
            fg="black",bg="white",width=50,font='Helvetica 18 bold'
        )
        self.buttonCl = tk.Button(
            master=self.frame3, text="Clear",command=self.clearFile,
            width=15,height=2, bg="white",fg="black",font='Helvetica 10'
        )
        self.buttonU = tk.Button(
            master=self.frame3,text="Uplaod",command=self.uploadFile ,
            width=15,height=2,bg="purple",fg="white",font='Helvetica 10'
        )
        self.buttonPr = tk.Button(
            master=self.frame3, text="Predict", command=self.predict,
            width=15, height=2, bg="purple", fg="white", font='Helvetica 10'
        )
        self.labelPredctionImg = tk.Label(
            master=self.frame3, text=" ", height=2, width=15,
            fg="black", font='Helvetica 12 '
        )
        label0.pack()

        self.buttonCl.place(x=80,y=420)
        self.buttonU.place(x = 230, y = 420)
        self.buttonPr.place(x = 380, y = 420)
        self.labelPredctionImg.place(x=530,y=420)
        self.img_LabelFrame = tk.LabelFrame(self.frame3, text="Upload image",bg="white")

        #frame1
        button0= tk.Button(master=self.frame1,text="Home",width=24,height=2,
            bg="white",fg="purple",font='Helvetica 10 ',bd=0,command=self.hide1)
        button0.place(x = 0, y = 100)
        button1 = tk.Button(master=self.frame1,text="Draw",width=24,height=2,
            bg="purple",fg="white",font='Helvetica 10 ',bd=0,command=self.hide2)
        button1.place(x = 0, y = 150)
        button2 = tk.Button(master=self.frame1,text="Upload",width=24,height=2,
            bg="purple",fg="white",font='Helvetica 10 ',bd=0,command=self.hide3)
        button2.place(x = 0, y = 200)
        
        #frame2
        self.frame2 = tk.Frame(master=self.frame0, width=200, bg="white")
        #self.frame2.pack(fill=tk.Y, side=tk.LEFT)
        self.labelPredction = tk.Label(
            master=self.frame2,text="resultat",height=2,width=15,
            fg="black",font='Helvetica 12 ')


        label = tk.Label(
            master=self.frame2,text="Digit Recognition Python MNIST",
            fg="black",bg="white",width=50,font='Helvetica 18 bold'
        )
        self.button = tk.Button(
            master=self.frame2,text="Predict", command=self.predict,
            width=15,height=2,bg="purple",fg="white",font='Helvetica 10'
        )
        self.buttonC = tk.Button(
            master=self.frame2, text="Clear",command=self.clear,
            width=15,height=2, bg="white",fg="black",font='Helvetica 10'
        )
        self.c = Canvas(master=self.frame2,bd=3,relief="ridge",width=600, height=300, bg='white')
        label.pack()
        self.c.bind("<Button-1>", self.putPoint)
        self.c.bind("<B1-Motion>", self.paint)


        self.c.place(x = 70, y = 70)
       
        self.buttonC.place(x = 100, y = 400)
        self.button.place(x = 300, y = 400) 
        self.labelPredction.place(x = 500, y = 400)

       #self.c.bind("<ButtonRelease-1>",self.getResult)
       

    def clear(self):
        self.c.delete('all')
        self.labelPredction.config(text="")

    def hide1(self):
        self.frame0.pack(fill=tk.Y, side=tk.LEFT)
        self.img_LabelFrame.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.label4.pack()
        self.label1.pack()
        self.label2.pack()
        
   
    def hide2(self):
        self.frame3.pack_forget()
        self.frame2.pack(fill=tk.Y, side=tk.LEFT)
        self.frame0.pack(fill=tk.Y, side=tk.LEFT)
        self.label2.pack_forget() 
        self.label1.pack_forget()
        self.label4.pack_forget()


    def hide3(self):
        self.frame2.pack_forget()
        self.label1.pack_forget()
        self.frame0.pack_forget()
        self.frame3.pack(fill=tk.Y, side=tk.LEFT)
        self.img_LabelFrame.place(x=100,y=100, width=550,height=300)

    def uploadFile(self):
        filename = filedialog.askopenfilename(initialdir =  "/", 
        title = "Select an Image", 
        filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
        image = Image.open(filename)   
        resize_image = image.resize((200, 250))
        show_img = ImageTk.PhotoImage(resize_image)
        var_photo = Label(self.img_LabelFrame,image=show_img,bg="white")
        var_photo.image = show_img
        var_photo.pack()
        self.predictImage(filename)


    def clearFile(self):
        for widget in self.img_LabelFrame.winfo_children():
            widget.destroy()

    def predict(self):
        #self.labelPredction.config(text="2")
        self.getResult(self)


    def predictImage(self,src):
        print(src)
        self.res = str(brainCNN.predict(src))
        self.labelPredctionImg['text'] = "Pred : " + self.res

    def getResult(self,e):
        x = self.c.winfo_rootx() + self.c.winfo_x()
        y = self.c.winfo_rooty() + self.c.winfo_y()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()
        img = PIL.ImageGrab.grab()
        img = img.crop((x, y, x1, y1))
        img.save("dist.png")
        self.res = str(brainCNN.predict("dist.png"))
        self.labelPredction['text'] = "Pred : " + self.res

    def putPoint(self, e):
        self.c.create_oval(e.x - self.bs, e.y - self.bs, e.x + self.bs, e.y + self.bs, outline='black', fill='black')
        self.pre = [e.x, e.y]

    def paint(self, e):
        self.c.create_line(self.pre[0], self.pre[1], e.x, e.y, width=self.bs * 2, fill='black', capstyle=ROUND,
                           smooth=TRUE)
        self.pre = [e.x, e.y]


if __name__ == "__main__":
    root = Tk()
    main(root)
    root.title('Digit Classifier')
    root.resizable(0, 0)
    root.mainloop()
