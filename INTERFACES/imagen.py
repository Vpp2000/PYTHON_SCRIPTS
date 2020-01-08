import tkinter as tk  
from PIL import Image,ImageTk  
root = tk.Tk()  
root.title("display image")  
im=Image.open("logo.png")  
photo=ImageTk.PhotoImage(im)  
cv = tk.Canvas()  
cv.pack(side='top', fill='both', expand='yes')  
cv.create_image(5, 5, image=photo, anchor='nw')  
root.mainloop()
