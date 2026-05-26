
import tkinter as tk

root = tk.Tk()
root.title("Solver")
root.attributes(fullscreen= True)
canvas = tk.Canvas(root, bg="black")
canvas.pack(fill="both", expand=True)
center_x = root.winfo_screenwidth() // 2
center_y = root.winfo_screenheight() // 2
r = 200
circle = canvas.create_oval( center_x-r,center_y-r,center_x+r,center_y+r, fill="black",outline="orange", width=10)
r = 50
label = tk.Label(root,text="roman",fg="orange",bg="black")
label.place(x=center_x, y=center_y, anchor="center")
root.mainloop()