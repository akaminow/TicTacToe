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
                   bg="#E27D60",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command=quit)
buttonQuit.pack(side=tk.LEFT)
buttonRestart = tk.Button(frame, 
                   text="Restart", 
                   bg="#E8A87C",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command=delete.main)
buttonRestart.pack(side=tk.LEFT)
buttonTrain = tk.Button(frame,
                   text="Train", 
                   bg = "#C38D9E",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command = ticTrain.main)
buttonTrain.pack(side=tk.LEFT)
buttonPlay = tk.Button(frame,
                   text="Play", 
                   bg = "#41B3A3",
                   font=('Helvetica', 48, 'bold'),
                   height = 6,
                   width = 10,
                   command = ticPlay.main)
buttonPlay.pack(side = tk.LEFT)
root.mainloop()