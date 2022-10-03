import csv

def add_names(filename: str = "", data: list = []) -> None:
	data = ["Resident Name"] + data
	with open(f"data/{filename}.csv","w",newline='') as fh:
		writer = csv.writer(fh, delimiter = ",")
		for entry in data:
			writer.writerow([entry])

def main():
	names = []
	while True:
		neighbor = input("Add name to list (leave empty to quit): ")
		if not neighbor:
			break
		names.append(neighbor)
	add_names("registry", names)

if __name__ == "__main__":
	main()