import csv

def SortByTitle():
    FileName = 'Book List.csv'
    rows = []
    with open(FileName, 'r', newline='') as infile:
        csv_reader = csv.reader(infile)
        for row in csv_reader:
            rows.append(row)

    # Sort the rows based on the title (first column, index 0)
    sorted_rows = sorted(rows[1:], key=lambda x: x[0])

    with open(FileName, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerows([rows[0]])  # Header Wont Be Moved.
        csv_writer.writerows(sorted_rows)
    return None
