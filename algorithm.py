from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image

app = Tk()
app.geometry('200x200')
app.resizable(0,0)
app.title("CONVERT ANY IMAGE TO ANY FORMAT")
img = PhotoImage(file="indir.png")
width, height = img.width(), img.height()
canvas = Canvas(app, width=width, height=height)
canvas.place(x=0,y=0)
canvas.create_image((0, 0), image=img, anchor="nw")

checkformat = IntVar()
checkformat.set(1)

checkpng = ttk.Radiobutton(app,text="CONVERT TO PNG",variable=checkformat,value=1).pack()
checkjpg = ttk.Radiobutton(app,text="CONVERT TO JPG",variable=checkformat,value=2).pack()
checkjpeg = ttk.Radiobutton(app,text="CONVERT TO JPEG",variable=checkformat,value=3).pack()



def process(extension):
        try:
            fileExtension = str(extension)
            source = getSource()
            im = Image.open(source)
            rgb_im = im.convert("RGB")
            target = f"{getTarget()}"+"/output."+fileExtension
            rgb_im.save(target)
            messagebox.showinfo("IMAGE CONVERTER",f"Donusturme islemi basarili\nKaydedilen dizin:\n{target}")
        except Exception as e:
            messagebox.showerror("Hata Desteklenmeyen format",f"{e}")

def getSource():
    return filedialog.askopenfilename()

def getTarget():
    return filedialog.askdirectory()

def convert():
    
    checker = checkformat.get()
    if checker==1:
        process("png")
    elif checker==2:
        process("jpg")
    else:
        process("jpeg")

button = ttk.Button(app,text="CONVERT",command=convert).place(x=63,y=110)
app.mainloop()