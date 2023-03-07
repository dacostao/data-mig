import csv

class ExtractCSV():

    def extract_file(file_path):
        data = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
