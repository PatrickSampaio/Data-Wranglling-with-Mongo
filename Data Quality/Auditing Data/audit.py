import codecs
import csv
import json
import pprint
import pdb

PATH_TO_DATA = "../../fixtures/autos.csv"

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}

    with open(PATH_TO_DATA, "r") as data_csv:
        pdb.set_trace()
        csv_lines = csv.reader(data_csv)
        current_csv = []

        for i in range(2): csv_lines.next()

        for data_line in csv_lines:
            current_line = {}
            for field in FIELDS:
                try:
                   current_line[field] = type(data_line[FIELDS.index(field)])
                except IndexError:
                   print("error")
            current_csv.append(current_line)
    
    for field in FIELDS:
        current_types = []
        [current_types.append(type(current_item[field]) for current_item in current_csv if type(current_item[field]) not in current_types][
        fieldtypes[field] = current_types
    
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()

