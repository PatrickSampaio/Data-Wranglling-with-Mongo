import csv
import pprint
import pdb
import datetime
import re
from dateutil import parser

INPUT_FILE = '../../fixtures/autos.csv'
OUTPUT_GOOD = '../../fixtures/autos-valid.csv'
OUTPUT_BAD = '../../fixtures/FIXME-autos.csv'
REGEX_IS_DATE = re.compile("^\\d{4}[-]?\\d{1,2}[-]?\\d{1,2}T\\d{1,2}:\\d{1,2}:\\d{1,2}[,]?\\d{1,3}")
REGEX_IS_URL = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

def check_for_url(url):
    if REGEX_IS_URL.match(url) != None:
        return "good"
    else:
        return "bad" 

def check_for_year_range(year):

    year = parser.parse(year)
    if(year.year >= 1886 and year.year <= 2014):
        return "good"
    else:
        return "bad"

def check_for_year(is_year):
    if REGEX_IS_DATE.match(is_year) != None:
        return "good"
    else:
        return "bad"

def row_validations(row_dict):
    row_state = check_for_year(row_dict["productionStartYear"])
    row_state = check_for_year_range(row_dict["productionStartYear"]) if row_state == "good" else "bad"
    row_state =  check_for_url(row_dict["URI"]) if row_state == "good" else "bad"
    return row_state
	
	

def process_file(input_file, output_good, output_bad):

    current_file = []
    good_file = []
    bad_file = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for row in reader:
            row_dict = {}

            for field in header:
                row_dict[field] = row[field]

            is_good_file = row_validations(row_dict)
            if is_good_file == "good" :
                good_file.append(row_dict)
            elif is_good_file == "bad" :
                bad_file.append(row_dict)

    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for file_row in good_file:
            writer.writerow(file_row)

    with open(output_bad, "w") as b:
        writer = csv.DictWriter(b, delimiter=",", fieldnames= header)
        writer.writeheader()
        for file_row in bad_file:
            writer.writerow(file_row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
