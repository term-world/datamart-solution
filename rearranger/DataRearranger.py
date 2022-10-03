import csv

from rich import Table
from rich import Console

DATA = None

def menu() -> any:
	n = narrator.Narrator()
	q = narrator.Question({
        "question": "\nOperation to perform:\n",
        "responses": [
            {"choice": "1 print table", "outcome": 1},
            {"choice": "2 sort table", "outcome": 2},
            {"choice": "3 rearrange columns", "outcome": 3},
			{"choice": "4 save table", "outcome": 5},
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
	with open(f"data/{filename}.csv","w",newline='') as fh:
		writer = csv.writer(fh, delimiter = ",")
		for row in DATA:
			writer.writerow(row)

def display_table(data: list = []) -> None:
	if not data: data = DATA
	else: data = [[],data]
	table = Table(title="NEIGHBORHOOD REGISTRY")
	for col in DATA[0]:
		table.add_column(col)
	for row in data[1:]:
		table.add_row(*row)
	console = Console()
	console.print(table)

def sorter(data: list = [], index: int = 0) -> list:
	return data.sort(key = lambda data: data[index])

def rearrange(data: list = [], order: list = []) -> list:
	temp = [data[0]]
	

def main():
	DATA=load()
	while True:
		response = menu()
		if not response:
			break
		if response == 1:
			pass
		if response == 2:
			pass
		if response == 3:
			pass
		if response == 4:
			pass


if __name__ == "__main__":
	main()