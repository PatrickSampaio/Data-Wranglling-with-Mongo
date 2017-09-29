#omplete the 'extract_airports()' function so that it returns a list of airport
#codes, excluding any combinations like "All".

#Refer to the 'options.html' file in the tab above for a stripped down version
#of what is actually on the website. The test() assertions are based on the
#given file.

import pdb
from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):

    with open(page, "r") as html:
        soup = BeautifulSoup(html, "lxml")
    
    airports_options = soup.find("select", {"id" : "AirportList"}).findAll("option")
    all_airports_value = [airports_options["value"]  for airports_options in airports_options[2:]]
   
    del all_airports_value[all_airports_value.index("AllOthers")]
 
    return all_airports_value


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    test()
