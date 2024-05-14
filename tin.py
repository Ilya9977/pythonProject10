import tkinter as tk
def move_by_keys(event):
    if event.keysym == "Up":
        canvas.move(oval,0,-20)
    elif event.keysym == "Down":
        canvas.move(oval,0,20)
    elif event.keysym == "Left":
        canvas.move(oval,-20,0)
    elif event.keysym == "Right":
        canvas.move(oval,20,0)
        
win = tk.Tk()
label=tk.Label(win, text = " han han")
label.pack
canvas=tk.Canvas(win, bg='#0ff', width=700,heigh=700)
oval=canvas.create_oval((300,300),(500,500), fill="yellow")
canvas.pack()
win.bind("<KeyPress>",move_by_keys)
win.mainloop()
