import random
import csv
import os
class Tic:
	def __init__(self):
			self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			self.fileWin = 'tic_win.csv'
			self.fileTie = 'tic_tie.csv'
			self.fileCurrent = 'tic_current.csv'
			self.fileLoss = 'tic_loss.csv'
			self.computerNum = '0'
			self.personNum = '0'
			self.allNum = '0'
			self.next = 0
			self.counter = 0
	def personHasWon(self):
		person = self.personArr()
		hasWon = False
		if ('1' in person and '2' in person and '3' in person)\
		 or ('4' in person and '5' in person and '6' in person)\
		 or ('7' in person and '8' in person and '9' in person)\
		 or ('1' in person and '4' in person and '7' in person)\
		 or ('2' in person and '5' in person and '8' in person)\
		 or ('3' in person and '6' in person and '9' in person)\
		 or ('1' in person and '5' in person and '9' in person)\
		 or ('3' in person and '5' in person and '7' in person):
			hasWon = True
		return hasWon
	def computerHasWon(self):
		computer = self.computerArr()
		hasWon = False
		if ('1' in computer and '2' in computer and '3' in computer)\
		 or ('4' in computer and '5' in computer and '6' in computer)\
		 or ('7' in computer and '8' in computer and '9' in computer)\
		 or ('1' in computer and '4' in computer and '7' in computer)\
		 or ('2' in computer and '5' in computer and '8' in computer)\
	     or ('3' in computer and '6' in computer and '9' in computer)\
		 or ('1' in computer and '5' in computer and '9' in computer)\
		 or ('3' in computer and '5' in computer and '7' in computer):
			hasWon = True
		return hasWon
	def addToCSV(self):
		person = self.personPlay()
		AI = self.firstMove()
		with open(self.fileCurrent, 'a') as append:
			writer = csv.writer(append, delimiter = ',')
			writer.writerow([person, AI])
		while not(self.personHasWon() or self.computerHasWon()) and self.list != []:
			self.showBoard()
			person = self.personPlay()
			self.computerCheck()
			AI = self.AIRun()
			with open(self.fileCurrent, 'a') as append:
				writer = csv.writer(append, delimiter = ',')
				writer.writerow([person, AI])
	def personPlay(self):
		personNum = int(input("Where would you like to go: "))
		if personNum in self.list:
			self.list.remove(personNum)
		else:
			self.personPlay()
		self.allNum += str(personNum)
		self.personNum += str(personNum)
		return personNum
	def computerRun(self):
		computerNum = random.choice(self.list)
		self.list.remove(computerNum)
		self.allNum += str(computerNum)
		self.personNum += str(computerNum)
		return computerNum
	def AIRun(self):
		if self.next != 0 and self.next in self.list:
			AINum = self.next
			self.list.remove(AINum)
			self.allNum += str(AINum)
			self.computerNum += str(AINum)
			return AINum
		elif self.list != []:
			AINum = random.choice(self.list)
			self.list.remove(AINum)
			self.allNum += str(AINum)
			self.computerNum += str(AINum)
			return AINum
	def firstMove(self):
		if 5 in self.list:
			self.list.remove(5)
			self.allNum += '5'
			self.computerNum += '5'
			return 5
		else:
			self.list.remove(1)
			self.allNum += '1'
			self.computerNum += '1'
			return 1
	def personArr(self):
		person = []
		with open(self.fileCurrent, 'r') as rf:
			reader = csv.reader(rf, delimiter = ',')
			for row in reader:
				person.append(row[0])
		return person
	def computerArr(self):
		computer = []
		with open(self.fileCurrent, 'r') as rf:
			reader = csv.reader(rf, delimiter = ',')
			for row in reader:
				computer.append(row[1])
		return computer
	def showBoard(self):
		person = self.personArr()
		computer = self.computerArr()
		for num in range(1, 10):
			if num in self.list:
				print ("\t" + str(num), end = "")
			elif str(num) in person:
				print("\tO", end = "")
			elif str(num) in computer:
				print("\tX", end = "")
			if num % 3 == 0:
				print("")
	def showEmptyBoard(self):
		for num in range(1, 10):
			print("\t" + str(num), end="")
			if num % 3 == 0:
				print("")
	def computerCheck(self):
		self.next = 0
		numWin = ''
		with open(self.fileWin, 'r') as rf:
		    reader = csv.reader(rf, delimiter = ',')
		    for row in reader:
		    	if len(row) > 1:
		    		numWin += str(row[1])
		numLoss = ''
		with open(self.fileLoss, 'r') as rf:
		    reader = csv.reader(rf, delimiter = ',')
		    for row in reader:
		    	if len(row) > 1:
		    		numLoss += str(row[0])
		bigNum = ''
		with open(self.fileTie, 'r') as rf:
		    reader = csv.reader(rf, delimiter = ',')
		    for row in reader:
		    	if len(row) > 1:
		    		bigNum += str(row[0]) + str(row[1])
		canWin = False
		inWin = []
		if self.computerNum in numWin:
			temp = numWin
			for count in range(numWin.count(self.computerNum)):
				if str(temp[1]) == '0' and int(temp[0]) in self.list:
					self.next = int(temp[0])
					canWin = True
					break
				elif self.next == 0 and len(temp) > 2 and str(temp[2]) == '0'\
				 and int(temp[1]) in self.list and int(temp[0]) in self.list:
				 	inWin.append(int(temp[0]))
				temp = temp[-(len(temp)-temp.index(self.computerNum)\
					-len(self.computerNum)):]
		if self.personNum in numLoss and not(canWin):
			canLose = False
			already = []
			temp = numLoss
			notIn = inWin
			for count in range(numLoss.count(self.personNum)):
				temp = temp[-(len(temp)-temp.index(self.personNum)\
					-len(self.personNum)):]
				if (len(temp) == 1 or (len(temp) > 1 and str(temp[1]) == '0')) and int(temp[0]) in self.list:
					self.next = int(temp[0])
					canLose = True
					break
				elif len(temp) > 2 and str(temp[2]) == '0'\
				 and int(temp[1]) in self.list and int(temp[0]) in self.list\
				 and (inWin == [] or int(temp[1]) in inWin):
				 	for num in already:
				 		if not(temp[0] in num) and temp[1] in num:
				 			self.next = int(temp[0])
				 	already.append(temp[0] + temp[1])
		if self.allNum in bigNum and self.next == 0 and len(self.allNum) > 3 and\
		 len(bigNum) > bigNum.index(self.allNum) + len(self.allNum):
			self.next = int(bigNum[bigNum.index(self.allNum)+len(self.allNum)])
	def shouldAdd(self):
		numWin = ''
		with open(self.fileWin, 'r') as rf:
		    reader = csv.reader(rf, delimiter = ',')
		    for row in reader:
		    	if len(row) > 1:
		    		numWin += str(row[1])
		numLoss = ''
		with open(self.fileLoss, 'r') as rf:
		    reader = csv.reader(rf, delimiter = ',')
		    for row in reader:
		    	if len(row) > 1:
		    		numLoss += str(row[0])
		bigNum = ''
		with open(self.fileTie, 'r') as rf:
		    reader = csv.reader(rf, delimiter = ',')
		    for row in reader:
		    	if len(row) > 1:
		    		bigNum += str(row[0]) + str(row[1])
		if self.personHasWon() and not(self.personNum in numLoss):
			return True
		elif self.computerHasWon() and not(self.computerNum in numWin):
			return True
		elif not(self.personHasWon() or self.computerHasWon()) and not(self.allNum in bigNum):
			return True
		else:
			return False
	def addInTie(self):
		with open(self.fileCurrent, 'r') as rf:
			reader = csv.reader(rf, delimiter = ',')
			with open (self.fileTie, 'a') as append:
				writer = csv.writer(append)
				for row in reader:
					writer.writerow([row[0], row[1]])
	def addInWin(self):
		with open(self.fileCurrent, 'r') as rf:
			reader = csv.reader(rf, delimiter = ',')
			with open (self.fileWin, 'a') as append:
				writer = csv.writer(append)
				for row in reader:
					writer.writerow([row[0], row[1]])
	def addInLoss(self):
		with open(self.fileCurrent, 'r') as rf:
			reader = csv.reader(rf, delimiter = ',')
			with open (self.fileLoss, 'a') as append:
				writer = csv.writer(append)
				for row in reader:
					writer.writerow([row[0], row[1]])
	def play(self):
		self.showEmptyBoard()	
		f = open(self.fileCurrent, 'w+')
		f.close()
		self.addToCSV()
		if self.personHasWon() and self.shouldAdd():
			self.addInLoss()
		elif self.computerHasWon() and self.shouldAdd():
			self.addInWin()
		elif self.shouldAdd():
			self.addInTie()
		if self.personHasWon():
			self.counter = 1
def main():
	counter = 0
	for num in range(1, 1000000):
	# while counter == 0:
		game = Tic()
		game.play()
		counter += game.counter
		print(counter/num)
		print(str(counter)+'/'+str(num))
main()
