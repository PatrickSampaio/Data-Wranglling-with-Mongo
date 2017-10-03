import codecs
import csv
import json
import pprint
import pdb

CITIES = '../../fixtures/cities.csv'
REGEX_AREA = regex = re.compile("^{.*\}$")

def fix_area(area):

    pdb.set_trace()

    return area



def process_file(filename):
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        for i in range(3):
            l = reader.next()

        for line in reader:
            
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] == None        
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()
