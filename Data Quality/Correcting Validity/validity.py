import csv
import pprint
import pdb

INPUT_FILE = '../../fixtures/autos.csv'
OUTPUT_GOOD = '../../fixtures/autos-valid.csv'
OUTPUT_BAD = '../../fixtures/FIXME-autos.csv'

def check_for_url(url):
    pdb.set_trace()
    return "good"

def check_for_year_range(year):
    pdb.set_trace()
    return "good"

def check_for_year(is_year):
    pdb.set_trace()
    return "good"

def row_validations(row_dict):
    row_state = check_for_year(row_dict["productionStartYear"])
    row_state = check_for_year_range(row_dict["productionStartYear"])
    row_state = check_for_url(row_dict["URI"])
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

        #COMPLETE THIS FUNCTION
    pdb.set_trace()

    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in YOURDATA:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
