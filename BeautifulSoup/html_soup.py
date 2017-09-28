import pdb
from bs4 import BeautifulSoup
import requests
import json

html_page = "fixtures/page_source.html"

EVENT_VALIDATION_ID = "__EVENTVALIDATION"
VIEW_STATE_ID = "__VIEWSTATE"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
	
    pdb.set_trace()

    with open(page, "r") as html:

	    soup = BeautifulSoup(html)
	    data['eventvalidation'] = soup('input', { "id" : EVENT_VALIDATION_ID })[0]['value']
	    data['viewstate'] = soup('input', { "id" : VIEW_STATE_ID })[0]['value']

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                      data={'AirportList': "BOS",
                            'CarrierList': "VX",
                            'Submit': 'Submit',
                            "__EVENTTARGET": "",
                            "__EVENTARGUMENT": "",
                            "__EVENTVALIDATION": eventvalidation,
                            "__VIEWSTATE": viewstate
                            })

    return r.text


def test():
    data = extract_data(html_page)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")


test()
