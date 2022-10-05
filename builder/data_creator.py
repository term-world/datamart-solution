import csv

# Do not alter --------------------------------------------
def add_names(data: list = []) -> None:
	with open(f"data/registry.csv","w",newline='') as fh:
		writer = csv.writer(fh, delimiter = ",")
		writer.writerow(["ID", "Resident Name"])
		for entry in data:
			writer.writerow([data.index(entry) + 1, entry])
# Do not alter --------------------------------------------

def main():
	names = []
	while True:
		neighbor = input("Add name to list (leave empty to quit): ")
		if not neighbor:
			break
		names.append(neighbor)
	add_names(names)

if __name__ == "__main__":
	main()