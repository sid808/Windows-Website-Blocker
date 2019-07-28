from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import sys
import os
website_list = []
website=" "        
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
def show_data():
    site= var_chk.get()   
    if site == 1:
        website="www.facebook.com"
        website_list.append(website)
    elif site == 2:
        website="www.twitter.com"
        website_list.append(website)
    elif site == 3:
        website="www.youtube.com"
        website_list.append(website)
    elif site == 4:
        website="locksicker.com"
        website_list.append(website)
    tkinter.messagebox.showinfo("Message","Website Added Sucessfully")
        
def block():
    with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list: 
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
                tkinter.messagebox.showinfo("Message","Website Blocked Sucessfully")
def unblock():
     with open(hosts_path, 'r+') as file:
                content = file.readlines() 
                file.seek(0) 
                for line in content:
                    if not any(website in line for website in website_list): 
                        file.write(line)
                    file.truncate()
                tkinter.messagebox.showinfo("Message","Fun hours ... Enjoy")

def helloCallBck():
    os.system('python siteblocker.py')
    
def about():
    tkinter.messagebox.showinfo("About"," Site Blocker App \n Designed In Python \n Suggestions Are Welcomed")

def bye():
         root.destroy();

def reach():
    tkinter.messagebox.showinfo("Contact Us","\nSiddharth : aadarsh.siddharth@gmail.com\n")

root = Tk()
root.geometry("850x650")
root.title("SiteBlockingApp")
var_chk = IntVar()

background_img = PhotoImage(file = "image3.png")
background_lb = Label (root, image = background_img)
background_lb.place(x=0, y =0, relheight=1, relwidth=1)

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="About",command=about)
submenu.add_separator()
submenu.add_command(label="Exit",command=bye)

menu.add_cascade(label="Reach Us",command=reach)


label_0 = Label(root, text="Website  Blocker",width=15,font=("bold", 50) , bg ="black", fg="yellow")
label_0.place(x=135,y=45)
l1 = Label(root, text=" List of Website(select 1 at a time) :", bg="black", fg="white", width=30,font=("bold", 20) )
l1.place(x=165,y=200)
l2 = Label(root, text="What do you want?", bg="black", fg="white",width=25,font=("bold", 20))
l2.place(x=165, y=450)

ch1= Radiobutton(root, text="Facebook", variable=var_chk, value=1 ,width=8,font=("bold",12))
ch1.place(x=165,y=250)
ch2= Radiobutton(root, text="Twitter ", variable=var_chk, value=2, width=8, font=("bold",12))
ch2.place(x=295,y=250)
ch3= Radiobutton(root, text="Youtube ", variable=var_chk, value=3, width=8, font=("bold",12))
ch3.place(x=425,y=250)
ch4= Radiobutton(root, text="Locksicker", variable=var_chk, value=4 , width=8,font=("bold",12))
ch4.place(x=555,y=250)
ch5= Button(root, text="Submit " ,width=8,font=("bold",12),command=show_data)
ch5.place(x=350,y=350)
ch6= Button(root, text="Block ",width=8,font=("bold",12), command=block)
ch6.place(x=170,y=530)
ch7= Button(root, text="Unblock " ,width=8, font=("bold",12), command=unblock) 
ch7.place(x=480,y=530)
ch8= Button(root, text="Other... ",width=8, font=("bold",12),command=helloCallBck )
ch8.place(x=550,y=350)

root.mainloop()
