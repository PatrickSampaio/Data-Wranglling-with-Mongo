# assume that you combined the code from the previous 2 exercises with code
#from the lesson on how to build requests, and downloaded all the data locally.
#The files are in a directory "data", named after the carrier and airport:
#"{}-{}.html".format(carrier, airport), for example "FL-ATL.html".

#The table with flight info has a table class="dataTDRight". Your task is to
#use 'process_file()' to extract the flight data from that table as a list of
#dictionaries, each dictionary containing relevant data from the file and table
#row. This is an example of the data structure you should return:

#data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#        },
#         {"courier": "..."}
#]

#Note - year, month, and the flight data should be integers.
#You should skip the rows that contain the TOTAL data for a year.

#There are couple of helper functions to deal with the data files.
#Please do not change them for grading purposes.
#All your changes should be in the 'process_file()' function.

#The 'data/FL-ATL.html' file in the tab above is only a part of the full data,
#covering data through 2003. The test() code will be run on the full table, but
#the given file should provide an example of what you will get.

from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
import pdb

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(current_file):
    #"""
    #This function extracts data from the file given as the function argument in
    #a list of dictionaries. This is example of the data structure you should
    #return:

    #data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #        },
    #        {"courier": "..."}
    #]


    #Note - year, month, and the flight data should be integers.
    #You should skip the rows that contain the TOTAL data for a year.
    #"""

    data = []
    info = {}
    info["courier"], info["airport"] = current_file[:6].split("-")
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
    with open("{}/{}".format(datadir, current_file), "r") as html:

        current_flight = {}
        current_airport = {"flights": current_flight}

        soup = BeautifulSoup(html, "lxml")

        flights_rows = soup.find("tr", { "class" : "dataTDRight" })

        for row in flights_rows:
            
            current_airport["year"] = int(flights_rows.select("td")[0].text)
            current_airport["month"] = int(flights_rows.select("td")[1].text)
            current_flight["domestic"] = int(flights_rows.select("td")[3].text)
            current_flight["international"] = float(flights_rows.select("td")[4].text)
            data.append(current_airport)

    print(data)

    return data


def test():
    print("Running a simple test...")
    #open_zip(datadir)
    files = process_all(datadir)
    data = []

    # Test will loop over three data files.
    for f in files:
        if(f == "FL-ATL.html"):
            data += process_file(f)
    
    pdb.set_trace()
    
    assert len(data) == 7  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
    print("... success!")

if __name__ == "__main__":
    test()
