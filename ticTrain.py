import tictactoe
import csv
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
class Train(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.frame = tk.Frame(self)
		self.frame.pack()
		self.progress = ttk.Progressbar(self.frame, orient="horizontal", length = 500)
		self.progress.pack(side = tk.BOTTOM)
		self.entry = tk.Entry(self.frame, font = ('Helvetica', 54, 'bold'))
		self.entry.insert(tk.END, "# of times")
		self.entry.bind('<ButtonRelease>', self.on_click)
		self.buttonTrain = tk.Button(self.frame, width = 6, bg = "green", text="Train", font = ('Helvetica', 48, 'bold'), command=self.on_button)
		self.buttonQuit = tk.Button(self.frame, width = 6, bg = "red", text="Close", font = ('Helvetica', 48, 'bold'), command=self.destroy)
		self.entry.config(width = 10)
		self.entry.pack()
		self.buttonTrain.pack(side = tk.RIGHT)
		self.buttonQuit.pack(side = tk.LEFT)
	def on_button(self):
		n = int(self.entry.get())
		for num in range(1, n+1):
			trainer = tictactoe.TicTrain()
			trainer.play()
			self.progress["value"] = int(num/n*100)
			self.update_idletasks()
		self.destroy()
	def on_click(self, event):
		self.entry.delete(0, tk.END)
def main():
	trainer = Train()
	trainer.mainloop()
if __name__ == "__main__":
	main()