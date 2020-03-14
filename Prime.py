import csv
with open('TB_data_dictionary_2020-03-02.csv') as file:
    reader = csv.reader(file)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)


