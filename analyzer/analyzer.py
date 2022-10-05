import csv
import narrator

from rich.table import Table
from rich.console import Console

# Do not alter ------------------------------------------
def menu() -> any:
	n = narrator.Narrator()
	q = narrator.Question({
        "question": "\nOperation to perform:\n",
        "responses": [
            {"choice": "1 print table", "outcome": 1},
            {"choice": "2 average a column", "outcome": 2},
            {"choice": "3 max value in column", "outcome": 3},
			{"choice": "4 count search term", "outcome": 4},
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
# Do not alter ------------------------------------------

def counter(term: str = "") -> int:
	count = 0
	for row in DATA:
		if term in row:
			count += 1
	return count

def max_value(column: str = "") -> any:
	max = 0
	column = COLS.index(column)
	for row in DATA:
		value = int(row[column])
		if value > max:
			max = value
	return max

def avg_column(column: str = "") -> int:
	total = 0
	values = []
	column = COLS.index(column)
	for row in DATA:
		total += row[column]
		values.append(row[column])
	return total / len(values)

def main():

	# Do not alter
	global DATA
	global COLS
	COLS = load()[0]
	DATA = load()[1:]
	# Do not alter
	
	while True:
		result = None
		response = menu()
		if not response:
			break
		if response == 1:
			display_table()
		if response == 2:
			result = avg_column(input("Column to average: "))
		if response == 3:
			result = max_value(input("Column to find max: "))
		if response == 4:
			result = counter(input("Search term: "))
		if result:
			print(result)

if __name__ == "__main__":
	main()