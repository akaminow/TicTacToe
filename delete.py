import csv
def main():
	with open('Data_Files/tic_tie.csv', mode = 'w') as accounts:
		csv.writer(accounts, delimiter = ',').writerow(['',''])
	with open('Data_Files/tic_win.csv', mode = 'w') as accounts:
		csv.writer(accounts, delimiter = ',').writerow(['',''])
	with open('Data_Files/tic_loss.csv', mode = 'w') as accounts:
		csv.writer(accounts, delimiter = ',').writerow(['',''])
if __name__ == '__main__':
	main()