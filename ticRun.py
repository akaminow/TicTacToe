import tkinter as tk
import tkinter.font as tkFont
import ticTrain
import ticPlay
import delete
root = tk.Tk()
root.title("Menu")
frame = tk.Frame(root)
frame.pack()
buttonQuit = tk.Button(frame, 
                   text="QUIT", 
                   bg="red",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command=quit)
buttonQuit.pack(side=tk.LEFT)
buttonRestart = tk.Button(frame, 
                   text="Restart", 
                   bg="yellow",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command=delete.main)
buttonRestart.pack(side=tk.LEFT)
buttonTrain = tk.Button(frame,
                   text="Train", 
                   bg = "blue",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command = ticTrain.main)
buttonTrain.pack(side=tk.LEFT)
buttonPlay = tk.Button(frame,
                   text="Play", 
                   bg = "green",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command = ticPlay.main)
buttonPlay.pack(side = tk.LEFT)
root.mainloop()