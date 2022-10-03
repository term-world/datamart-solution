import csv
import narrator

from rich.table import Table
from rich.console import Console

COLS = None
DATA = None

# Do not alter ------------------------------------------
def menu() -> any:
	n = narrator.Narrator()
	q = narrator.Question({
        "question": "\nOperation to perform:\n",
        "responses": [
            {"choice": "1 print table", "outcome": 1},
            {"choice": "2 sort table", "outcome": 2},
            {"choice": "3 switch columns", "outcome": 3},
			{"choice": "4 save table", "outcome": 4},
			{"choice": "5 quit", "outcome": False}
        ]
    })
	return q.ask()

def load(filename: str = "registry") -> list:
	data = []
	with open(f"data/{filename}.csv", "r") as fh:
		reader = csv.reader(fh, delimiter=",")
		for row in reader:
			data.append(row)
	return data

def write(filename: str = "registry") -> None:
	data = [COLS] + DATA
	with open(f"data/{filename}.csv","w",newline='') as fh:
		writer = csv.writer(fh, delimiter = ",")
		for row in data:
			writer.writerow(row)
	print("TABLE SAVE SUCCESS!")

def display_table(data: list = []) -> None:
	if not data: data = DATA
	else: data = [[],data]
	table = Table(title="NEIGHBORHOOD REGISTRY")
	for col in COLS:
		table.add_column(col)
	for row in data:
		table.add_row(*row)
	console = Console()
	console.print(table)

def sorter(index: int = 0) -> list:
	DATA.sort(key = lambda DATA: DATA[index])
	display_table()
# Do not alter ------------------------------------------

def switch_columns(col_1: str = "ID", col_2: str = "Resident Name"):
	# Switch headers
	c1 = COLS.index(col_1)
	c2 = COLS.index(col_2)
	COLS[c1] = col_2
	COLS[c2] = col_1
	# Switch content
	for row in DATA:
		tmp = row[c2]
		row[c2] = row[c1]
		row[c1] = tmp

def main():

	# Do not alter
	global DATA
	global COLS
	COLS = load()[0]
	DATA = load()[1:]
	# Do not alter
	
	while True:
		response = menu()
		if not response:
			break
		if response == 1:
			display_table()
		if response == 2:
			sort_on = input("Name of column to sort: ")
			sort_idx = COLS.index(sort_on)
			sorter(sort_idx)
		if response == 3:
			col_1 = input("Column name to switch: ")
			col_2 = input("Column name to swtich with: ")
			switch_columns(col_1, col_2)
		if response == 4:
			write()


if __name__ == "__main__":
	main()