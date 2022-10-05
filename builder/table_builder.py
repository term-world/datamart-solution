import csv
import narrator

from rich.table import Table
from rich.console import Console

DATA = None
COLS = None

# Do not alter --------------------------------------------
def menu() -> any:
	n = narrator.Narrator()
	q = narrator.Question({
        "question": "\nOperation to perform:\n",
        "responses": [
            {"choice": "1 row retrieval ", "outcome": 1},
            {"choice": "2 add to a row ", "outcome": 2},
            {"choice": "3 add a column ", "outcome": 3},
			{"choice": "4 remove from row ", "outcome": 4},
			{"choice": "5 save file ", "outcome": 5},
			{"choice": "6 print table ", "outcome": 6},
			{"choice": "7 quit", "outcome": False}
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
# Do not alter --------------------------------------------

def get_row(row_num: int = 1) -> list:
	row = DATA[row_num - 1]
	return row

def add_column(entry: any = None) -> bool:
	COLS.append(entry)
	return True

def add_to_row(row_num: int = 1, entry: any = None) -> bool:
	row = DATA[row_num - 1]
	row.append(entry)
	return True

def remove_from_row(row_num: int = 0) -> bool:
	DATA[row_num - 1].pop()
	return True

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
		elif response == 1:
			row_num = int(input("Input row number: "))
			row = get_row(row_num)
			display_table(row)
		elif response == 2:
			row_num = int(input("Input row number: "))
			entry = input("Data to add: ")
			if add_to_row(row_num, entry): print("ROW ADD SUCCESS!")
			else: print("ROW ADD FAILED!")
		elif response == 3:
			entry = input("Column to add: ")
			if add_column(entry): print("COLUMN ADD SUCCESS!")
			else: print("COLUMN ADD FAILED!")
		elif response == 4:
			entry = int(input("Row to prune: "))
			if remove_from_row(entry): print("REMOVE SUCCESSFUL!")
			else: print("REMOVE FAILED!")
		elif response == 5:
			write()
		elif response == 6:
			display_table()

if __name__ == "__main__":
	main()