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