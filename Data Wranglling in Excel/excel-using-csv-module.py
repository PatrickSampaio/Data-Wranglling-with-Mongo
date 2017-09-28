import csv
import os

from webencodings import UTF8

DATADIR = ""
DATAFILE = "745090TYA.CSV"


def parse_file(datafile):
    name = ""
    data = []

    with open(datafile,'r') as csvfile:
        spamreader = csv.reader(csvfile)
        list_actual = []

        name = spamreader.__next__()[1]
        spamreader.__next__()

        for row in spamreader:
            data.append(row)



    return (name, data)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()