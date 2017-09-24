# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

FIELDS_CSV = ['Title', 'Released', 'Label', 'UK Chart Position', 'US Chart Position', 'BPI Certification', 'RIAA Certification']

csv_array = []


def transformLineInTODict(line):
    line_dict = {};
    line_values = line.split(',')
    yield_controller = ''

    for field in line_values:
        if yield_controller == '' :
            yield_controller = field_picker(line_dict)
            yield_controller.__next__()

        try:
            line_dict = yield_controller.send(line)
        except StopIteration:
            print("Error")

def field_picker(line_dict):

    for column in FIELDS_CSV:
        value_field = yield
        line_dict[column] = value_field

    csv_array.append(line_dict)

def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        for line in f:
            transformLineInTODict(line)
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)',
                 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum',
                 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
                 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert csv_array[0] == firstline
    assert csv_array[9] == tenthline


test()