import tictactoe
import csv
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
class Train(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Trainer")
		self.frame = tk.Frame(self)
		self.frame.pack()
		self.entry = tk.Entry(self.frame, font = ('Helvetica', 54, 'bold'))
		self.entry.insert(tk.END, "# of times")
		self.entry.bind('<ButtonRelease>', self.on_click)
		self.buttonTrain = tk.Button(self.frame, width = 6, bg = "#41B3A3", text="Train", font = ('Helvetica', 48, 'bold'), command=self.on_button)
		self.buttonClose = tk.Button(self.frame, width = 6, bg = "#E27D60", text="Close", font = ('Helvetica', 48, 'bold'), command=self.destroy)
		self.entry.config(width = 12)
		self.entry.pack()
		self.buttonTrain.pack(side = tk.RIGHT)
		self.buttonClose.pack(side = tk.LEFT)
	def on_button(self):
		n = int(self.entry.get())
		self.entry.destroy()
		self.buttonTrain.destroy()
		self.buttonClose.destroy()
		self.progress = ttk.Progressbar(self.frame, orient="horizontal", length = 1000)
		self.progress.pack(side = tk.BOTTOM)
		self.update_idletasks()
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