# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

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
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
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

# YOUR CODE HERE


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
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()