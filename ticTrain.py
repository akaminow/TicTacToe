import tictactoe
import csv
import tkinter as tk
import tkinter.font as tkFont
class Train(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.frame = tk.Frame(self)
		self.frame.pack()
		self.entry = tk.Entry(self.frame, font = ('Helvetica', 54, 'bold'))
		self.buttonTrain = tk.Button(self.frame, bg = "green", text="Train", font = ('Helvetica', 48, 'bold'), command=self.on_button)
		self.buttonQuit = tk.Button(self.frame, bg = "red", text="Quit", font = ('Helvetica', 48, 'bold'), command=self.destroy)
		self.entry.config(width = 8)
		self.entry.pack()
		self.buttonTrain.pack(side = tk.RIGHT)
		self.buttonQuit.pack(side = tk.LEFT)
	def on_button(self):
		n = int(self.entry.get())
		for num in range(n):
			trainer = tictactoe.TicTrain()
			trainer.play()
		self.destroy()
def main():
	trainer = Train()
	trainer.mainloop()
if __name__ == "__main__":
	main()