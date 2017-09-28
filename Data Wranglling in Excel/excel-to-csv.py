import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"

FIELDS = ['Year', 'Month', 'Day', 'Hour', 'Max Load']


def discover_header(sheet):
    header_array = []
    x = sheet.cell_value(0,0)
    for idx in range(0, sheet.ncols):
        header_array.append(sheet.cell_value(0, idx))

    return header_array


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    first_row = []
    data = None

    header = discover_header(sheet)

    with open(outfile, 'w+') as csvfile:
        row_writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)


        all_datas = sheet.col_values(0, start_rowx=1)
        row_writer.writerow(['Station'] + FIELDS)

        for index in range(0, len(header[1:-1])):
            all_value = sheet.col_values(index+1, start_rowx=1)
            max_value = max(all_value)
            index_of_max_value = all_value.index(max_value)
            max_value_date = xlrd.xldate_as_tuple(all_datas[index_of_max_value], 0)
            row_writer.writerow([header[index+1], max_value_date[0], max_value_date[1], max_value_date[2]
                               ,max_value_date[3] ,max_value])

    return data


def save_file(data, filename):
    pass

def test():
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']


    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in FIELDS:

                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line


                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        assert number_of_rows == 8

        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()