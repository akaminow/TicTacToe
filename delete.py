import csv
def main():
	with open('tic_tie.csv', mode = 'w') as accounts:
		csv.writer(accounts, delimiter = ',').writerow(['',''])
	with open('tic_win.csv', mode = 'w') as accounts:
		csv.writer(accounts, delimiter = ',').writerow(['',''])
	with open('tic_loss.csv', mode = 'w') as accounts:
		csv.writer(accounts, delimiter = ',').writerow(['',''])

main()
